from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class Company(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='companies_that_i_own',
        on_delete=models.CASCADE,
    )

    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    website = models.URLField(blank=True, null=True)

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['owner']),
        ]
        unique_together = (
            ('owner', 'slug'),
            ('owner', 'slug'),
        )
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        max_length = Company._meta.get_field('slug').max_length

        self.slug = slugify(self.name)[:max_length]

        return super(Company, self).save(*args, **kwargs)
