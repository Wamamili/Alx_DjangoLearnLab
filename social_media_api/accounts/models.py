# User model for the social media API
# This model extends the AbstractUser to include additional fieldsS

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    
    followers = models.ManyToManyField(
        "self",
        through="UserFollower",
        through_fields=("user", "follower"),
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def follow(self, user):
        if user != self:
            UserFollower.objects.get_or_create(user=user, follower=self)

    def unfollow(self, user):
        if user != self:
            UserFollower.objects.filter(user=user, follower=self).delete()

    def is_following(self, user):
        return UserFollower.objects.filter(user=user, follower=self).exists()

    def __str__(self):
        return self.username


class UserFollower(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_followers",
        on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        User,
        related_name="user_following",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "follower") 

    def __str__(self):
        return f"{self.follower} follows {self.user}"
