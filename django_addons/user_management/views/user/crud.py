from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.repositories.user.query import UserQueryRepository
from django_addons.user_management.serializers.user.crud import UserCRUDSerializer

User = get_user_model()


class UserCRUDView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    serializer_class = UserCRUDSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis['user']['crud']['permission_classes']

    def get_queryset(self):
        return UserQueryRepository.all()
