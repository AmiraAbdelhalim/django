from rest_framework import serializers
from .models import Student, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    track = TrackSerializer(read_only=True)
    track_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = ("id", "student_name", "student_age", "Student_reg_date", "track", "track_id")

