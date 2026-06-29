from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # positions
    path('positions/', views.browse_positions, name='positions'),
    path('positions/<int:pk>', views.position_detail, name='position_detail'),
    path('apply/<int:pk>', views.apply_position, name='apply_position'),
    
    # companies
    path('companies/', views.company_list, name='companies'),
    path('companies/<int:pk>', views.company_detail, name='company_detail'),
    
    # Student 
    
    path('profile/', views.student_profile, name='student_profile'),
    
    # Authentication
    path('register/', views.register, name='register'),   
    path('login/', views.user_login, name='login'),   
    path('logout/', views.user_logout, name='logout'),   
]