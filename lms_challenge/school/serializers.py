from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'identification', 'school']
        extra_kwargs = {
            'identification': {'read_only': True},
        }

    def create(self,data):
        """check for max students before assigning a school to student"""
        if 'school' in data:
            school = data['school']
            if len(school.students.all()) >= school.max_students:
                raise serializers.ValidationError('Maximum number of student reached')
        student = Student.objects.create( **data)
        return student
    
    def update(self, instance, data):
        """check for max students before assigning a school to student in update"""
        if 'school' in data:
            school= data['school']
            if len(school.students.all()) >= school.max_students:
                raise serializers.ValidationError('Maximum number of student reached')
        return instance

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'max_students']
