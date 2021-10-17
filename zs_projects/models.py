from django.db import models
import os

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"




class Projects(models.Model):
    title=models.CharField(max_length=150)
    developer=models.CharField(max_length=150 , default='Zahra Safdari')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title