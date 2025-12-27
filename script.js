const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");

function addMessage(message, isUser = false) {
    const div = document.createElement("div");
    div.className = `message ${isUser ? "user-message" : "bot-message"}`;

    const time = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

    div.innerHTML = `
        <div class="message-content">${message.replace(/\n/g, "<br>")}</div>
        <div class="message-time">${time}</div>
    `;

    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTyping() {
    const div = document.createElement("div");
    div.id = "typing";
    div.className = "message bot-message";
    div.innerHTML = `
        <div class="message-content">
            <span class="typing-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    `;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing");
    if (typing) typing.remove();
}

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, true);
    userInput.value = "";

    showTyping();

    fetch("http://192.168.1.5:5000/chat", {

        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
        .then(res => res.json())
        .then(data => {
            removeTyping();
            addMessage(data.response);
        })
        .catch(() => {
            removeTyping();
            addMessage("⚠️ Server not reachable.");
        });
}

function sendQuickMessage(text) {
    userInput.value = text;
    sendMessage();
}

function handleKeyPress(e) {
    if (e.key === "Enter") sendMessage();
}

window.sendMessage = sendMessage;
window.sendQuickMessage = sendQuickMessage;
window.handleKeyPress = handleKeyPress;
