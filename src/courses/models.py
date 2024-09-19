from django.db import models
import helpers
from cloudinary.models import CloudinaryField
# Create your models here.
helpers.cloudinary_init()
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
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField(
        "image", 
        null=True, 
        # public_id_prefix=get_public_id_prefix,
        # display_name=get_display_name,
        # tags=["course", "thumbnail"]
    )
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
    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    @property
    def image_admin(self):
        if not self.image:
            return ''
        image_options = {
            "width" : 200
        }
        url = self.image.build_url(**image_options)
        return url
    def image_thumbnail(self, as_html=False, width=500):
        if not self.image:
            return ''
        image_options = {
            "width" : 200
        }
        if as_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # course_id 
    public_id = models.CharField(max_length=130, blank=True, null=True, db_index=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    preview = models.BooleanField(default=False,help_text="If user does not have access to course, can they see this?" )
    # thumbnail = CloudinaryField("image", 
    #             public_id_prefix=get_public_id_prefix,
    #             display_name=get_display_name,
    #             tags = ['thumbnail', 'lesson'],
    #             blank=True, null=True)

    video = CloudinaryField("video",null=True, blank=True,resource_type='video') 
    thumbnail = CloudinaryField("image", null=True, blank=True)
    
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
    )
    order = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order','-updated']
    