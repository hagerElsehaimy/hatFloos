from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('<int:id>', views.get_user_info),
    path('register', views.register, name='register'),
    path('<int:id>', views.view_profile, name='view_profile'),
    # path(r'^profile/(?P<id>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    path('edit/<int:id>', views.edit_profile, name='edit_profile'),
    path('delete/<int:id>', views.delete_account),
    path('test/test', views.top_rated, name='top_rated')
    # path(r'<int:id>/edit/', views.edit_profile, name='edit_profile'),
]
