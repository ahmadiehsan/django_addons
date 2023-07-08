from abc import ABC, abstractmethod

from django.conf import settings


class IOptionStrategy(ABC):
    @abstractmethod
    def fill_options(self):
        pass

    @classmethod
    def _get(cls, nested_key, default_value):
        try:
            value = cls._get_nested_key_from_dict(settings.USER_MANAGEMENT, nested_key)
        except (KeyError, AttributeError):
            value = default_value

        return value

    @classmethod
    def _get_nested_key_from_dict(cls, nested_dict, nested_key):
        source_dict = nested_dict

        for key in nested_key.split('.'):
            lookup_key = key
            source_dict = source_dict[lookup_key]

        value = source_dict

        return value
