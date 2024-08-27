from rest_framework import serializers

from .models import FriendLink


class FriendLinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, label='网站名字', allow_blank=False)
    intro = serializers.CharField(max_length=120, label='网站简介', allow_blank=False)
    link = serializers.URLField(label='网站链接')
    avatar = serializers.URLField(label='网站头像')
    email = serializers.EmailField(label='邮箱')

    status = serializers.CharField(required=False, label='链接状态')

    def validate_email(self, value):
        if self.instance:
            if value.lower() == self.instance.email.lower():
                return value
        query_set = FriendLink.objects.all()
        if self.instance:
            query_set = query_set.exclude(id=self.instance.id)
        if query_set.filter(email__iexact=value).exists():
            raise serializers.ValidationError("邮箱已经被注册了，换一个邮箱吧")
        return value

    def create(self, validated_data):
        # 抛出 status字段
        status = validated_data.get('status', '')
        if status or status != '':
            validated_data.pop('status')
        friend_link = FriendLink.objects.create(**validated_data)
        return friend_link

    def update(self, instance, validated_data):

        for field in self.fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
        instance.save()
        return instance


# TODO 抽取到公共APP中
class DeleteMultiple(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(), required=True, allow_empty=False, min_length=1)
