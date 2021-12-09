from datetime import date
from rest_framework import serializers
from .models import NoticeBoard


class NoticeBoardSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        data = self.validated_data
        notice = NoticeBoard.objects.create(
            name=data["name"],
            date=data["date"],
        )
        notice.description = data["description"]
        notice.link = data["link"]
        if data["ping"] == "true":
            notice.ping = True
        elif data["ping"] == "false":
            notice.ping = False
        notice.save()
        return notice

    class Meta:
        model = NoticeBoard
        fields = (
            "id",
            "name",
            "description",
            "date",
            "link",
            "ping",
            "upvote",
            "downvote",
        )
