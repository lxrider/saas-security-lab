from django.test import TestCase
from django.urls import reverse

from identity.models import Organization, User
from .models import Contact


class ContactTenantIsolationTests(TestCase):
    def setUp(self):
        self.org_a = Organization.objects.create(
            name="Organization A",
            slug="org-a",
        )
        self.org_b = Organization.objects.create(
            name="Organization B",
            slug="org-b",
        )

        self.alice = User.objects.create_user(
            username="alice",
            password="alice-test-password",
            organization=self.org_a,
        )

        self.contact_b = Contact.objects.create(
            organization=self.org_b,
            first_name="Bob",
            last_name="Contact",
            email="contact-b@example.test",
        )

    def test_user_cannot_access_contact_from_another_organization(self):
        self.client.login(
            username="alice",
            password="alice-test-password",
        )

        response = self.client.get(
            reverse("contact-detail", args=[self.contact_b.pk])
        )

        self.assertEqual(response.status_code, 404)