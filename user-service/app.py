from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
next_id = 1

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400
    user = {"id": next_id, "name": data["name"], "email": data["email"]}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "email" in data:
        users[user_id]["email"] = data["email"]
    return jsonify(users[user_id])

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "user-service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
