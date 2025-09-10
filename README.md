# WorkStream: Realtime Activity Dashboard

A **multi-user, real-time activity tracking dashboard** built with **Django + Django REST Framework + Channels (WebSockets)**.  
Users can sign up, log in, and track activities in real-time with secure authentication.

---

## 🚀 Features
- User authentication (Signup, Login, Logout) with token-based auth
- Activity tracking (CRUD) per user
- Real-time updates via **Django Channels + WebSockets**
- Secure multi-user setup (each user sees only their own activities)
- Frontend templates for Signup, Login, Dashboard
- CSRF-safe API handling
- Clean separation of `accounts` and `activity` apps

---

## 🛠 Tech Stack
- **Backend**: Django 5, Django REST Framework, Django Channels
- **Frontend**: HTML, JS (vanilla)
- **Database**: SQLite (default, can switch to Postgres)
- **Realtime**: Channels + Redis
- **Auth**: TokenAuthentication

---

## 📂 Project Structure
