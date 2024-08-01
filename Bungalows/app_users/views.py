from django.shortcuts import render
from allauth.account.views import LoginView,LogoutView
from app_users.forms import loginBisForm

from allauth.utils import get_request_param
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def Welcome(request):
    return render(request, 'app_users/welcome.html')

class LoginViewBis(LoginView):
    template_name = 'app_users/loginBis.html'
    form_class = loginBisForm
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        ret = super(LoginView, self).get_context_data(**kwargs)
        return ret

Login = LoginViewBis.as_view()

class LogoutViewBis(LogoutView):
    template_name = 'app_users/logoutBis.html'
    redirect_field_name = 'next'

Logout = LogoutViewBis.as_view()