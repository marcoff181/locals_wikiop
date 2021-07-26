from rest_framework import serializers

from .models import FixedSection, PrimarySection, ProjectExample,QuestionAndAnswer, SecondarySection


class ProjectExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectExample
        fields = ('name','text','image')

class PrimarySectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrimarySection
        fields = '__all__'


class SecondarySectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecondarySection
        fields = '__all__'
    

class FixedSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FixedSection
        fields = '__all__'


class QuestionAndAnswerSerializer(serializers.HyperlinkedModelSerializer):
    primary_section   = PrimarySectionSerializer(many=False)
    secondary_section = SecondarySectionSerializer(many=False,read_only=True)
    fixed_section     = FixedSectionSerializer(many=False,read_only=True)
    class Meta:
        model = QuestionAndAnswer
        #fields = ('primary_section','secondary_section','fixed_section','question','answer_text')
        fields = '__all__'


