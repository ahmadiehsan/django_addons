from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.views.group.assignment import GroupAssignmentView
from django_addons.user_management.views.group.crud import GroupCRUDView
from django_addons.user_management.views.permission.assignment import PermissionAssignmentView
from django_addons.user_management.views.permission.crud import PermissionCRUDView
from django_addons.user_management.views.user.change_email import UserChangeEmailView
from django_addons.user_management.views.user.change_email_verify import UserChangeEmailVerifyView
from django_addons.user_management.views.user.change_password import UserChangePasswordView
from django_addons.user_management.views.user.crud import UserCRUDView
from django_addons.user_management.views.user.forgot_password import UserForgotPasswordView
from django_addons.user_management.views.user.forgot_password_verify import UserForgotPasswordVerifyView
from django_addons.user_management.views.user.invitation import UserInvitationView
from django_addons.user_management.views.user.invitation_verify import UserInvitationVerifyView
from django_addons.user_management.views.user.registration import UserRegistrationView
from django_addons.user_management.views.user.registration_verify import UserRegistrationVerifyView
from django_addons.user_management.views.user.search import UserSearchView
from django_addons.user_management.views.verification_code.crud import VerificationCodeCRUDView

_API_ROUTER = DefaultRouter()

if USER_MANAGEMENT_OPTIONS.apis["user"]["change_email"]["is_active"]:
    _API_ROUTER.register("api/v1/change-email/verify", UserChangeEmailVerifyView, basename="user_change_email_verify")
    _API_ROUTER.register("api/v1/change-email", UserChangeEmailView, basename="user_change_email")

if USER_MANAGEMENT_OPTIONS.apis["user"]["change_password"]["is_active"]:
    _API_ROUTER.register("api/v1/change-password", UserChangePasswordView, basename="user_change_password")

if USER_MANAGEMENT_OPTIONS.apis["user"]["search"]["is_active"]:
    _API_ROUTER.register("api/v1/users/search", UserSearchView, basename="users_search")

if USER_MANAGEMENT_OPTIONS.apis["user"]["crud"]["is_active"]:
    _API_ROUTER.register("api/v1/users", UserCRUDView, basename="users")

if USER_MANAGEMENT_OPTIONS.apis["user"]["forgot_password"]["is_active"]:
    _API_ROUTER.register("api/v1/forgot-password", UserForgotPasswordView, basename="user_forgot_password")
    _API_ROUTER.register(
        "api/v1/forgot-password/verify", UserForgotPasswordVerifyView, basename="user_forgot_password_verify"
    )

if USER_MANAGEMENT_OPTIONS.apis["user"]["invitation"]["is_active"]:
    _API_ROUTER.register("api/v1/invitation/verify", UserInvitationVerifyView, basename="user_invitation_verify")
    _API_ROUTER.register("api/v1/invitation", UserInvitationView, basename="user_invitation")

if USER_MANAGEMENT_OPTIONS.apis["user"]["registration"]["is_active"]:
    _API_ROUTER.register("api/v1/registration/verify", UserRegistrationVerifyView, basename="user_registration_verify")
    _API_ROUTER.register("api/v1/registration", UserRegistrationView, basename="user_registration")

if USER_MANAGEMENT_OPTIONS.apis["group"]["assignment"]["is_active"]:
    _API_ROUTER.register("api/v1/groups/assignment-to-user", GroupAssignmentView, basename="groups_assignment_to_user")

if USER_MANAGEMENT_OPTIONS.apis["group"]["crud"]["is_active"]:
    _API_ROUTER.register("api/v1/groups", GroupCRUDView, basename="groups")

if USER_MANAGEMENT_OPTIONS.apis["permission"]["assignment"]["is_active"]:
    _API_ROUTER.register(
        "api/v1/permissions/assignment-to-user", PermissionAssignmentView, basename="permissions_assignment_to_user"
    )

if USER_MANAGEMENT_OPTIONS.apis["permission"]["crud"]["is_active"]:
    _API_ROUTER.register("api/v1/permissions", PermissionCRUDView, basename="permissions")

if USER_MANAGEMENT_OPTIONS.apis["verification_code"]["crud"]["is_active"]:
    _API_ROUTER.register("api/v1/verification-codes", VerificationCodeCRUDView, basename="verification_codes")

urlpatterns = (path("", include(_API_ROUTER.urls)),)

if USER_MANAGEMENT_OPTIONS.apis["user"]["login"]["is_active"]:
    urlpatterns += (
        path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
        path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    )
