from django.urls import path

from simplelogin.users.myviews import list_allusers, login_view
from simplelogin.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"

my_urlpatterns = [path("all/", view=list_allusers, name="list"), path("login/", view=login_view, name="login")]

urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]

urlpatterns += my_urlpatterns
