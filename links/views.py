from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, FormView

from .forms import SocialMediaLinksForm, LinksBoardUpdateForm
from .models import SocialMedia, LinkBoard


class LinksBoardUpdateViw(LoginRequiredMixin, UpdateView):
    template_name = 'pages/index.html'
    form_class = LinksBoardUpdateForm
    context_object_name = 'board'

    def get_object(self):
        board = LinkBoard.objects.get(user__id=self.kwargs['pk'])
        return board

    def get_context_data(self, **kwargs):
        context = super(LinksBoardUpdateViw, self).get_context_data()
        context['form_social'] = SocialMediaLinksForm
        context['social_media'] = SocialMedia.objects.first()
        return context

    def form_valid(self, form):
        form.kwargs = self.kwargs
        form.save()
        return HttpResponseRedirect(self.request.user.links.get_absolute_url())


class SocialMediaView(LoginRequiredMixin, FormView):
    """View for creating or updating social media"""
    form_class = SocialMediaLinksForm
    http_method_name = ('POST',)

    def form_valid(self, form):
        board = self.request.user.links
        try:
            obj = SocialMedia.objects.first()
            obj.whatsapp = form.cleaned_data['whatsapp']
            obj.telegram = form.cleaned_data['telegram']
            obj.save(update_fields=('whatsapp', 'telegram'))
        except SocialMedia.DoesNotExist():
            SocialMedia.objects.create(
                board=board,
                whatsapp=form.cleaned_data['whatsapp'],
                telegram=form.cleaned_data['telegram']
            )
        return HttpResponseRedirect(board.get_absolute_url())
