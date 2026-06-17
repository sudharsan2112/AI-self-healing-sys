from flask import Flask, request, jsonify
from flask_cors import CORS

from ann_model import predict_error
from rl_agent import RLAgent
from auto_heal import execute_action

app = Flask(__name__)
CORS(app)

agent = RLAgent()

@app.route('/')
def home():
    return jsonify({"message": "Self-Healing AI System Running"})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    log_message = data.get('log')

    error_type = predict_error(log_message)
    action = agent.choose_action(error_type)
    status = execute_action(action)

    return jsonify({
        "error_type": error_type,
        "action": action,
        "status": status
    })

if __name__ == '__main__':
    app.run(debug=True)
