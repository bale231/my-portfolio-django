from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import path
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user
import json
from django.contrib import messages
from .models import Appointment

# Create your views here.

# View per la pagina di login
class LoginView(View):
    def get(self, request):
        return render(request, "portfolio/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        context = {"username_error": "", "password_error": "", "username_value": username}

        if not username:
            context["username_error"] = "Inserisci un username valido."
        if not password:
            context["password_error"] = "Inserisci una password."
        if user is None and username and password:
            context["password_error"] = "Username o password errati."

        if user is not None:
            login(request, user)
            return redirect("index")  # Redirect alla home se il login ha successo

        return render(request, "portfolio/login.html", context)


# View per il logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

# View per la home page
class IndexView(View):
    def get(self, request):
        context = {
            'js': 'script.js',
            'css': 'styles.css',
            'titolo': 'Il Mio Portfolio',
        }
        return render(request, 'portfolio/index.html', context)













# View per gestire gli appuntamenti senza DRF
class AppointmentView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        context = {
            'js': 'appointments.js',
            'css': 'appointments.css',
            'titolo': 'Appuntamenti',
            'appointments': appointments
            }
        return render(request, 'portfolio/appointments.html', context)

# View per gestire gli appuntamenti con DRF
class AppointmentViewMethod(View):
    def appointment_view(self, request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                print("Dati ricevuti:", data)  # Debug log
                
                # Verifica il tipo di dati ricevuti
                for key, value in data.items():
                    print(f"{key}: {value} (type: {type(value)})")
                
                # Recupera l'utente autenticato
                user = get_user(request)
                
                # Conversione dei dati con gestione degli errori
                try:
                    eta = int(data['eta']) if isinstance(data['eta'], str) else data['eta']
                    numero_stanza = int(data['numero_stanza']) if isinstance(data['numero_stanza'], str) else data['numero_stanza']
                    orario = datetime.strptime(data['orario'], "%H:%M").time()
                    print(f"Dati convertiti - Eta: {eta}, Numero Stanza: {numero_stanza}, Orario: {orario}")
                except ValueError as ve:
                    print(f"Errore di conversione: {ve}")
                    return JsonResponse({'error': f'Errore di conversione dei dati: {str(ve)}'}, status=400)
                
                appointment = Appointment.objects.create(
                    nome_paziente=data['nome_paziente'],
                    eta=eta,
                    tipologia_visita=data['tipologia_visita'],
                    diagnosi=data.get('diagnosi', ''),
                    orario=orario,
                    numero_stanza=numero_stanza,
                    dottore=user if user.is_authenticated else None
                )
                return JsonResponse({'message': 'Appuntamento creato con successo!', 'id': appointment.id}, status=201)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Formato JSON non valido'}, status=400)
            except KeyError as ke:
                return JsonResponse({'error': f'Manca il campo richiesto: {str(ke)}'}, status=400)
            except Exception as e:
                print(f"Errore generico: {e}")
                return JsonResponse({'error': f'Errore generico: {str(e)}'}, status=400)
        elif request.method == 'GET':
            appointments = list(Appointment.objects.values())
            return JsonResponse(appointments, safe=False)
        else:
            return JsonResponse({'error': 'Metodo non supportato'}, status=405)

# View per l'approvazione di un appuntamento
class ApproveAppointmentView(View):
    def approve_appointment(self, request, appointment_id):
        if request.method == "POST":
            appointment = get_object_or_404(Appointment, id=appointment_id)
            appointment.confermato = True  # Segna l'appuntamento come confermato
            appointment.save()
            return JsonResponse({"success": True, "message": "Appuntamento confermato!"})
        return JsonResponse({"success": False, "error": "Metodo non consentito"}, status=405)

# View per la cancellazione di un appuntamento
class DeleteAppointmentView(View):
    def delete_appointment(self, request, appointment_id):
        if request.method == "DELETE":
            appointment = get_object_or_404(Appointment, id=appointment_id)
            appointment.delete()
            return JsonResponse({"success": True, "message": "Appuntamento eliminato!"})
        return JsonResponse({"success": False, "error": "Metodo non consentito"}, status=405)
    
# View per la ista di appuntamenti
class AppointmentsListView(View):
    def appointments_list(request):
        appointments = Appointment.objects.all()
        return render(request, "portfolio/appointments.html", {"appointments": appointments})
