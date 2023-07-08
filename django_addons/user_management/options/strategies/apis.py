from django_addons.django_helper.utils.module_tool import get_class_from_full_path
from django_addons.user_management.options.strategies.interface import IOptionStrategy


class APIsOptionBuilder:
    def __init__(self, option_getter):
        self._get = option_getter
        self._apis = {}

    def add_api(
        self, section_name, api_name, is_active_default_value: bool, permission_classes_default_value: list[str] = None
    ):
        self._apis.setdefault(section_name, {}).setdefault(api_name, {})

        self._apis[section_name][api_name]['is_active'] = self._get(
            f'apis.{section_name}.{api_name}.is_active', is_active_default_value
        )

        if permission_classes_default_value:
            self._apis[section_name][api_name]['permission_classes'] = self._list_of_str_to_list_of_class(
                self._get(f'apis.{section_name}.{api_name}.permission_classes', permission_classes_default_value)
            )

    def get_result(self):
        return self._apis

    @staticmethod
    def _list_of_str_to_list_of_class(list_of_str):
        new_list = []

        for path_str in list_of_str:
            new_list.append(get_class_from_full_path(path_str))

        return new_list


class APIsOptionStrategy(IOptionStrategy):
    def fill_options(self):
        is_authenticated_perm = 'rest_framework.permissions.IsAuthenticated'
        django_model_full_perm = (
            'apps.django_helper.drf.permissions.django_model_full_permissions.DjangoModelFullPermissions'
        )
        can_add_user_perm = 'apps.user_management.permissions.user.crud.CanAddUserPermission'

        builder = APIsOptionBuilder(self._get)
        builder.add_api(section_name='user', api_name='login', is_active_default_value=True)
        builder.add_api(
            section_name='user',
            api_name='change_email',
            is_active_default_value=True,
            permission_classes_default_value=[is_authenticated_perm],
        )
        builder.add_api(
            section_name='user',
            api_name='change_password',
            is_active_default_value=True,
            permission_classes_default_value=[is_authenticated_perm],
        )
        builder.add_api(
            section_name='user',
            api_name='crud',
            is_active_default_value=True,
            permission_classes_default_value=[django_model_full_perm],
        )
        builder.add_api(
            section_name='user',
            api_name='search',
            is_active_default_value=True,
            permission_classes_default_value=[is_authenticated_perm],
        )
        builder.add_api(section_name='user', api_name='forgot_password', is_active_default_value=True)
        builder.add_api(
            section_name='user',
            api_name='invitation',
            is_active_default_value=True,
            permission_classes_default_value=[is_authenticated_perm],
        )
        builder.add_api(section_name='user', api_name='registration', is_active_default_value=True)
        builder.add_api(
            section_name='group',
            api_name='crud',
            is_active_default_value=True,
            permission_classes_default_value=[django_model_full_perm],
        )
        builder.add_api(
            section_name='group',
            api_name='assignment',
            is_active_default_value=True,
            permission_classes_default_value=[can_add_user_perm],
        )
        builder.add_api(
            section_name='permission',
            api_name='crud',
            is_active_default_value=True,
            permission_classes_default_value=[django_model_full_perm],
        )
        builder.add_api(
            section_name='permission',
            api_name='assignment',
            is_active_default_value=True,
            permission_classes_default_value=[can_add_user_perm],
        )
        builder.add_api(
            section_name='verification_code',
            api_name='crud',
            is_active_default_value=True,
            permission_classes_default_value=[django_model_full_perm],
        )

        return builder.get_result()
