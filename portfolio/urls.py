from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('home/', views.IndexView.as_view(), name='index'),
    path('appointments_page/', views.AppointmentView.as_view(), name='appointments_page'),
    path('api/appointments/', views.AppointmentViewMethod.as_view(), name='appointment_api'),
    path('appointments/', views.AppointmentsListView.as_view(), name='appointments_list'),  # ✅ Aggiunto il percorso per la tabella
    path("api/appointments/<int:appointment_id>/approve/", views.ApproveAppointmentView.as_view(), name="approve_appointment"),
    path("api/appointments/<int:appointment_id>/delete/", views.DeleteAppointmentView.as_view(), name="delete_appointment"),
]