from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.django_helper.drf.mixins.multi_lookup_fields import MultiLookUpFieldsMixin
from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.repositories.user.query import UserQueryRepository
from django_addons.user_management.serializers.user.minimal import UserMinimalSerializer

User = get_user_model()


class UserSearchView(MultiLookUpFieldsMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserMinimalSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["user"]["search"]["permission_classes"]

    lookup_fields = ("username", "email")
    lookup_value_regex = r"[^/]+"  # for accepting email address as a lookup field

    def get_queryset(self):
        return UserQueryRepository.all_except_inactive_ones()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                MultiLookUpFieldsMixin.lookup_url_kwarg,
                location=OpenApiParameter.PATH,
                description=f"Send `{'` or `'.join(lookup_fields)}`",
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
