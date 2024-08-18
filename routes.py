from flask import request, jsonify
from models import db, ToDoItem
from app import app

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = ToDoItem(
        title=data['title'],
        description=data.get('description', ''),
        deadline=data.get('deadline')
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "To-Do item created"}), 201

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = ToDoItem.query.all()
    return jsonify([{
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "deadline": todo.deadline
    } for todo in todos]), 200

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = ToDoItem.query.get_or_404(id)
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "deadline": todo.deadline
    }), 200

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = ToDoItem.query.get_or_404(id)
    data = request.get_json()
    todo.title = data['title']
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    todo.deadline = data.get('deadline', todo.deadline)
    db.session.commit()
    return jsonify({"message": "To-Do item updated"}), 200

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = ToDoItem.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "To-Do item deleted"}), 204

