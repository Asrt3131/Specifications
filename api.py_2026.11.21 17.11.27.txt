from flask import Flask, jsonify

app = Flask(__name__)

PROJECTS_DATA = [
    {"id": 1, "title": "SMS Spam Detector", "live": "https://sms-spam-detector-kb98vmxzj65ttuffy6h56dsyvu55.streamlit.app/", "github": "https://github.com/Asrt3131/sms-spam-detector.git"},
    {"id": 2, "title": "House Price Prediction", "live": "https://house-price-prediction-acuccze543baay6rn4354syp34bgbq.streamlit.app/", "github": "https://github.com/Asrt3131/house-price-prediction.git"},
    {"id": 3, "title": "Persian RAG Chatbot", "live": "https://persian-rag-chatbot-amtzeujabqdazrzcvnrew5.streamlit.app/", "github": "https://github.com/Asrt3131/persian-rag-chatbot.git"},
    {"id": 4, "title": "Medical-Legal RAG", "live": "https://medical-legal-rag-f8whusetlraqtgxt8lwiam.streamlit.app/", "github": "https://github.com/Asrt3131/medical-legal-rag.git"},
    {"id": 5, "title": "AI Agent Tool Calling", "live": "https://ai-agent-tool-calling-f6rdca8iuuhukcwe7lrnl5.streamlit.app/", "github": "https://github.com/Asrt3131/ai-agent-tool-calling.git"},
    {"id": 6, "title": "Realtime Vision YOLOv8", "live": "https://realtime-vision-yolov8-mediapipe-emyqrahh3wfbgyvvycvcfq.streamlit.app/", "github": "https://github.com/Asrt3131/realtime-vision-yolov8-mediapipe.git"},
    {"id": 7, "title": "ML API Project", "live": "https://ml-api-project-8xte3fdm8ft2see9qzezu9.streamlit.app/", "github": "https://github.com/Asrt3131/ml-api-project.git"},
    {"id": 8, "title": "Data Dashboard", "live": "https://data-dashboard-srt343-z8hpwmaamvsucqn5jc5a4c.streamlit.app/", "github": "https://github.com/Asrt3131/data-dashboard-srt343.git"}
]

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(PROJECTS_DATA)

if __name__ == '__main__':
    print("🔗 Project API is running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)