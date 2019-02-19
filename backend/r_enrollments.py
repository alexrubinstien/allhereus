from core.models import *

import logging


def yo(text):
    print("***YO: {}".format(text))


logging.getLogger().setLevel(logging.DEBUG)

# TODO: specify the district ID
from core import roster
EDNUDGE_HOST="3.93.153.40"

r=roster.Roster(EDNUDGE_HOST)

district_id='d:39761370-c5bb-41e8-88a3-10d6d21ffbd7'

en_learners = r.ednudge_get_learners(district_id)
en_instructors = r.ednudge_get_instructors(district_id)

eenrollments = r.ednudge_get_enrollments(district_id).data

esections = r.ednudge_get_sections(district_id).data

for en in eenrollments:
    yo("school_id:{}, enrollment_id:{}".format(en.school_id, en.id))
    roster_action="N"

    if en.person_type == "learner":
        sl_roster_action = "N"
        try:
            ah_section_student = SectionStudent.objects.get(
                ednudge_is_enabled = True,
                ednudge_enrollment_id=en.id
            )
        except SectionStudent.DoesNotExist:
            ah_section_student = None
            sl_roster_action = "C"

        # Ensure Student Exists
        student_roster_action = "N"
        try:
            ah_student = Student.objects.get(
                ednudge_is_enabled = True,
                ednudge_learner_id = en.person_id
            )
        except Student.DoesNotExist:
            ah_student = None
            student_roster_action = "C"

        if student_roster_action == "C":
            yo("en:{}".format(en))
            en_learner = [x for x in en_learners.data 
                if x.id == en.person_id]
            if len(en_learner) == 0:
                yo("en.person_id={}, en.person_type={} not found.".format(
                    en.person_id, en.person_type
                ))
                continue
            if len(en_learner) > 1:
                yo("We found more than one learner with person_id={}. SKIPPING....".format(en.person_id))
                continue
            
            # Get the en_learner so that we're not working with a list
            en_learner = en_learner[0]

            yo("Found en_learner:{}".format(en_learner))
            school = School.objects.get(
                ednudge_is_enabled = True,
                ednudge_school_id = en.school_id
            )
            district = District.objects.get(
                ednudge_is_enabled = True,
                ednudge_district_id = district_id
            )
            ah_student = Student.objects.create(
                ednudge_is_enabled = True,
                ednudge_learner_id = en_learner.id,
                ednudge_learner_local_id = en_learner.local_id,
                student_id = en_learner.local_id,
                first_name = en_learner.first_name,
                last_name = en_learner.last_name,
                language = en_learner.home_language,
                email = en_learner.email,
                grade = en_learner.grade,
                school = school,
                district = district
            )
            yo("Created Student: {}".format(ah_student))

        if sl_roster_action == "C":
            yo("en:{}".format(en))
            ah_section = Section.objects.get(
                ednudge_is_enabled = True,
                ednudge_section_id = en.section_id)
            yo("ah_section:{}".format(ah_section))
            ah_student = ah_student

            ah_sectionstudent = SectionStudent.objects.create(
                section = ah_section,
                student = ah_student,
                ednudge_is_enabled = True,
                ednudge_enrollment_id = en.id,
                ednudge_section_id = en.section_id,
                ednudge_person_id = en.person_id   
            )
 
    if en.person_type == "instructor":
        print("instructor")
        st_roster_action = "N"
        try:
            ah_section_teacher = SectionTeacher.objects.get(
                ednudge_is_enabled = True,
                ednudge_enrollment_id=en.id
            )
        except SectionTeacher.DoesNotExist:
            ah_section_teacher = None
            st_roster_action = "C"

        # Ensure Teacher Exists
        teacher_roster_action = "N"
        try:
            ah_teacher = MyUser.objects.get(
                ednudge_is_enabled = True,
                ednudge_person_id = en.person_id
            )
        except MyUser.DoesNotExist:
            ah_teacher = None
            teacher_roster_action = "C"

        if teacher_roster_action == "C":
            yo("en:{}".format(en))
            en_instructor = [x for x in en_instructors.data 
                if x.id == en.person_id]
            if len(en_instructor) == 0:
                yo("en.person_id={}, en.person_type={} not found.".format(
                    en.person_id, en.person_type
                ))
                continue
            if len(en_instructor) > 1:
                yo("We found more than one instructor with person_id={}. SKIPPING....".format(en.person_id))
                continue
            
            # Get the en_instructor so that we're not working with a list
            en_instructor = en_instructor[0]

            # Ensure instructor's email is unique
            instructor_email = en_instructor.email
            try:
                test = MyUser.objects.get(email=instructor_email)
            except MyUser.DoesNotExist:
                # yo("Found a user with the same email address.  Skipping..... {}".format(test))
                # TODO: uncomment ```continue```
                #continue
                yo("Creating a fake email address and continuing....")
                instructor_email = "noemail-{}@allhere.com".format(en_instructor.id)

            yo("Found en_instructor:{}".format(en_instructor))
            school = School.objects.get(
                ednudge_is_enabled = True,
                ednudge_school_id = en.school_id
            )
            district = District.objects.get(
                ednudge_is_enabled = True,
                ednudge_district_id = district_id
            )
            ah_teacher = MyUser.objects.create(
                ednudge_is_enabled = True,
                ednudge_person_id = en_instructor.id,
                ednudge_person_local_id = en_instructor.local_id,
                ednudge_person_type = en.person_type,

                school = school,
                district = district,

                role = 'T',

                first_name = en_instructor.first_name,
                last_name = en_instructor.last_name,

                email = instructor_email
            )
            yo("Created Teacher: {} with email: {}".format(ah_teacher, ah_teacher.email))

        if st_roster_action == "C":
            yo("en:{}".format(en))
            ah_section = Section.objects.get(
                ednudge_is_enabled = True,
                ednudge_section_id = en.section_id)
            yo("ah_section:{}".format(ah_section))

            ah_sectionteacher = SectionTeacher.objects.create(
                section = ah_section,
                teacher = ah_teacher,
                ednudge_is_enabled = True,
                ednudge_enrollment_id = en.id,
                ednudge_section_id = en.section_id,
                ednudge_person_id = en.person_id   
            )

            yo("ah_sectionteacher: {}".format(ah_sectionteacher))