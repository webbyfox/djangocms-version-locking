from djangocms_versioning.admin import VersioningAdminMixin
from djangocms_versioning.models import Version

from .helpers import content_is_unlocked


class VersionLockAdminMixin(VersioningAdminMixin):
    """
    Mixin providing versioning functionality to admin classes of
    version models.
    """

    def has_change_permission(self, request, content_obj=None):
        """
        If there’s a lock for edited object and if that lock belongs
        to the current user
        """

        # User has permissions?
        has_permission = super().has_change_permission(request, content_obj)
        if not has_permission:
            return False

        # Check if the lock exists and belongs to the user
        return content_is_unlocked(content_obj, request.user)
