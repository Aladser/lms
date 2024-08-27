from config.settings import USERS_GROUP_NAME


class OwnerQuerysetMixin:
    def get_queryset(self):
        if self.request.user.groups.filter(name=USERS_GROUP_NAME).exists():
            return super().get_queryset().filter(owner=self.request.user)
        else:
            return super().get_queryset()
