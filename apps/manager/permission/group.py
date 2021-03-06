from rest_framework.permissions import BasePermission

__all__ = [
    "GroupAPIRequiredMixin", "GroupListRequiredMixin", "GroupCreateRequiredMixin",
    "GroupUpdateRequiredMixin", "GroupDetailRequiredMixin", "GroupDeleteRequiredMixin"
]


class GroupAPIRequiredMixin(BasePermission):

    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list=list(request.user.get_all_permissions())
        print(perm_list)
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class GroupListRequiredMixin(GroupAPIRequiredMixin):
    permission_required = u'manager.yo_list_group'


class GroupCreateRequiredMixin(GroupAPIRequiredMixin):
    permission_required = u'manager.yo_create_group'


class GroupUpdateRequiredMixin(GroupAPIRequiredMixin):
    permission_required = u'manager.yo_update_group'


class GroupDetailRequiredMixin(GroupAPIRequiredMixin):
    permission_required = u'manager.yo_detail_group'


class GroupDeleteRequiredMixin(GroupAPIRequiredMixin):
    permission_required = u'manager.yo_delete_group'
