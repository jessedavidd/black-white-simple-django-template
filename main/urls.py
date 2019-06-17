from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Entries page
    path('entries/', views.entries, name='entries'),

    # Full entry page
    path('entries/<int:entry_id>/', views.entry, name='entry'),

    # Categories page
    path('categories/', views.categories, name='categories'),

    # Entris under category
    path('categories/<int:category_id>/', views.category, name='category'),
]
