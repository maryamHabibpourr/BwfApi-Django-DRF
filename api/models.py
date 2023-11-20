from django.db import models
from django.contrib.auth.models import User
import uuid

"""
for user profile
"""
def upload_path_handler(instance, filename):
    return "avatars/{id}/{file}".format(id=instance.user.id, file=filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    bio = models.CharField(max_length=256, blank=True, null=True)


"""
for group model
"""
class Group(models.Model):
    name = models.CharField(max_length=32, null=False, unique=False)
    location = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=256, null=False, unique=False)

    class Meta:
        unique_together = (('name', 'location'))

    def num_members(self):
        return Member.objects.filter(group=self).count()


    def __str__(self):
        return self.name

"""
 for Event model
"""
class Event(models.Model):
    team1 = models.CharField(max_length=32, blank=False)
    team2 = models.CharField(max_length=32, blank=False)
    time = models.DateTimeField(null=False, blank=False)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.team1
    
    def __str__(self):
        return self.team2

"""
for memeber
"""
class Member(models.Model):
    group = models.ForeignKey(Group, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='members_of', on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'group'),)
        index_together = (('user', 'group'),)


"""
for comments
"""
class Comment(models.Model):
    group = models.ForeignKey(Group, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    description = models.CharField(max_length=256, null=False, unique=False)
    time = models.DateTimeField(auto_now_add=True)
   

"""
for bet
"""
class Bet(models.Model):
    user = models.ForeignKey(User, related_name='user_bets', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='bets', on_delete=models.CASCADE)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(default=None, null=True, blank=True)

    class Meta:
        unique_together = (('user', 'event'),)
        index_together = (('user', 'event'),)