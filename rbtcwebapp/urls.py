from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path("service/", views.service_single, name="service_single"),
    path('about/', views.about, name='about'),
    path('members/', views.members, name='members'),
    path("team/", views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('events/', views.events, name='events'),
    path('achievements/', views.achievements, name='achievements'),
    path('gallery/', views.gallery, name='gallery'),
    path('inventory_02/menu/', views.inventory_menu, name='inventory_menu'),
    path('contact/', views.contact, name='contact'),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallary, name="gallery"),
    # invetoery event project
    path("landing/", views.landing, name="landing"),
    path("events/", views.event, name="event"),
    path("projects/", views.projects, name="projects"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('protect/', views.protect, name="protect"),
    path('shipping/', views.ship, name="ship"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('ngo/', views.ngo, name="ngo"),
    path('policy/', views.policy, name="policy"),
    path('profile/', views.user_profile, name='user_profile'),
    path('inventory/issue/', views.issue_component, name='issue_component'),
    # path('inventory/manage-requests/', views.manage_request, name='manage_requests'),
    path('inventory/my-issued-components/', views.my_issued_components, name='my_issued_components'),
    path('inventory/components/', views.components, name='components'),
    path('inventory/issue/<int:component_id>/', views.issue_component, name='issue_component'),
] 
