from rest_framework import serializers
from server.models.program import Program
from server.models.lesson import Lesson



class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id',
            'thumbnail',
            'title',
            'slug',
            'duration_in_days',
            'description',
            'price',
            'is_free',
            'start_date'
        ]


class ProgramDetailSerializer(serializers.ModelSerializer):
    included_programs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Program
        fields = [
            'id',
            'thumbnail',
            'intro',
            'title',
            'slug',
            'description',
            'syllabus',
            'duration_in_days',
            'description',
            'price',
            'is_free',
            'start_date',
            'included_programs'
        ]

    def get_included_programs(self, obj):
        queryset = obj.parent_programs.filter(is_active=True)
        serializer = ProgramDetailSerializer(queryset, many=True)
        return serializer.data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'sl',
            'title',
            'description',
            'is_complete',
            'resource',
            'assignment',
            'video_src'
        ]