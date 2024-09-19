from django.db import models

# Create your models here.

class PublishStatus(models.TextChoices):
    ANYONE = "any" , 'Anyone'
    EMAIL_REQUIRED = "email_required", "Email required"
    

class AccessRequirement(models.TextChoices):
    PUBLISHED = "pub" , 'Published'
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image
    access = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.DRAFT
    )
    status = models.CharField(
        max_length=10,
        choices= PublishStatus.choices,
        default = PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED