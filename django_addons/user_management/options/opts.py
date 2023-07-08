from django_addons.django_helper.utils.singleton_meta import SingletonMeta
from django_addons.user_management.options.strategies.additional_fields import AdditionalFieldsOptionStrategy
from django_addons.user_management.options.strategies.apis import APIsOptionStrategy
from django_addons.user_management.options.strategies.email_data import EmailDataOptionStrategy
from django_addons.user_management.options.strategies.interface import IOptionStrategy


class UserManagementOptions(metaclass=SingletonMeta):
    def __init__(
        self,
        additional_fields_strategy: IOptionStrategy,
        apis_strategy: IOptionStrategy,
        email_data_strategy: IOptionStrategy,
    ):
        self.additional_fields = additional_fields_strategy.fill_options()
        self.apis = apis_strategy.fill_options()
        self.email_data = email_data_strategy.fill_options()


USER_MANAGEMENT_OPTIONS = UserManagementOptions(
    AdditionalFieldsOptionStrategy(), APIsOptionStrategy(), EmailDataOptionStrategy()
)
