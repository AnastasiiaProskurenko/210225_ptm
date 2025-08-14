from flask import Flask, request, jsonify
from pydantic import BaseModel


app = Flask(__name__)


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True


@app.route('/register', methods=['POST'])
def regiser():
    data = request.get_json()
    try:
        user = User(**data)
        return jsonify({'message': 'success'})
    except BaseException as e:
        return jsonify({'error': str(e)}), 400

    # if "username" not in data or len(data["username"]) < 3:
    #     return jsonify({"error": "Username too short"}), 400
    # if "age" not in data or not isinstance(data["age"], int) or data["age"] < 18:
    #     return jsonify({"error": "Age must be >= 18"}), 400
    # if "email" not in data or "@" not in data["email"]:
    #     return jsonify({"error": "Invalid email"}), 400
    #
    # return jsonify({"message": "User registered successfully"})






if __name__ == '__main__':
    app.run(debug=True)