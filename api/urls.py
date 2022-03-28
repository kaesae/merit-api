from django.urls import path
from .views.users import SignUp, SignIn, ChangePassword, SignOut
from .views.posts import PostsView, PostView

urlpatterns = [
    #### Post Route
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    #### Post Route
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    #### Update Route
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    #### Delete Route
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    #### Get and Post route
    path('post/', PostsView.as_view(), name='post'),
    #### Get route
    path('posts/<int:pk>', PostView.as_view(), name='posts'),
]