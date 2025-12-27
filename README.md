📱 QuickFix Phone Repair Chatbot API

A Flask-based chatbot backend API designed to automate customer support for a phone repair business.
The chatbot answers common customer questions about prices, services, business hours, warranty, appointments, and contact details.

This project demonstrates clean backend architecture, API design, and rule-based conversational logic, with future support for AI-powered automation.

🚀 Features

✅ RESTful API built with Flask

✅ Rule-based chatbot logic (fast & reliable)

✅ Business information centralized in configuration

✅ JSON responses (frontend & mobile friendly)

✅ CORS enabled for frontend integration

✅ Health check endpoint

✅ AI-ready architecture (DeepSeek / OpenAI can be added)

🧠 How the Chatbot Works

The chatbot analyzes user messages using keyword matching and returns structured responses.

Supported topics:

Greetings

Screen repair services

Battery replacement

Pricing

Business hours

Appointments

Warranty information

Contact & location details

Customer complaints

🗂 Project Structure
phone-repair-chatbot/
│
├── app.py              # Main Flask application
├── chatbot.py          # Chatbot logic & message analysis
├── config.py           # Business configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

🛠 Technologies Used

Python 3

Flask

Flask-CORS

REST API principles

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/phone-repair-chatbot.git
cd phone-repair-chatbot

2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the Application
python app.py


Server will start at:

http://localhost:5000

🔌 API Endpoints
🏠 Home

GET /

Shows API status and available endpoints

💬 Chat Endpoint

POST /chat

Request Body

{
  "message": "How much is screen repair?"
}


Response

{
  "response": "Screen Replacement costs 25000 TZS and takes about 1 hour.",
  "type": "service",
  "confidence": 0.9
}

🏢 Business Info

GET /info

Returns business details such as services, prices, and working hours.

❤️ Health Check

GET /health

{
  "status": "healthy",
  "service": "phone-repair-chatbot"
}


Useful for deployment monitoring.

🧪 Example Test Using cURL
curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{"message":"What time are you open?"}'

🔮 Future Improvements

🤖 AI integration (DeepSeek / OpenAI)

📊 Conversation analytics

🗄 Database integration

🌍 Multi-language support

🔐 Authentication for admin dashboard

🚀 Cloud deployment (Render, Railway, VPS)

🎯 Use Cases

Phone repair shops

Small business customer support

WhatsApp / Telegram bot backend

AI automation learning project

Freelance backend portfolio project

👨‍💻 Author

Digo Master
Backend Developer & Automation Enthusiast

📌 This project was built as a learning and portfolio project, focusing on clean architecture and real-world backend practices.

📄 License

This project is open-source and available under the MIT License.
You are free to use, modify, and distribute it.
