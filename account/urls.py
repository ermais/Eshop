from django.urls import path
from .views import user_profile_update

urlpatterns = [
    path('update/',user_profile_update,name="update_user_profile"),
]
