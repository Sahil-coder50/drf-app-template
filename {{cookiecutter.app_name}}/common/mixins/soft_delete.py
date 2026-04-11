from django.db import models

class SoftDeleteMixin:
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()
