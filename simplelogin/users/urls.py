from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from simplelogin.users.myviews import list_allusers, login_view
from simplelogin.users.rest_views import get_all_users, register_user
from simplelogin.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"

my_urlpatterns = [
    path("all/", view=list_allusers, name="list"),
    path("login/", view=login_view, name="login"),
]

rest_url_patterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("all_users/", view=get_all_users, name="get_all_users"),
    path("register_user/", view=register_user, name="register_user"),
]

urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]

urlpatterns += my_urlpatterns + rest_url_patterns
