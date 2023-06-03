from shared import Model


# Super Ultra Fast Fix: added import_course method to the model (naive solution)
class Course(Model):
    title = ''
    is_assessment = False

    def import_course(self, opts=None):
        if opts and opts.get('is_assessment'):
            self.is_assessment = True
        # ... business logic
        self.save()
        return self
