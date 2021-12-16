from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from .models import NoticeBoard
from authentication.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "name", "email", "phone_number", "photo_url")


class NoticeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeBoard
        fields = "__all__"


class NoticeCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        request = self.context["request"]
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        print(profile.get_notice_privileges())
        if profile.get_notice_privileges():
            raise PermissionDenied("You are not authorized to create notices")
        return attrs

    def save(self, **kwargs):
        data = self.validated_data
        # pylint: disable=no-member
        noticeBoard = NoticeBoard.objects.create(
            title=data["title"],
            description=data.get("description", ""),
            date=data["date"],
            upvote=data.get("upvote", 0),
            downvote=data.get("downvote", 0),
        )
        noticeBoard.contact.set(data.get("contact", []))
        # By default, add the creator of the workshop as the contact for the workshop
        noticeBoard.contact.add(
            UserProfile.objects.get(user=self.context["request"].user)
        )
        # FirebaseAPI.send_club_message(data, self.context['club'])
        return noticeBoard

    class Meta:
        model = NoticeBoard
        fields = "__all__"