"""
DDD - Domain Driven Design

This code example omits DAL (Data Access Layer) which encapsulates DB -> gives simple DB swao, example:

class PlayerContentRepository(ABC):
    # ...
    
    @abstractmethod
    def get(**kwargs):
        ''''Interface for getting the PlayerContent object'''
"""
from typing import Union, List
from shared import Model

GUID = int


# '''''''''''''''''''''''''''''''''''''''''''''' #
# Player Domain
# '''''''''''''''''''''''''''''''''''''''''''''' #
class PlayerContent(Model):
    """
    Mainly what we show to the user.
    It can be a video, text, image, etc. 
    API should be provided by the team resp. for player.
    They should tell what shape this body should have."""
    id: int
    bucket_url: str


# '''''''''''''''''''''''''''''''''''''''''''''' #
# Course Domain
# '''''''''''''''''''''''''''''''''''''''''''''' #
class Page(Model):
    """Pages are our smallest unit of content."""
    id: GUID
    title: str
    page_number: int
    player_content: PlayerContent

    def get_content(self) -> PlayerContent:
        return self.player_content


class Lesson(Model):
    """Lessons are collection of pages."""
    id: GUID
    title: str
    pages: List[Page]  # through: lesson_pages table (id | lesson_id | page_id)

    def __int__(self):
        self.pages = sorted(self.pages, key=lambda page: page.page_number)

    def get_pages_content(self) -> List[PlayerContent]:
        return [page.get_content() for page in self.pages]


class Chapter(Model):
    """
    Chapter are recursive collection of lessons/pages.

    /parent=None
    /chapter1
        /chapter2
            /chapter3
            /chapter4
    """
    id: int
    parent: Union['Chapter', None]
    data: Union[Lesson, Page]


class CourseSettings(Model):
    """Contains settings for course."""
    course: 'Course'
    is_visible_for_non_premium: bool = False
    is_adaptive: bool = False

    @staticmethod
    def create_from_dict(settings: dict = {}):
        if 'course' not in settings:
            raise ValueError('Course relation is required')
        return CourseSettings.objects.create(**settings)


class Course(Model):
    """Contains meta and structure information about course."""
    id: int
    rank: int
    state: str = 'draft'
    chapters: List[Chapter]  # through: course_chapters table (id | course_id | chapter_id)
    settings: CourseSettings


# '''''''''''''''''''''''''''''''''''''''''''''' #
# Import/Export Domain
# '''''''''''''''''''''''''''''''''''''''''''''' #
class CourseExport(Model):
    id: int
    course: Course
    state: str = 'not_started'

    def export(self):
        pass


class CourseImport(Model):
    id: int
    course: Course
    state: str = 'not_started'

    def import_(self):
        pass


class AssessmentImport(Model):
    id: int
    assessment: 'Assessment'
    state: str = 'not_started'

    def import_(self):
        pass


# '''''''''''''''''''''''''''''''''''''''''''''' #
# Assessment Domain
# '''''''''''''''''''''''''''''''''''''''''''''' #
class Assessment(Model):
    id: int
    content: PlayerContent
    state: str = 'draft'

    @staticmethod
    def create_from_content(content: PlayerContent):
        return Assessment.objects.create(content=content)


class Course2(Model):  # Should be named Course, because of the same file
    """
    If we still need course representation for Assessment purposes, we should create another model for that.
    """
    id: int
    pages: List[Page] = []


# '''''''''''''''''''''''''''''''''''''''''''''' #
# Search Domain
# '''''''''''''''''''''''''''''''''''''''''''''' #
class Searchable(Model):
    """Searchable is a generic model that can be searched. It can be a course, lesson, page, etc."""
    id: GUID
    title: str
    url: str
    relevance: float  # or some inverted index mechanism like elasticsearch or meilisearch utilizes
