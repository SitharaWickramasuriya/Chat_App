# 🟢 Flask WhatsApp-style Chat App

A real-time chat application built using Flask, Flask-SocketIO, and JavaScript, designed with a WhatsApp-like interface. It allows multiple users to communicate instantly, with features like timestamps, typing indicators, emoji support, and a clean responsive UI.

# 🧩 Features
✅ Real-Time Messaging: Instant message delivery using WebSockets (via Flask-SocketIO).

🕓 Timestamps: Every message includes the time it was sent.

👤 User Login: Simple username-based login screen.

💬 Typing Indicator: Shows when another user is typing.


😄 Emoji Support: Easily insert emojis into messages.

📱 Responsive Design: Optimized for desktop and mobile view.

🎨 WhatsApp-Style UI: Familiar look with green and white chat bubbles.

# 🔧 Technologies Used
Frontend: HTML, CSS (custom styles), JavaScript

Backend: Python with Flask

Real-Time Engine: Flask-SocketIO + Eventlet

# 📁 Project Structure
<pre>
  chat_app/
│
├── app.py                 # Main Flask server
├── requirements.txt       # (Optional) Dependencies
├── templates/
│   └── index.html         # Chat interface
├── static/
│   └── style.css          # WhatsApp-style CSS 
</pre>
  
# 🚀 Getting Started
1. Clone the Repository
<pre>
  git clone https://github.com/SitharaWickramasuriya/chat_app.git 
  cd chat_app </pre>
2. Install Dependencies
<pre>
  pip install flask flask-socketio eventlet </pre>
3. Run the App
<pre>
  python app.py </pre>
4. Open in Browser
Visit: http://localhost:5000

# 📦 To-Do / Future Improvements
🔐 User authentication with passwords

💾 Store chat history in a database

📎 File and image sharing

🌙 Dark mode toggle

✅ Message read indicators (like WhatsApp blue ticks)

📱 Convert to mobile app with React Native or Flutter



