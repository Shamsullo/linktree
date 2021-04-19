from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import SocialMedia, LinkBoard


class LinksBoardUpdateForm(forms.ModelForm):
    """
    As we have board created by signal, we need to add or update board content.
    This form for this purposes
    """
    def save(self, commit=True):
        try:
            board = LinkBoard.objects.get(user__id=self.kwargs['pk'])
        except LinkBoard.DoesNotExist:
            raise ValidationError(_('Board has not been found'))
        update_fields = []

        if self.cleaned_data['avatar']:
            board.avatar = self.cleaned_data['avatar']
            update_fields.append('avatar')
        if self.cleaned_data['title']:
            board.title = self.cleaned_data['title']
            update_fields.append('title')
        if self.cleaned_data['bio']:
            board.bio = self.cleaned_data['bio']
            update_fields.append('bio')
        if self.cleaned_data['public_link']:
            board.public_link = self.cleaned_data['public_link']
            update_fields.append('public_link')
        if self.cleaned_data['links_title']:
            board.links_title = self.cleaned_data['links_title']
            update_fields.append('links_title')

        # TODO: Attemp to get gid or if-else statements
        # cleaned_data = self.cleaned_data
        # for data in cleaned_data.keys():
        #     if cleaned_data[data]:
        #         field = str(data)
        #         board. = self.cleaned_data[field]
        #         update_fields.append(str(data))

        return board.save(update_fields=update_fields)

    class Meta:
        model = LinkBoard
        fields = ('avatar', 'title', 'bio', 'public_link', 'links_title')


class SocialMediaLinksForm(forms.ModelForm):
    """Form for getting social media data and validating them."""

    class Meta:
        model = SocialMedia
        fields = ('whatsapp', 'telegram')
