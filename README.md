# DriverSafetyManagementSystem
Driver Safety Management System is a web-based application that monitors driving behavior and enhances road safety through real-time tracking and analytics.  It includes features like driver performance scoring, incident detection, and an admin dashboard for managing and analyzing driver data.  
🚗 Driver Safety Management System

📌 Overview

The Driver Safety Management System is an AI-based project designed to enhance road safety by detecting unsafe driving behaviors in real time. The system identifies drowsiness, alcohol consumption, and mobile phone usage while driving.

🎯 Features

- 😴 Drowsiness Detection (eye movement & facial analysis)
- 📱 Mobile Phone Usage Detection
- 🍺 Alcohol Detection
- 📍 GPS Alert System (for emergency tracking)
- 📊 Dashboard for monitoring alerts

🛠️ Technologies Used

- Python
- Computer Vision (OpenCV)
- Machine Learning / Deep Learning
- Flask (for server/dashboard)

⚙️ How It Works

1. Captures live video input from camera
2. Processes frames using AI models
3. Detects unsafe behavior (drowsiness, phone use, alcohol)
4. Triggers alerts and warnings
5. Displays results on dashboard

📂 Project Structure

- "dashboard/" – Frontend interface
- "ai_detection.py" – Core detection logic
- "phone_detection.py" – Mobile detection
- "gps_alert.py" – Location alert system
- "server.py" – Backend server
- "requirements.txt" – Dependencies

▶️ How to Run

pip install -r requirements.txt
python server.py

🚀 Future Scope

- Integration with IoT sensors
- Real-time cloud monitoring
- Deployment in smart vehicles

👩‍💻 Author

Likhitha N
