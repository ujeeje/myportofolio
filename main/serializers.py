
from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import CTFWriteup


class CTFWriteupSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = CTFWriteup
        fields = [
            "id",
            "title",
            "description",
            "writeup_url",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = [
            "id",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_description(self, value):
        if value is None:
            return value
        return strip_tags(value)

    def validate(self, attrs):
        if self.instance is not None and not self.partial:
            required_fields = [
                "title",
                "description",
                "writeup_url",
            ]

            for field in required_fields:
                if field not in attrs:
                    raise serializers.ValidationError({
                        field: "This field is required."
                    })

        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(pk=request.user.pk).exists()

    def get_starred_by_names(self, obj):
        return list(
            obj.starred_by.values_list("username", flat=True)
        )
