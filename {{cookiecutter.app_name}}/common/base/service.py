from django.db import transaction

class BaseService:
    """
    Base Service with transaction handling
    """
    @staticmethod
    @transaction.atomic
    def atomic_exceute(func, *args, **kwargs):
        return func(*args, kwargs)
