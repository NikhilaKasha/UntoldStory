from django.db import models
from django.utils import timezone

class Profile(models.Model):
    Profile_id = models.CharField(max_length= 20, null = False, default='DEFAULT VALUE')
    Profile_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, null= True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Profile_name)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

class Interest(models.Model):
    Profile_name = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='interests')
    Interest_category = models.CharField(primary_key='TRUE', max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Profile_name)

    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interest'


class Story(models.Model):
    Profile_name = models.ForeignKey('Profile', on_delete=models.CASCADE, default='True', related_name='Story')
    title = models.CharField(max_length=100)
    p_description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Profile_name)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Story'


class Saved(models.Model):
    Profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.Profile_id)

    class Meta:
        verbose_name = 'Saved'
        verbose_name_plural = 'Saved'


class ReadLater(models.Model):

    Profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.Profile_id)

    class Meta:
        verbose_name = 'ReadLater'
        verbose_name_plural = 'ReadLater'