from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from djangocms_versioning.admin import VersioningAdminMixin

from .models import VersionLock


class VersionLockAdminMixin(VersioningAdminMixin):
    """
    Mixin providing versioning functionality to admin classes of
    version models.
    """
    def save_model(self, request, obj, form, change):
        """
        Overrides the save method to create a version lock on the
        version object when a content object is created
        """
        super().save_model(request, obj, form, change)

    """
    TODO: Implement permissions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    """

class VersionLockingAdmin(admin.ModelAdmin):
    """
    Admin class used for version locked models.
    """
    list_display = (
        'nr',
        'created',
        'created_by',
        'locked',
        'state',
        'state_actions',
    )

    def locked(self, obj):
        return obj.id
    locked.short_description = _('version locked')
