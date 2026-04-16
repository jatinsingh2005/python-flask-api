from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Flask API is running 🚀"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')

    if not task:
        return jsonify({"error": "Task is required"}), 400

    tasks.append(task)
    return jsonify({"message": "Task added", "tasks": tasks})

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return jsonify({"message": "Deleted", "task": removed})
    return jsonify({"error": "Invalid index"}), 404

if __name__ == '__main__':
    app.run(debug=True)
