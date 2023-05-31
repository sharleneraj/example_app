"""exmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from list.views import home, PersonListView, PersonCreateView, PersonDetailView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('persons/', PersonListView.as_view(), name='person-list'),
    path('persons/create/', PersonCreateView.as_view(), name='person-create'),
    path('persons/detail/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('persons/update/<int:pk>/', PersonUpdateView.as_view(), name='person-update'),
    path('persons/delete/<int:pk>/', PersonDeleteView.as_view(), name='person-delete'),
]

