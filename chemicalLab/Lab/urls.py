from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.render_login, name="render_login"),
    path('auth_user/', views.login, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("analysis/", views.analysis, name="analysis"),
    path("view_schedule/", views.schedule, name="view_schedule"),
    path("get_historic_data/<int:id>",
         views.get_historic_data, name="historic_data"),
    path("get_schedule_details", views.get_schedule_details,
         name="get_schedule_details"),
    path("get_scheduled_data", views.get_scheduled_data, name="get_scheduled_data"),
    path("get_sensor_data", views.get_sensor_data, name="get_sensor_data"),
    path("email", views.email, name='email'),
    path("notifications", views.check_notifications_working, name="notifications")
]
