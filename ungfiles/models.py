# from django.db import models

# from django.db.models.signals import pre_save, post_delete
# from django.utils.text import slugify
# from django.conf import settings
# from django.dispatch import receiver
# from ckeditor.fields import RichTextField
# from django.utils import timezone


# def upload_location(instance, filename):
#     file_path = 'tender/files/{title}-{filename}'.format(
#         title=str(instance.title), filename=filename
#     )
#     return file_path


# class Category(models.Model):
#     name = models.CharField(max_length=150)

#     def __str__(self):
#         return self.name


# class SubCategories(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
#     subcategory = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.subcategory


# class UploadedFile(models.Model):
#     title = models.CharField(max_length=250)
#     sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='sub_category_name')
#     # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
#     body = RichTextField(blank=True, null=True)
#     ung_file = models.FileField(upload_to=upload_location, null=False, blank=False)
#     # date_published = models.DateTimeField(auto_now_add=True,)
#     # date_updated = models.DateTimeField(auto_now=True, verbose_name="date_updated")

#     def __str__(self):
#         return self.title
