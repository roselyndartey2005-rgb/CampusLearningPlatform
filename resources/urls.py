
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course-list'),
    path('courses/<int:pk>/',views.course_detail, name='course-detail'),
    path('courses/create/', views.course_create,name='course-create'),
    path('courses/<int:pk>/update/', views.course_update, name='course-update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course-delete'),
    path('resources/', views.resource_list, name='resource-list'),
    path('resources/<int:pk>/', views.resource_detail, name='resource-detail'),
    path('resources/create/', views.resource_create, name='resource-create'),
    path('resources/<int:pk>/update/', views.resource_update, name='resource-update'),
    path('resources/<int:pk>/delete/', views.resource_delete, name='resource-delete'),
    path('courses/<int:pk>/resources/', views.course_resources, name='course-resources'),
    path('courses/resource-counts/', views.course_resource_counts, name='course-resource-counts'),
    

]

