from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class BaseManager(models.Manager):
    '''
    a class for defining the functions for the inheritance models
    '''

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_all(self):
        return super().get_queryset()


class BaseModel(models.Model):
    '''
        a class for modifying all the objects in the project
        '''
    objects = BaseManager()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        '''
        override default delete function,instead of deleting from the database it will change its condition to is_deleted
        '''
        self.is_deleted = True
        self.save()

    def undeleted(self):
        '''
        it will change the object  condition to not deleted
        '''

        self.is_deleted = False
        self.save()

    def activate(self):
        '''
        it will change the object  condition to active
        '''
        self.is_active = True
        self.save()

    def deactivate(self):
        '''
        it will change the object  condition to deactive
        '''
        self.is_active = False
        self.save()

    def done(self):
        '''
        it will change the object  condition to done
        '''
        self.is_done = True
        self.save()

#
# class MyUserManager(UserManager):
#     '''
#     this class overrides the default UserManager model to put the user's phone number instead of username when creating a new user
#     '''
#
#     def create_user(self, phone_number, email=None, password=None, **extra_fields):
#         '''
#         replace the user's username with its phone number'
#         '''
#         extra_fields.pop('username')
#         username = phone_number
#         return super().create_user(username, email, password, **extra_fields)
#
#     def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
#         extra_fields.pop('username')
#         username = phone_number
#         return super().create_superuser(username, email, password, **extra_fields)
#
#
class User(AbstractUser):
    '''
    override the default User class and put the phone number instead of username
    '''
    #
    # phone_number = models.CharField(max_length=11, unique=True)
    # objects = MyUserManager()
    #
    # def save(self, *args, **kwargs):
    #     self.username = self.phone_number
    #     super().save(*args, **kwargs)
