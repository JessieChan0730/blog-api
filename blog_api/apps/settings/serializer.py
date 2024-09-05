from rest_framework import serializers

from .models import Settings, FrontCover, AdminLogo


class SettingSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="配置ID")
    value = serializers.CharField(label="配置值",allow_blank=True)

    def create(self, validated_data):
        id = validated_data.get("id", "")
        value = validated_data.get("value", "")
        Settings.objects.filter(pk=id).update(value=value)
        return validated_data

    def validate_id(self, id):
        exists = Settings.objects.filter(pk=id).exists()
        if not exists:
            raise serializers.ValidationError(f"设置ID不存在")
        return id

    def validate_value(self, value):
        try:
            int_value = int(value)
            # 如果能成功转换为整数，并且你有特别的处理需求，可以在这里做
            # 例如，返回整数而不是字符串
            return int_value
        except ValueError:
            # 如果转换失败，假设它是有效的字符串，直接返回
            return value


class FrontCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontCover
        fields = ['cover']


class AdminLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLogo
        fields = ['logo']
