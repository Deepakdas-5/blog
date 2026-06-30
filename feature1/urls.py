from django.urls import path
from .import views

urlpatterns = [
    path("",views.landing_page,name="welcome_page"),
    path("posts",views.post_list,name="post_list_page"),
    path("posts/<slug>",views.post_description,name="post_description_page")
]
