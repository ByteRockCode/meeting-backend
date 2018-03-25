from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Company


User = get_user_model()


class CompanyTestCase(TestCase):
    fixtures = [
        'users',
    ]

    def test_slugify_name(self):
        owner = User.objects.first()
        name = 'Mi Super Compañía!'
        slug = 'mi-super-compania'

        company = Company.objects.create(name=name, owner=owner)

        assert company.name == name
        assert company.slug == slug
