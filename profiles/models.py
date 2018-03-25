from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    company = models.ForeignKey(
        'companies.Company',
        null=True,
        related_name='team',
        on_delete=models.DO_NOTHING,
    )

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='profiles',
    )

    email = models.EmailField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'company')
        verbose_name_plural = 'profiles'

    def __str__(self):
        identifer = self.user.__str__() if self.user else self.email
        return f'{identifer} es parte de {self.company}'
