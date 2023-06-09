from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .form import LoginForm,MyPasswordChangeForm



urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.show_cart,name='checkout'),
     path('order/',views.order_placed,name='order'),


    #LOGIN AUTHENTICATIONS---
    path("registration/",views.CustomerRegistrationview.as_view(),name="customerregistration"), 
    path("accounts/login/",auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name='app/Changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name="passwordchange"),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name="passwordchangedone"),
    path("logout/",auth_view.LogoutView.as_view(next_page='login'),name='logout'),


    

   

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

