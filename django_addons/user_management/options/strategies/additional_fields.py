from django_addons.user_management.options.strategies.interface import IOptionStrategy


class AdditionalFieldsOptionStrategy(IOptionStrategy):
    def fill_options(self):
        return {"user": tuple(self._get("additional_fields.user", {}).keys())}
