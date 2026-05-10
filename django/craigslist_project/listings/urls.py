from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.all_listings,
        name='all_listings'
    ),

    path(
        'listing/<int:id>/',
        views.listing_detail,
        name='listing_detail'
    ),

    path(
        'newlisting/',
        views.new_listing,
        name='new_listing'
    ),

    path(
        'edit/<int:id>/',
        views.edit_listing,
        name='edit_listing'
    ),

    path(
        'delete/<int:id>/',
        views.delete_listing,
        name='delete_listing'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]