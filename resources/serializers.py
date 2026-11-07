
from rest_framework import serializers
from .models import Course, Resource


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Course title cannot be empty."
            )
        return value

    def validate_course_code(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Course code cannot be empty."
            )
        return value


class ResourceSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all()
    )
    
    class Meta:
        model = Resource
        fields = [
            'id',
            'title',
            'description',
            'resource_type',
            'course',
        ]
