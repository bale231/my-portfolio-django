from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('home/', views.index, name='index'),
    path('appointments_page/', views.AppointmentView.as_view(), name='appointments_page'),
    path('api/appointments/', views.appointment_view, name='appointment_api'),
    path('appointments/', views.appointments_list, name='appointments_list'),  # ✅ Aggiunto il percorso per la tabella
    path("api/appointments/<int:appointment_id>/approve/", views.approve_appointment, name="approve_appointment"),
    path("api/appointments/<int:appointment_id>/delete/", views.delete_appointment, name="delete_appointment"),
]