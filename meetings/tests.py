from django.contrib.admin.sites import AdminSite
from django.core.exceptions import ValidationError
from django.test import TestCase

from companies.models import Company
from profiles.models import Profile

from .admin import MeetingAdmin
from .models import Agreement
from .models import Compromise
from .models import Guest
from .models import Meeting


class AgreementTestCase(TestCase):
    fixtures = [
        'users',
        'companies',
        'meetings',
    ]

    def test_agreement_to_string(self):
        meeting = Meeting.objects.get(id=1)
        description = 'Lorem ipsum'

        agreement = Agreement.objects.create(meeting=meeting, description=description)
        agreement_like_string = agreement.__str__()

        self.assertEqual(type(agreement_like_string), str)
        assert description in agreement_like_string
        assert meeting.motive in agreement_like_string


class CompromiseTestCase(TestCase):
    fixtures = [
        'users',
        'companies',
        'profiles',
        'meetings',
    ]

    def test_compromise_to_string(self):
        company = Company.objects.get(id=1)
        meeting = Meeting.objects.get(id=4)

        description = 'Lorem ipsum'

        compromise = Compromise.objects.create(
            company=company,
            meeting=meeting,
            description=description,
        )

        compromise_like_string = compromise.__str__()

        self.assertEqual(type(compromise_like_string), str)
        assert description in compromise_like_string
        assert company.name in compromise_like_string
        assert meeting.motive in compromise_like_string

    def test_responsable_company_is_on_meeting(self):
        meeting = Meeting.objects.get(id=1)

        Guest.objects.bulk_create(
            [Guest(profile=profile, meeting=meeting) for profile in Profile.objects.all()],
        )

        # TODO


class GuestTestCase(TestCase):
    fixtures = [
        'users',
        'companies',
        'profiles',
        'meetings',
        'guests',
    ]

    def test_guest_to_string(self):
        guest = Guest.objects.get(id=1)
        guest_like_string = guest.__str__()

        self.assertEqual(type(guest_like_string), str)
        assert guest.meeting.motive in guest_like_string
        assert guest.profile.__str__() in guest_like_string

    def test_multiple_guests_of_a_meeting(self):
        meeting = Meeting.objects.get(id=1)

        Guest.objects.bulk_create(
            [Guest(profile=profile, meeting=meeting) for profile in Profile.objects.all()],
        )

    def test_cant_exist_multiple_guests_as_creators(self):
        profile_1 = Profile.objects.get(id=1)
        profile_2 = Profile.objects.get(id=2)

        meeting = Meeting.objects.get(id=1)

        Guest.objects.create(profile=profile_1, meeting=meeting, creator=True)

        try:
            Guest.objects.create(profile=profile_2, meeting=meeting, creator=True)

        except ValidationError as e:
            pass

        creator_guests = Guest.objects.filter(meeting=meeting, creator=True)

        message = 'The second guest as creator of a meeting was created, but it should not'
        assert creator_guests.count() == 1, message

    def test_cant_exist_duplicated_guest_in_a_meeting(self):
        profile = Profile.objects.get(id=1)
        meeting = Meeting.objects.get(id=1)

        Guest.objects.create(profile=profile, meeting=meeting)

        try:
            Guest.objects.create(profile=profile, meeting=meeting)

        except ValidationError as e:
            pass

        guests = Guest.objects.filter(profile=profile, meeting=meeting)
        message = 'A meeting as a duplicated guest, but it should not'
        assert guests.count() == 1, message


class MeetingAdminTestCase(TestCase):
    fixtures = [
        'users',
        'companies',
        'meetings',
    ]

    def setUp(self):
        self.request = object()
        self.site = AdminSite()

        self.meeting_admin = MeetingAdmin(Meeting, self.site)

    def test_get_companies_names(self):

        meeting_1 = Meeting.objects.get(id=1)
        companies_names_1 = self.meeting_admin.get_companies_names(meeting_1)
        self.assertEqual(companies_names_1, '')

        meeting_2 = Meeting.objects.get(id=2)
        companies_names_2 = self.meeting_admin.get_companies_names(meeting_2)
        self.assertEqual(companies_names_2, 'Tecnored')

        meeting_3 = Meeting.objects.get(id=3)
        companies_names_3 = self.meeting_admin.get_companies_names(meeting_3)
        self.assertEqual(companies_names_3, 'Pérez & Asociados y Tecnored')

        meeting_4 = Meeting.objects.get(id=4)
        companies_names_4 = self.meeting_admin.get_companies_names(meeting_4)
        self.assertEqual(companies_names_4, 'CompuMundoHiperMegaRed, Pérez & Asociados y Tecnored')
