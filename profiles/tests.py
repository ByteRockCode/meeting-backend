from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Profile


class ProfileTestCase(TestCase):
    fixtures = [
        'users',
        'companies',
        'profiles',
    ]

    def test_cant_exist_duplicated_profile_for_a_user(self):
        profile = Profile.objects.get(id=1)
        user = profile.user
        company = profile.company

        try:
            with transaction.atomic():
                Profile.objects.create(company=company, user=user)

        except IntegrityError as e:
            pass

        profiles = Profile.objects.filter(company=company, user=user)
        message = 'The second profile with same comapy and user was created, but it shuld not'
        assert profiles.count() == 1, message

    def test_profile_to_string(self):
        profile = Profile.objects.get(id=1)

        assert isinstance(profile.__str__(), str), 'String is expected'
