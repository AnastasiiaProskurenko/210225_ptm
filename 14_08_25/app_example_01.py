from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if "username" not in data or len(data["username"]) < 3:
        return jsonify({"error": "Username too short"}), 400
    if "age" not in data or not isinstance(data["age"], int) or data["age"] < 18:
        return jsonify({"error": "Age must be >= 18"}), 400
    if "email" not in data or "@" not in data["email"]:
        return jsonify({"error": "Invalid email"}), 400

    return jsonify({"message": "User registered successfully"})


if __name__ == '__main__':
    app.run(debug=True)