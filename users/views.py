from django.views.generic import CreateView, FormView
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect

from .forms import CustomUserCreationForm

User = get_user_model()

class SignUpFormView(CreateView):
    '''
    This view takes data from request andcreates a new User
    '''
    model = User
    success_url = '/'
    form_class = CustomUserCreationForm
    template_name = 'users/sign_up.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')


def already_exist(request):
    if request.is_ajax and request.method == "GET":
        phone_number = request.GET.get('phoneNumber', None)
        # the is some extra code in the begining of number passed
        phone_number = list(phone_number)
        phone_number.pop(0)
        phone_number = ''.join(phone_number)
        data = {
            'is_taken': User.objects.filter(phone_number=phone_number).exists()
        }
        return JsonResponse(data)  
