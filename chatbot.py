from config import BUSINESS_INFO


def analyze_message(user_message: str) -> dict:
    if not user_message or not user_message.strip():
        return {
            "response": "Please type a valid question so I can help you 😊",
            "type": "validation",
            "confidence": 0.30
        }

    message = user_message.lower().strip()

    # 1. GREETINGS
    if any(word in message for word in ["hi", "hello", "hey", "good morning", "good afternoon"]):
        return {
            "response": f"Hello! Welcome to {BUSINESS_INFO['name']} 👋 How can I help you today?",
            "type": "greeting",
            "confidence": 0.95
        }

    # 2. SCREEN REPAIR
    if any(word in message for word in ["screen", "crack", "broken", "display", "glass", "lcd", "touch"]):
        service = BUSINESS_INFO["services"]["screen"]
        return {
            "response": (
                f"{service['name']} costs {service['price']} {BUSINESS_INFO['currency']} "
                f"and takes about {service['time']}. {service['description']}."
            ),
            "type": "service",
            "service": "screen",
            "confidence": 0.90
        }

    # 3. BATTERY REPAIR
    if any(word in message for word in ["battery", "charge", "power", "dies", "drains"]):
        service = BUSINESS_INFO["services"]["battery"]
        return {
            "response": (
                f"{service['name']} costs {service['price']} {BUSINESS_INFO['currency']} "
                f"and takes about {service['time']}. {service['description']}."
            ),
            "type": "service",
            "service": "battery",
            "confidence": 0.90
        }

    # 4. PRICING
    if any(word in message for word in ["price", "cost", "how much", "fee"]):
        s = BUSINESS_INFO["services"]
        return {
            "response": (
                "Our prices:\n"
                f"• {s['screen']['name']}: {s['screen']['price']} {BUSINESS_INFO['currency']}\n"
                f"• {s['battery']['name']}: {s['battery']['price']} {BUSINESS_INFO['currency']}\n"
                f"All repairs include a {BUSINESS_INFO['warranty_days']}-day warranty."
            ),
            "type": "pricing",
            "confidence": 0.85
        }

    # 5. BUSINESS HOURS
    if any(word in message for word in ["open", "hours", "time", "close", "when"]):
        return {
            "response": (
                f"We're open {BUSINESS_INFO['hours']}. "
                f"We are closed on {', '.join(BUSINESS_INFO['closed_days'])}."
            ),
            "type": "hours",
            "confidence": 0.85
        }

    # 6. CONTACT
    if any(word in message for word in ["contact", "phone", "call", "address", "location", "where"]):
        return {
            "response": (
                f"📞 Phone: {BUSINESS_INFO['phone']}\n"
                f"📍 Address: {BUSINESS_INFO['address']}\n"
                f"⏰ Hours: {BUSINESS_INFO['hours']}"
            ),
            "type": "contact",
            "confidence": 0.90
        }

    # 7. APPOINTMENT
    if any(word in message for word in ["appointment", "book", "schedule", "visit"]):
        return {
            "response": (
                "You can visit us during business hours or call to book an appointment.\n"
                "Average waiting time is 15–30 minutes."
            ),
            "type": "appointment",
            "confidence": 0.80
        }

    # 8. WARRANTY
    if any(word in message for word in ["warranty", "guarantee", "guaranteed"]):
        return {
            "response": (
                f"All repairs come with a {BUSINESS_INFO['warranty_days']}-day warranty "
                "covering parts and labor."
            ),
            "type": "warranty",
            "confidence": 0.85
        }

    # 9. COMPLAINTS
    if any(word in message for word in ["complaint", "bad", "terrible", "angry", "unhappy"]):
        return {
            "response": (
                "We're sorry for your experience 😔.\n"
                "Please visit us or call and ask for the manager so we can resolve it."
            ),
            "type": "complaint",
            "confidence": 0.70
        }

    # 10. DEFAULT
    return {
        "response": (
            "I can help with screen repairs, battery replacement, prices, hours, "
            "appointments, contact info, and warranty details."
        ),
        "type": "default",
        "confidence": 0.40
    }
