# Django Addons

## django_helper

### Activate

```python
INSTALLED_APPS = [
    ...,
    django_addons.user_management.apps.UserManagementConfig,
]
```

### Django Model

```python
from django_addons.django_helper.models.base import AbstractBaseModel

class SampleModel(AbstractBaseModel):
    ...
```

```python
from django_addons.django_helper.models.id_only import AbstractIDOnlyModel

class SampleModel(AbstractIDOnlyModel):
    ...
```

```python
from django_addons.django_helper.models.base_user import AbstractExtendedBaseUser

class User(AbstractExtendedBaseUser):
    ...

AUTH_USER_MODEL = 'sample_app.User'
```

### Django Admin

```python
from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django_addons.django_helper.admin.base_user import ExtendedBaseUserAdmin

User = get_user_model()

@register(User)
class CustomUserAdmin(ExtendedBaseUserAdmin):
    ...
```

```python
from django.contrib.admin import register
from django_addons.django_helper.admin.base import BaseAdmin


@register(SampleModel)
class SampleModelAdmin(BaseAdmin):
    ...
```

```python
from django.contrib.admin import register
from django_addons.django_helper.admin.base import BaseAdmin
from django_addons.django_helper.admin.mixins.change_readonly_fields import ChangeReadonlyFieldsMixin


@register(SampleModel)
class SampleModelAdmin(ChangeReadonlyFieldsMixin, BaseAdmin):
    readonly_fields = ('sample_field_one', 'sample_field_two')
    change_readonly_fields = ('sample_field_three',)
    ...
```

### Swagger

```python
from django.urls import include, path

urlpatterns = (
    ...,
    path('', include('django_addons.django_helper.swagger.urls')),
)
```

### Utils

```python
from django_addons.django_helper.utils.singleton_meta import SingletonMeta

class SampleClass(metaclass=SingletonMeta):
    ...
```

```python
from django_addons.django_helper.utils.module_tool import get_class_from_full_path, get_module_from_full_path

SampleClass = get_class_from_full_path('path.to.SampleClass')
sample_module = get_module_from_full_path('path.to.sample_module')
```

### DRF Settings

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'django_addons.django_helper.drf.responses.custom_json.CustomJSONRenderer',
        ...,
    ),
    'EXCEPTION_HANDLER': 'django_addons.django_helper.drf.exceptions.handler.custom_exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'django_addons.django_helper.drf.pagination.custom_page_number.CustomPageNumberPagination',
}
```

### DRF View

```python
from rest_framework.viewsets import GenericViewSet
from django_addons.django_helper.drf.mixins.ok_model import OKModelMixin

class SampleView(OKModelMixin, GenericViewSet):
    ...
```

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_addons.django_helper.drf.mixins.list_serializer import ListSerializerMixin

class SampleView(ListSerializerMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = SampleSerializer
    serializer_list_class = SampleListSerializer
    ...
```

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_addons.django_helper.drf.mixins.update_serializer import UpdateSerializerMixin

class SampleView(UpdateSerializerMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = SampleSerializer
    serializer_update_class = SampleUpdateSerializer
    ...
```

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_addons.django_helper.drf.mixins.multi_lookup_fields import MultiLookUpFieldsMixin

class SampleView(MultiLookUpFieldsMixin, mixins.RetrieveModelMixin, GenericViewSet):
    lookup_fields = ('sample_field_one', 'sample_field_two')
    ...
```

```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_addons.django_helper.drf.mixins.current_user import CurrentUserMixin

class SampleView(CurrentUserMixin, mixins.RetrieveModelMixin, GenericViewSet):  # Will accept `me` as `id` in the URL
    ...
```

### DRF Permission

```python
from rest_framework.viewsets import ModelViewSet
from django_addons.django_helper.drf.permissions.django_model_full_permissions import DjangoModelFullPermissions

class SampleView(ModelViewSet):
    permission_classes = (DjangoModelFullPermissions,)
    ...
```

## notification_helper

### Activate

```python
INSTALLED_APPS = [
    ...,
    django_addons.notification_helper.apps.NotificationHelperConfig,
]
```

## user_management

### Activate

```python
INSTALLED_APPS = [
    ...,
    django_addons.django_helper.apps.DjangoHelperConfig,
]
```

### Settings

```python
USER_MANAGEMENT = {
    'additional_fields': {
        'user': {}
    },
    'apis': {
        'user': {
            'login': {'is_active': True},
            'change_email': {'is_active': True},
            'change_password': {'is_active': True},
            'crud': {
                'is_active': True,
                'permission_classes': ['path.to.a.custom.PermissionClass'],
            },
            'search': {'is_active': True},
            'forgot_password': {'is_active': True},
            'invitation': {'is_active': True},
            'registration': {'is_active': True},
        },
        'group': {
            'crud': {'is_active': True},
            'assignment': {'is_active': True}
        },
        'permission': {
            'crud': {'is_active': True},
            'assignment': {'is_active': True}
        },
        'verification_code': {
            'crud': {'is_active': True}
        },
    },
    'email_data': {
        'invitation_acceptance_link': 'https://example.com/invitaion/accept/'
    },
}
```

## For Package Developers

### Quick Start

```shell
git clone <this repo>
cd django_addons

virtualenv -p python3.10 venv
source venv/bin/activate
./runner requirements.install.dev
```

### Available Commands

- `./runner git.pre_commit.init`
- `./runner git.pre_commit.run_for_all`
- `./runner requirements.compile`
