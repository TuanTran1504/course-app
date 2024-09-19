from django.db import models

# Create your models here.

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub" , 'Published'
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

class AccessRequirement(models.TextChoices):
    ANYONE = "any" , 'Anyone'
    EMAIL_REQUIRED = "email", "Email required"
 
    

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    # image = CloudinaryField(
    #     "image", 
    #     null=True, 
    #     public_id_prefix=get_public_id_prefix,
    #     display_name=get_display_name,
    #     tags=["course", "thumbnail"]
    # )
    access = models.CharField(
        max_length=5,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10,
        choices= PublishStatus.choices,
        default = PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED