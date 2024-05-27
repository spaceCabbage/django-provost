from django.db import models
from django.contrib.auth.models import Permission

"""
This module contains the base models for the provost app. These models are
abstract and should be inherited by the actual models in the app.

These have been mostly stolen from django-guardian, all the commented out code is
from the original django-guardian implementation. ignore that for now.

everything raises NotImplementedError becasue we havent implemented it yet.
"""


class BaseObjectPermission(models.Model):
    """
    Abstract ObjectPermission class. Actual class should additionally define
    a ``content_object`` field and either ``user`` or ``group`` field.
    """

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        raise NotImplementedError


class BaseGenericObjectPermission(models.Model):
    # TODO Implement base generic object permission model

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_pk = models.CharField(_('object ID'), max_length=255)
    # content_object = GenericForeignKey(fk_field='object_pk')

    class Meta:
        abstract = True
        # indexes = [
        #     models.Index(fields=['content_type', 'object_pk']),
        # ]


class UserObjectPermissionBase(BaseObjectPermission):
    # TODO Implement user object permission base model
    """
    **Manager**: :manager:`UserObjectPermissionManager`
    """

    # user = models.ForeignKey(user_model_label, on_delete=models.CASCADE)
    # objects = UserObjectPermissionManager()

    class Meta:
        abstract = True
        # unique_together = ['user', 'permission', 'content_object']


class UserObjectPermissionAbstract(
    UserObjectPermissionBase, BaseGenericObjectPermission
):
    # TODO Implement user object permission abstract model
    class Meta(UserObjectPermissionBase.Meta, BaseGenericObjectPermission.Meta):
        abstract = True
        # unique_together = ['user', 'permission', 'object_pk']


class UserObjectPermission(UserObjectPermissionAbstract):
    # TODO Implement user object permission model
    class Meta(UserObjectPermissionAbstract.Meta):
        abstract = True


class GroupObjectPermissionBase(BaseObjectPermission):
    # TODO Implement group object permission base model
    """
    **Manager**: :manager:`GroupObjectPermissionManager`
    """

    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # objects = GroupObjectPermissionManager()

    class Meta:
        abstract = True
        # unique_together = ['group', 'permission', 'content_object']


class GroupObjectPermissionAbstract(
    GroupObjectPermissionBase, BaseGenericObjectPermission
):
    # TODO Implement group object permission abstract model
    class Meta(GroupObjectPermissionBase.Meta, BaseGenericObjectPermission.Meta):
        abstract = True
        # unique_together = ['group', 'permission', 'object_pk']


class GroupObjectPermission(GroupObjectPermissionAbstract):
    # TODO Implement group object permission model
    class Meta(GroupObjectPermissionAbstract.Meta):
        abstract = True
