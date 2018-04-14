from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Agreement(models.Model):
    meeting = models.ForeignKey('Meeting', related_name='agreements', on_delete=models.DO_NOTHING)

    description = models.TextField()

    def __str__(self):
        return f'Se acuerda {self.description} en {self.meeting}'


class Compromise(models.Model):
    meeting = models.ForeignKey(
        'Meeting',
        null=True,
        related_name='compromises',
        on_delete=models.DO_NOTHING,
    )

    company = models.ForeignKey(
        'companies.Company',
        related_name='compromises',
        on_delete=models.DO_NOTHING,
    )

    description = models.TextField()

    def __str__(self):
        return f'{self.company} se compromente a {self.description} en {self.meeting}'


class Guest(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.DO_NOTHING)
    profile = models.ForeignKey('profiles.Profile', on_delete=models.DO_NOTHING)

    creator = models.BooleanField(default=False, validators=[])

    class Meta:
        unique_together = ('meeting', 'profile')
        verbose_name_plural = 'guests'

    def __str__(self):
        relation = 'creo' if self.creator else 'fue invitado a'

        return f'{self.profile}, y {relation} {self.meeting}'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Guest, self).save(*args, **kwargs)

    def validate_unique(self, *args, **kwargs):
        super(Guest, self).validate_unique(*args, **kwargs)

        queryset = Guest.objects.exclude(id=self.id).filter(meeting=self.meeting_id, creator=True)

        if self.creator and queryset.exists():
            raise ValidationError('Already exist a guest as creator for this meeting')


class Meeting(models.Model):
    guests = models.ManyToManyField(
        'profiles.Profile',
        through='Guest',
        through_fields=('meeting', 'profile'),
    )

    companies = models.ManyToManyField(
        'companies.Company',
        # related_name='meetings',
    )

    motive = models.CharField(max_length=255)

    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField()
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        from_date = self.from_datetime.date()
        from_time = self.from_datetime.time()

        return f'{self.motive}, el {from_date} a las {from_time}'

    def get_absolute_url(self):
        return reverse('meetings__detail', args=[self.id])
