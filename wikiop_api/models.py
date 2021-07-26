from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from cities_light.models import City


class PrimarySection(models.Model): 
    name        = models.CharField(max_length= 50,unique=True)
    description = models.CharField(max_length= 400,null=True,blank=True)

    def __str__(self): 
        return self.name


class SecondarySection(models.Model): 
    primary_section = models.ForeignKey(
        PrimarySection,
        on_delete    = models.SET_NULL,
        null         = True,
        related_name = "secondary_section"
    )
    name = models.CharField(max_length= 50)
    
    def __str__(self): 
        return self.name


class FixedSection(models.Model): 
    name        = models.CharField(max_length= 50,unique=True)
    description = models.CharField(max_length= 400,null=True,blank=True)

    def __str__(self): 
        return self.name


class QuestionAndAnswer(models.Model): 
    primary_section   = models.ForeignKey(PrimarySection,on_delete=models.SET_NULL,null=True,related_name="question",help_text="main sections/themes of the website (AGUA, AMBIENTE ...)")
    secondary_section = ChainedForeignKey(
        SecondarySection,
        chained_field       = "primary_section",
        chained_model_field = "primary_section",
        show_all            = False,
        auto_choose         = True,
        sort                = True,
        related_name        = "question",
        help_text           = "secondary sections/themes for each primary section"
    )
    fixed_section               = models.ForeignKey(FixedSection,on_delete=models.SET_NULL,null=True,)
    question                    = models.TextField()
    answer_file                 = models.FileField(null=True,blank=True,help_text="image or video to answer the question (optional)")
    answer_text                 = MarkdownField(
        rendered_field='answer_text_rendered', 
        validator=VALIDATOR_STANDARD,
        help_text="the full answer to the question asked, possible to add links",
        blank          = True,
        null           = True)
    answer_text_rendered        = RenderedMarkdownField()
    relevant_documents          = MarkdownField(
        rendered_field='relevant_documents_rendered', 
        validator=VALIDATOR_STANDARD,
        help_text="relevant documents with important information to answer this question",
        blank          = True,
        null           = True)
    relevant_documents_rendered = RenderedMarkdownField()
    other_sources               = MarkdownField(
        rendered_field = 'other_sources_rendered',
        validator      = VALIDATOR_STANDARD,
        help_text      = "other sources about the current theme",
        blank          = True,
        null           = True)
    other_sources_rendered = RenderedMarkdownField()
    warning_text           = models.TextField(max_length=2000, blank=True, help_text="the text shown in red at the end of the answer section (optional)")


    def __str__(self): 
        return self.question

class ProjectExample(models.Model): 
    theme = models.ForeignKey(PrimarySection,on_delete=models.SET_NULL,null=True,related_name="project_example",help_text="main sections/primarysections of the website (AGUA, AMBIENTE ...)")
    intention = models.CharField(max_length = 200)
    description  = models.CharField(max_length = 200)
    city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,related_name = "project_example")
    budget = models.DecimalField(decimal_places=2,max_digits=20)
    year = models.IntegerField(validators=[
            MaxValueValidator(9999),
            MinValueValidator(1800)
        ])
    image = models.ImageField(blank = True,null = True)
    link = models.URLField()
    def __str__(self): 
        return self.description


