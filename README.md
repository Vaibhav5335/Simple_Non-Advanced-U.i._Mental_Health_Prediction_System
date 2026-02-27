# 🧠 Simple Mental Health Prediction System (Basic UI Version)

### Lightweight Machine Learning Web App with Minimal UI

---

## 📌 Overview

The **Simple Mental Health Prediction System** is a **lightweight and beginner-friendly web application** that predicts mental health conditions using a machine learning model.

This version focuses on:

* 🧩 Simplicity in design
* ⚡ Faster performance
* 🧠 Core ML functionality
* 🎯 Clean and minimal user interface

It is ideal for demonstrating **fundamentals of ML integration with web apps** without complex UI/UX layers.

---

## 🚀 Key Features

### 🧠 Prediction System

* Machine learning-based predictions
* Simple input form
* Instant result display

### 🎯 Minimal UI

* Clean and distraction-free design
* Basic HTML templates
* Easy navigation

### ⚡ Lightweight Architecture

* Faster load time
* Minimal dependencies
* Easy to understand for beginners

---

## 🏗️ Project Structure

```id="p7kx9c"
Simple-Non-Adv-UI-MentalHealthPrediction/
│
├── prediction/              # Core app
│   ├── views.py             # Handles logic & predictions
│   ├── models.py            # Database models (if used)
│   ├── urls.py              # Routing
│
├── templates/               # HTML templates
├── static/                  # CSS (basic styling)
│
├── train_model.py           # ML training script
├── manage.py                # Django entry point
├── db.sqlite3               # Database
```

---

## 🧠 Machine Learning Workflow

### ⚙️ Model Training

The system uses a trained ML model created using:

* **Pandas** → Data preprocessing
* **NumPy** → Data handling
* **Joblib / Pickle** → Model serialization

### 🔄 Prediction Flow

1. User enters input data
2. Data is passed to backend
3. Model processes the input
4. Prediction is generated
5. Result is displayed instantly

---

## 🖥️ Tech Stack

### 🌐 Frontend

* HTML
* Basic CSS

### ⚙️ Backend

* Python
* Django Framework

### 🤖 Machine Learning

* Pandas
* NumPy
* Scikit-learn / Joblib

### 🗄️ Database

* SQLite (optional usage)

---

## 🔄 Application Flow

1. User opens homepage
2. Enters required mental health parameters
3. Submits form
4. Backend processes request
5. Prediction result is shown

---

## 📂 Core Files Explained

### 📌 `views.py`

* Handles form input
* Loads ML model
* Returns prediction results

### 📌 `train_model.py`

* Trains the ML model
* Saves model for reuse

### 📌 `templates/`

* Contains basic UI pages
* Displays forms and results

---

## 🎨 UI Highlights

* Minimalist interface
* No complex styling
* Beginner-friendly structure
* Focus on functionality over design

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository

```bash id="f2k9sd"
git clone https://github.com/your-username/simple-mental-health-prediction.git
cd simple-mental-health-prediction
```

### 2️⃣ Create Virtual Environment

```bash id="v0l3pd"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash id="d8u2qp"
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash id="k91nqe"
python manage.py migrate
```

### 5️⃣ Train Model (if required)

```bash id="h7c5rb"
python train_model.py
```

### 6️⃣ Run Server

```bash id="n4y8mx"
python manage.py runserver
```

### 7️⃣ Open in Browser

```id="r3j9zt"
http://127.0.0.1:8000/
```

---

## 📊 Use Case

This project is best suited for:

* 🎓 Beginners learning Django + ML
* 🧠 Understanding ML deployment basics
* 💼 Portfolio demonstration (entry-level)
* 🧪 Testing ML models quickly

---

## 🌟 Highlights

✔ Beginner-friendly project
✔ Simple and clean structure
✔ Focus on core ML logic
✔ Easy to modify and extend

---

## 🧩 Future Improvements

* 🎨 Improve UI/UX design
* 🔐 Add authentication system
* 📊 Store prediction history
* 🌐 Deploy on cloud platforms
* 📱 Make responsive design

---

## 👨‍💻 Author

**Vaibhav Sharma**

* Aspiring Full Stack & ML Developer
* Built this project as a learning milestone

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Final Note

This project proves that even a **simple UI + strong logic** can create impactful applications.

A perfect stepping stone toward advanced full-stack ML systems 🚀

---
