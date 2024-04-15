from django.urls import path , include
from .views import SignUpView, MyLoginView, admin_dashboard, regular_user_dashboard

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('regular_user/dashboard/', regular_user_dashboard, name='regular_user_dashboard'),
    path('accounts/', include('allauth.urls')),
]
