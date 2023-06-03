from shared import Model


class Course(Model):
    id: int
    # We can remove is_assessment
    # is_assessment = False

    def import_course(self):
        # ... business logic
        return self


# Solution: With another model :) PROBABLY BETTER THAT PREV ONE
# Maybe good enough for now, but it's not a best solution
class CourseAssessment(Model):
    id: int
    course: Course  # foreign key: int

    def import_course(self):
        # ... business logic
        return self.course

    @staticmethod
    def from_course(course: Course):
        return CourseAssessment.objects.create(course=course)


course_assessment = CourseAssessment.from_course(Course.objects.get(pk=1))
