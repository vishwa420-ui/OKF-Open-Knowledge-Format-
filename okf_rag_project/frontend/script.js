
const API_URL = "http://127.0.0.1:8000";

const messages = document.getElementById("messages");
const questionInput = document.getElementById("question");
const welcome = document.getElementById("welcome");


// CONNECTION STATUS

async function checkHealth() {

    const status = document.getElementById("connectionStatus");
    const dot = document.querySelector(".status-dot");

    try {

        const response = await fetch(`${API_URL}/health`);

        if (!response.ok) throw new Error("API error");

        const data = await response.json();

        status.textContent = "Backend Connected";
        dot.style.background = "#22c55e";

        document.getElementById("vectorCount").textContent =
            data.stored_vectors;

    } catch {

        status.textContent = "Backend Disconnected";
        dot.style.background = "#ef4444";

    }
}


// DISPLAY MESSAGE

function addMessage(text, type, sources = []) {

    welcome.style.display = "none";

    const wrapper = document.createElement("div");
    wrapper.className = `message ${type}`;

    const content = document.createElement("div");
    content.className = "message-content";
    content.textContent = text;

    wrapper.appendChild(content);

    if (type === "ai-message" && sources.length) {

        const sourceBox = document.createElement("div");
        sourceBox.className = "source-list";

        const heading = document.createElement("strong");
        heading.textContent = "📚 Retrieved Sources";
        sourceBox.appendChild(heading);

        sources.forEach(source => {

            const item = document.createElement("div");
            item.className = "source-item";

            item.textContent =
                `${source.title} (${source.source})`;

            sourceBox.appendChild(item);

        });

        wrapper.appendChild(sourceBox);

    }

    messages.appendChild(wrapper);

    messages.scrollTop = messages.scrollHeight;
}


// ASK QUESTION

async function sendQuestion() {

    const question = questionInput.value.trim();

    if (!question) return;

    addMessage(question, "user-message");

    questionInput.value = "";

    const button = document.getElementById("sendBtn");
    button.disabled = true;

    const loading = document.createElement("div");
    loading.className = "message ai-message";
    loading.textContent = "Searching knowledge base...";
    messages.appendChild(loading);

    try {

        const response = await fetch(`${API_URL}/query`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        if (!response.ok) {
            throw new Error(await response.text());
        }

        const data = await response.json();

        loading.remove();

        addMessage(
            data.answer,
            "ai-message",
            data.sources || []
        );

    } catch (error) {

        loading.remove();

        addMessage(
            "Error connecting to the backend: " + error.message,
            "ai-message"
        );

    } finally {

        button.disabled = false;
        questionInput.focus();

        checkHealth();

    }
}


// INGEST KNOWLEDGE

async function ingestKnowledge() {

    const button = document.querySelector(".ingest-btn");

    button.disabled = true;
    button.textContent = "Ingesting...";

    try {

        const response = await fetch(`${API_URL}/ingest`, {
            method: "POST"
        });

        if (!response.ok) {
            throw new Error(await response.text());
        }

        const data = await response.json();

        alert(
            `Ingestion completed!\n\n` +
            `Documents: ${data.documents_processed}\n` +
            `Chunks: ${data.chunks_stored}\n` +
            `Vectors: ${data.total_vectors}`
        );

        checkHealth();

    } catch (error) {

        alert("Ingestion failed: " + error.message);

    } finally {

        button.disabled = false;
        button.textContent = "↻ Ingest Knowledge";

    }
}


// SUGGESTIONS

function suggestQuestion(text) {

    questionInput.value = text;
    sendQuestion();

}


// NEW CHAT

function newChat() {

    messages.innerHTML = "";
    welcome.style.display = "block";

}


// ENTER KEY

function handleEnter(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();
        sendQuestion();

    }

}


// INITIALIZE

checkHealth();

setInterval(checkHealth, 10000);
