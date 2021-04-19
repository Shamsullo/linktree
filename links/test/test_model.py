from django.test import TestCase
from django.db import IntegrityError
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from ..models import LinkBoard, SocialMedia

User = get_user_model()


class LinkBoardTest(TestCase):
    """
    Class to test BoardLink model. I am writing just a couple of test to show
    my unit testing skills
    """
    phone_number = '+996012345678'
    password = '0990poop'
    public_link = 'my_links_board_link'

    def setUp(self):
        User.objects.create(phone_number=self.phone_number, password=self.password)
        board = LinkBoard.objects.first()
        board.public_link = self.public_link
        board.save(update_fields=('public_link',))
        SocialMedia.objects.create(board=board, whatsapp=self.phone_number)

    def test_signal_creation(self):
        created = LinkBoard.objects.filter(
            user__phone_number=self.phone_number).exists()
        self.assertEqual(created, True)

    def test_public_link_label(self):
        board = LinkBoard.objects.first()
        field_label = board._meta.get_field('public_link').verbose_name
        self.assertEqual(field_label, _('Address to the links board'))

    def test_public_link_value(self):
        board = LinkBoard.objects.get(user__phone_number=self.phone_number)
        value = board.public_link
        self.assertEqual(value, self.public_link)

        user = User.objects.create(phone_number='+996987654321',
                                   password='somePas123')
        board = LinkBoard.objects.get(user=user)
        with self.assertRaises(IntegrityError):
            board.public_link = self.public_link
            board.save(update_fields=('public_link',))

    def test_none_value_field(self):
        board = LinkBoard.objects.get(user__phone_number=self.phone_number)
        title = board.title
        self.assertEqual(title, None)

    def test_whatsapp_number(self):
        whatsapp = SocialMedia.objects.get(
            board__user__phone_number=self.phone_number).whatsapp
        self.assertEqual(whatsapp, self.phone_number)

    def test_get_absolute_url(self):
        board = LinkBoard.objects.get(id=1)
        user_id = board.user.id
        absolute_url = reverse('add-or-update-board-data', args=[user_id])
        self.assertEqual(board.get_absolute_url(), absolute_url)
