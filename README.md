# 🧠 Simple Mental Health Prediction System (Basic UI Version)  
### *A Lightweight ML-Powered Web Application with Minimal UI*

The **Simple Mental Health Prediction System** is a beginner-friendly Django web application that integrates a machine learning model to predict mental health conditions. Designed with simplicity and performance in mind, this project focuses on **core ML functionality and clean architecture**, making it an ideal starting point for learning ML deployment.

With a minimal UI and fast response time, this system demonstrates how machine learning models can be seamlessly integrated into web applications without unnecessary complexity.

---

<p align="center">
  <strong>⚡ Mental Health Predictor</strong><br/>
  <em>Simple Interface • Smart Predictions • Fast Performance</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Django-Web%20Framework-green?style=flat-square&logo=django"/>
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/UI-Minimal-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Application Flow](#-application-flow)
- [Core Modules](#-core-modules)
- [UI Design](#-ui-design)
- [Getting Started](#-getting-started)
- [Use Cases](#-use-cases)
- [Future Improvements](#-future-improvements)
- [Project Structure](#-project-structure)

---

## 🌟 Overview

This project is a **lightweight full-stack ML web app** built using Django, aimed at demonstrating the fundamentals of **machine learning integration into web systems**.

It focuses on:

- 🧠 Core prediction logic  
- ⚡ Fast and lightweight performance  
- 🎯 Minimal UI for clarity  
- 🧩 Beginner-friendly architecture  

Unlike complex ML systems, this project strips away unnecessary layers and highlights the **essential workflow of ML deployment**.

---

## ✨ Key Features

| Feature | Description |
|--------|------------|
| 🧠 **ML Prediction Engine** | Uses a trained model to predict mental health conditions |
| 🎯 **Minimal UI** | Clean HTML interface with no distractions |
| ⚡ **Lightweight System** | Fast loading and minimal dependencies |
| 🔄 **Instant Results** | Real-time prediction display |
| 🧩 **Beginner Friendly** | Easy-to-understand code structure |

---

## 🛠 Technology Stack

| Layer | Technology | Purpose |
|------|-----------|--------|
| **Frontend** | HTML, CSS | Simple UI rendering |
| **Backend** | Python, Django | Server logic and request handling |
| **Machine Learning** | Pandas, NumPy, Scikit-learn | Model training and prediction |
| **Model Storage** | Joblib / Pickle | Model serialization |
| **Database** | SQLite (optional) | Data storage |

---

## 🏗 Architecture

The application follows a **simple Django MVC structure**:

```
User Input → Django View → ML Model → Prediction → UI Display
```

### Layers:

1. **Frontend Layer** → HTML forms for user input  
2. **Backend Layer** → Django views process requests  
3. **ML Layer** → Model generates predictions  
4. **Output Layer** → Results displayed to user  

---

## 🧠 Machine Learning Workflow

### ⚙️ Model Training

The model is trained using:

- **Pandas** → Data preprocessing  
- **NumPy** → Data handling  
- **Scikit-learn** → Model training  
- **Joblib/Pickle** → Saving trained model  

---

### 🔄 Prediction Flow

```
1. User inputs data
2. Data sent to backend
3. Model processes input
4. Prediction generated
5. Result displayed instantly
```

---

## 🔄 Application Flow

1. User opens the web application  
2. Inputs mental health-related parameters  
3. Submits the form  
4. Backend processes data using ML model  
5. Prediction result is shown  

---

## 📦 Core Modules

### 📌 `views.py`
- Handles user input  
- Loads trained ML model  
- Returns prediction results  

---

### 📌 `train_model.py`
- Trains machine learning model  
- Saves model for reuse  

---

### 📌 `templates/`
- Contains HTML UI  
- Displays forms and results  

---

## 🎨 UI Design

- Minimalist layout  
- Clean and simple forms  
- No heavy styling  
- Focus on usability and functionality  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x  
- Django  

---

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/simple-mental-health-prediction.git
cd simple-mental-health-prediction
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Train Model (if required)
```bash
python train_model.py
```

### 6️⃣ Run Server
```bash
python manage.py runserver
```

### 7️⃣ Open in Browser
```
http://127.0.0.1:8000/
```

---

## 🎯 Use Cases

- 🎓 Learning Django + Machine Learning integration  
- 🧠 Understanding ML deployment basics  
- 💼 Entry-level portfolio project  
- 🧪 Quick ML model testing  

---

## 🌟 Highlights

✔ Beginner-friendly implementation  
✔ Lightweight and fast system  
✔ Focus on core ML concepts  
✔ Easy to extend and customize  
✔ Clean and modular structure  

---

## 🔮 Future Improvements

- 🎨 Enhanced UI/UX design  
- 🔐 Authentication system  
- 📊 Store prediction history  
- ☁ Cloud deployment  
- 📱 Responsive design  

---

## 📁 Project Structure

```
Simple-Non-Adv-UI-MentalHealthPrediction/
│
├── prediction/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│
├── templates/
├── static/
│
├── train_model.py
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 👨‍💻 Author

**Vaibhav Sharma**  
*Aspiring Full Stack & ML Developer*

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

> Even a **simple UI combined with powerful logic** can create meaningful applications.

This project is a perfect stepping stone toward building **advanced full-stack ML systems 🚀**

---

<p align="center">
  Built with ❤️ using Django & Machine Learning<br/>
  <strong>Mental Health Predictor</strong> — Simple Yet Powerful
</p>
