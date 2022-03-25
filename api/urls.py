from django.urls import path
from .views.users import SignUp, SignIn, ChangePassword, SignOut

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),

]