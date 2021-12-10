from django.db import models
from authentication.models import UserProfile


class NoticeBoard(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    notice_url = models.URLField(null=True, blank=True)
    contacts = models.ManyToManyField(UserProfile, blank=True, related_name='notice_contact')
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " - " + self.description
