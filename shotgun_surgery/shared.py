from dataclasses import dataclass


@dataclass
class Response:
    data: dict


class Manager(object):
    def get(self, **kwargs):
        return Course()

    def filter(self, **kwargs):
        pass

    def create(self, **kwargs):
        pass


@dataclass
class Model:
    objects = Manager()

    def save(self):
        pass


class Course(Model):
    title = ''
    is_assessment = False
