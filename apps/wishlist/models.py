from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if not postData['first_name'].isalpha():
            errors['first_name'] = 'First name contains non-alpha characters.'
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name should be at least 3 characters.'
        if len(postData['user_name']) < 3:
            errors['user_name'] = 'User name should be at least 3 characters.'
        if not postData['user_name'].isalpha():
            errors['user_name'] = 'User name contains non-alpha characters.'
        # if not re.match(EMAIL_REGEX, postData['email']):
        #     errors['email'] = 'Email is not valid.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match.'
        if User.objects.filter(user_name = postData['user_name']):
            errors['user_name'] = 'User Name already exists.'
 
        return errors

    def itemValidator(self,postData):
        errors = {}
        if len(postData['item_name']) < 4:
            errors['item_name'] = 'Item should be at least 4 characters.'
        return errors














class User(models.Model): #has to be capitals
    first_name = models.CharField(max_length=255)
    user_name = models.TextField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now = True)
    password = models.CharField(max_length=255)
    hireDate = models.CharField(max_length=255)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} | {}>".format(self.first_name,self.user_name)

class Item(models.Model): #has to be capitals
    item = models.TextField(max_length=1000)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, related_name = 'creates')
    liked_by = models.ManyToManyField(User, related_name="likes")

    def __repr__(self):
        return "<Secret object: {} | {} | {}>".format(self.item,self.created_by,self.liked_by)
