# MicroMentor: Mentor Booking System

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/anuj604/MICRO--MENTOR)

A full-stack web platform built with **Django** and **Bootstrap 5** that connects students with industry mentors based on technical skills and domain expertise.

---

## 🚀 Key Features

* **Role-Based Authentication & Onboarding**:
  * Distinct registration pathways for **Students** and **Mentors**.
  * Mentors provide primary skills, years of experience, expertise summary, and contact details during application.
  * Role-based automatic redirection to specialized dashboards upon login.
* **Smart Search & Discovery**:
  * Search mentors by **Username**, **Primary Skill**, or **Expertise** keywords using Django `Q` query filters.
  * Live availability badges (`Available` vs `Paused`).
* **Session Booking & Duplicate Prevention**:
  * Students can schedule sessions by picking a date and time slot.
  * Built-in validation prevents double-booking for the same mentor and time slot.
* **Booking Lifecycle & Status Tracking**:
  * Real-time status indicators: **Pending**, **Accepted**, **Rejected**, and **Cancelled**.
  * Students can cancel pending booking requests with one click.
* **1-on-1 Video Session Integration**:
  * Upon acceptance, an instant live video call room (`meet.jit.si`) and Google Meet shortcut are activated for both student and mentor.
* **Dynamic Mentor Availability Control**:
  * Mentors can toggle their booking availability on/off anytime from their dashboard to pause incoming requests.

---

## 🛠️ Tech Stack

* **Backend**: Python, Django
* **Database**: SQLite
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Video Meeting**: Jitsi Meet & Google Meet integration
* **Deployment Ready**: Gunicorn, WhiteNoise, Procfile

---

## 💻 Local Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd micromentor
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🌐 Deploying Live (Render / PythonAnywhere)

### Option 1: Render.com (Recommended Free Hosting)
1. Push this project to your GitHub repository.
2. Sign in to [Render.com](https://render.com) and click **New + > Web Service**.
3. Connect your GitHub repository.
4. Set the following settings:
   * **Runtime**: `Python 3`
   * **Build Command**: `pip install -r requirements.txt && python manage.py migrate`
   * **Start Command**: `gunicorn micromentor.wsgi:application`
5. Click **Create Web Service** — Render will build and deploy your project live with a free `onrender.com` URL!

### Option 2: PythonAnywhere.com
1. Create a free account on [PythonAnywhere.com](https://www.pythonanywhere.com/).
2. Open a Bash console and clone your repo: `git clone <repo-url>`.
3. Set up the virtual environment, install requirements, and configure the Web tab with the WSGI file.

---

## 👤 Author
Developed with ❤️ by **Anuj** (2026)
