from rest_framework import serializers

from .models import Settings


class SettingSerializer(serializers.Serializer):
    sid = serializers.IntegerField(label="配置ID")
    value = serializers.CharField(label="配置值")

    def create(self, validated_data):
        sid = validated_data.get("sid", "")
        value = validated_data.get("value", "")
        Settings.objects.filter(pk=sid).update(value=value)
        return validated_data

    def validate_sid(self, sid):
        exists = Settings.objects.filter(pk=sid).exists()
        if not exists:
            raise serializers.ValidationError(f"设置ID不存在")
        return sid

    def validate_value(self, value):
        try:
            int_value = int(value)
            # 如果能成功转换为整数，并且你有特别的处理需求，可以在这里做
            # 例如，返回整数而不是字符串
            return int_value
        except ValueError:
            # 如果转换失败，假设它是有效的字符串，直接返回
            return value
