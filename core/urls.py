from django.urls import path
from .views import (index, contact, signupPage,
                    ItemDetailView, home, loginPage, logoutPage)

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signupPage, name='signup'),
    path('contact/', contact, name='contact'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('password-reset', password_reset, name='password_reset'),
    # path('password-reset/done/', password_reset_done, name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]
