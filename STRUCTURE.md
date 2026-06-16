🧠 Why This Is Important

In a monolith:
Application
    ↓
Single log file

In microservices:
User Service
Order Service
Payment Service
Inventory Service
      ↓
Central Log Service

Without centralized logging, debugging becomes extremely difficult.

🛠 Tech Stack
Python
Flask
SQLAlchemy
SQLite
datetime

📂 Project Structure
distributed-logging-system/
│
├── app.py
├── logs.db
└── README.md
