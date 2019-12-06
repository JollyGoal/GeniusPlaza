from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# from django.db.models.signals import pre_save


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Step(models.Model):
    step_text = models.TextField()
    recipe = models.ForeignKey('Recipe', related_name='recipe', on_delete=models.CASCADE)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.step_text

    class Meta:
        verbose_name = 'Step'
        verbose_name_plural = 'Steps'


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to=image_folder)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# def pre_save_posts_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(instance.title)
#         instance.slug = slug
#
#
# pre_save.connect(pre_save_posts_slug, sender=Recipe)
