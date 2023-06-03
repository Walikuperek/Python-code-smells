"""
Shotgun surgery is a code smell that occurs when a single change to the source requires
many different changes in other source files. Shotgun surgery is often a sign of bad design,
and thus should be refactored. It is a form of code duplication.

Problem is that we made bad models, and now we need to change them.
"""
from shared import Course, Response


def import_course(course_id):
    """Given function 1 somewhere in the codebase"""
    course = Course.objects.get(pk=course_id)
    course.is_assessment = True  # was set during development in 1 ticket for some business reason
    # ... some more business logic
    course.save()
    return course


def async_import_course(course_id):
    """Given function 2 somewhere else in the codebase"""
    course = Course.objects.get(pk=course_id)
    # ... business logic
    course.save()
    return course


class ImportedCourseDetailsView(object):
    """"Someone joins the team and was ticketed to implement a new feature with details for the course"""

    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        # Omitted course.is_assessment = True logic
        # so result will be shown only for some users group :(
        return Response(data=course.__dict__)
