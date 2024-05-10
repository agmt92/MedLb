from django.urls import path

from accounts.views import SignUpView

app_name='accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]