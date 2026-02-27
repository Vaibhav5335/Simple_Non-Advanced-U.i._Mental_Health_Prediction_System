from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import joblib
import numpy as np
import os

# Load ML model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "app", "health_model.pkl")

with open(model_path, "rb") as f:
    model = joblib.load(f)

# If you also have a scaler, load it here
# scaler_path = os.path.join(BASE_DIR, "app", "scaler.pkl")
# with open(scaler_path, "rb") as f:
#     scalar = joblib.load(f)

def welcome(req):
    return render(req, "welcome.html")

def login(req):
    return render(req, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        from .models import candidate   # make sure candidate model exists
        if candidate.objects.filter(username=username).exists():
            userstatus = 1
        else:
            user = candidate()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.name = request.POST.get('name')
            user.save()
            userstatus = 2
    else:
        userstatus = 3
    return render(request, 'register.html', {'userstatus': userstatus})

def home(req):
    return render(req, 'home.html')

def ml(req):
    return render(req, "ml.html")

def ml_page(request):
    return render(request, "ml.html")

def result(request):
    if request.method == "POST":
        try:
            # Input values
            gender = int(request.POST.get("gender", 0))
            depressed = int(request.POST.get("depressed", 0))
            pleasure = int(request.POST.get("pleasure", 0))
            sleep = int(request.POST.get("sleep", 0))
            tired = int(request.POST.get("tired", 0))
            meal = int(request.POST.get("meal", 0))
            bad = int(request.POST.get("bad", 0))
            concentration = int(request.POST.get("concentration", 0))
            restless = int(request.POST.get("restless", 0))
            hurt = int(request.POST.get("hurt", 0))
            family = int(request.POST.get("family", 0))
            job = int(request.POST.get("job", 0))
            study_hour = int(request.POST.get("study_hour", 0))
            eg_hour = int(request.POST.get("eg_hour", 0))
            sm_hour = int(request.POST.get("sm_hour", 0))
            ex_hour = int(request.POST.get("ex_hour", 0))
            alcohol = int(request.POST.get("alcohol", 0))
            percentage = float(request.POST.get("percentage", 0))
            education = request.POST.get("education", "graduate")

            # Education encoding
            if education == "school":
                edu_vec = [0, 1, 0]
            elif education == "postgraduate":
                edu_vec = [1, 0, 0]
            else:  # graduate default
                edu_vec = [0, 0, 1]

            # Final feature list
            data = [
                gender, depressed, pleasure, sleep, tired, meal, bad,
                concentration, restless, hurt, family, job,
                study_hour, eg_hour, sm_hour, ex_hour,
                alcohol, percentage
            ] + edu_vec

            # If scaler exists, transform
            # data = scalar.transform([data])
            # Else, just pass raw data
            prediction = model.predict([data])[0]

            return render(request, "result.html", {"prediction": prediction})

        except Exception as e:
            return render(request, "result.html", {"error": str(e)})
    else:
        return render(request, "ml.html")