from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class LinkBoard(models.Model):
    """
    Board that have user information and his/her links that need to be shared.
    """
    user = models.OneToOneField(User, verbose_name=_('Owner of the links'),
                                related_name='links', on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name=_("Avatar"), blank=True, null=True,
                               upload_to='photos/avatars/')
    title = models.CharField(verbose_name=_('Board title'), max_length=80,
                             blank=True, null=True)
    bio = models.TextField(verbose_name=_('Your board description'),
                           blank=True, null=True)
    public_link = models.SlugField(verbose_name=_('Address to the links board'),
                                   max_length=100, blank=True, null=True,
                                   unique=True)
    links_title = models.CharField(verbose_name=_('Title for above the links'),
                                   max_length=80, blank=True, null=True)

    class Meta:
        verbose_name = _("Links Board")
        verbose_name_plural = _("Links Boards")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('add-or-update-board-data', kwargs={'pk': self.user.pk})


class SocialMedia(models.Model):
    """For social medias that have a clear way go get the link to them"""
    whatsapp = models.CharField(verbose_name=_('WhatsApp'), max_length=20,
                                blank=True, null=True)
    telegram = models.CharField(verbose_name=_('Telegram ID'), max_length=100,
                                blank=True, null=True)
    board = models.OneToOneField(LinkBoard, on_delete=models.CASCADE,
                                 related_name='social_links')


class Link(models.Model):
    """
    If user want to add some other links to board, this table wil store them.
    """
    link = models.CharField(verbose_name=_('Link that need to be shared'),
                            max_length=200)
    name = models.CharField(verbose_name=_('Site name'), max_length=50)
    board = models.ForeignKey(LinkBoard, on_delete=models.CASCADE,
                              related_name='link')

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_link_board(sender, instance, created, **kwargs):
    if created:
        LinkBoard.objects.create(user=instance)
