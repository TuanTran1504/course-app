from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from cloudinary import CloudinaryImage
from .models import Course, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = [
        'updated'
    ]
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    list_filter = ['status', 'access']
    readonly_fields = ['display_image']
    list_display = ['title', 'status', 'access']
    def display_image(self, obj, *args, **kwargs):
        # url = helpers.get_cloudinary_image_object(
        #     obj, 
        #     field_name='image',
        #     width=200
        # )
        url = obj.image_admin
        return format_html(f"<img src={url} />")
    
    display_image.short_description = "Current Image"
# admin.site.register(Course)
