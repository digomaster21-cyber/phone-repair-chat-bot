from flask import Flask, request, jsonify
from flask_cors import CORS

from chatbot import analyze_message
from config import BUSINESS_INFO

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return """
    <h1>QuickFix Phone Repair Chatbot API</h1>
    <p>Status: Running ✅</p>

    <h3>Available Endpoints</h3>
    <ul>
        <li><b>POST</b> /chat – Chat with the bot</li>
        <li><b>GET</b> /info – Business information</li>
        <li><b>GET</b> /health – Health check</li>
    </ul>

    <p>Example POST request to <code>/chat</code>:</p>
    <pre>
    {
        "message": "How much is screen repair?"
    }
    </pre>
    """


@app.route("/info", methods=["GET"])
def info():
    return jsonify(BUSINESS_INFO)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "phone-repair-chatbot"
    })


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receives:
        {
            "message": "user question"
        }

    Returns:
        {
            "response": "bot answer",
            "type": "category",
            "confidence": 0.85
        }
    """
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({
                "error": "Missing 'message' field",
                "example": {"message": "What time are you open?"}
            }), 400

        user_message = data.get("message", "")
        bot_reply = analyze_message(user_message)

        return jsonify(bot_reply), 200

    except Exception as error:
        return jsonify({
            "error": "Internal server error",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Starting QuickFix Phone Repair Chatbot API")
    print("=" * 50)
    print(f"📍 Business: {BUSINESS_INFO['name']}")
    print(f"⏰ Hours: {BUSINESS_INFO['hours']}")
    print(f"📞 Phone: {BUSINESS_INFO['phone']}")
    print("\n🌐 Server running at: http://localhost:5000")
    print("🛑 Press CTRL+C to stop the server")
    print("=" * 50)

    app.run(host="0.0.0.0", port=5000, debug=True)
