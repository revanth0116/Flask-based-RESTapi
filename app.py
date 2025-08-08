from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {'name': 'Alice', 'email':"alice@example.com"},
    2: {'name': 'Bob', 'email':'bob@email.com'}
}
@app.route('/')
def home():
    return "Welcome to the Flask User API! Use /users to access user data."

#GET - get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

#GET - get a specific user by ID
@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error":"User not Found"}), 404
    return jsonify(user)

#POST - Create a new user
@app.route("/users", methods=['POST'])
def create_new_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"Error":"Invalid input"}), 404
    
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {'name' : data['name'],'email': data['email']}
    return jsonify({"id": new_id, "message" : "User created"}), 201

#PUT - Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({'error':'User not Found'})
    
    users[user_id].update(data)
    return jsonify({'message':'user updated'})

#DELETE -delete a user
@app.route('/users/<int:user_id>', methods = ['DELETE'])
def remove_user(user_id):
    if user_id not in users:
        return jsonify({'error':'User not found'})
    
    del users[user_id]
    return jsonify({'message':'User Deleted'})


if __name__ == '__main__':
    app.run(debug = True)