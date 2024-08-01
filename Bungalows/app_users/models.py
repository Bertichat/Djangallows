from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


import os
import uuid


# class User(AbstractUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     is_company = models.BooleanField('company status', default=False)
#     is_companyuser = models.BooleanField('companyuser status', default=False)
#     is_client = models.BooleanField('client status', default=False)

#     class Meta:
#         db_table = "User"

    # objects = UserManager()

    # def get_absolute_url(self):
    #     return "/users/%i/" % (self.pk)
    
    # def save(self, *args, **kwargs):
    #     if os.path.isdir(str(root_media)+"/Company/user_{0}".format(self.id)) == False:
    #         os.makedirs(str(root_media)+"/Company/user_{0}".format(self.id), exist_ok=True)
    #         os.makedirs(str(root_media)+"/Company/user_{0}/pts".format(self.id), exist_ok=True)
    #         os.makedirs(str(root_media)+"/Company/user_{0}/ptc".format(self.id), exist_ok=True)
    #         os.makedirs(str(root_media)+"/Company/user_{0}/papers".format(self.id), exist_ok=True)
            # self.weights_dir = "user_{0}/MyFolder/{1}".format(self.id, self.username)
            # add creating directory code here

        # super(AbstractUser, self).save(*args, **kwargs)
