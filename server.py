import flask
import random
import json
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get():
    return '''
    <h3>GET /answers/user_id</h3>
    <h3>POST /answers/user_id</h3>
    <h3>GET /questions/question_id</h3>
    <h3>GET /questions/h3>
    <h3>GET /config/user_id</h3>
    <h3>GET /login/user_id</h3>
    <h3>POST /register</h3>
    '''


@app.route('/answers/<user_id>', methods=['GET', 'POST'])
def answers(user_id):
    if request.method == 'GET':
        data = open(f'answers/{user_id}.json', 'rb').read()
        return json.loads(data)

    elif request.method == 'POST':
        new_answer = request.get_json()
        config_data = json.loads(open(f'answers/{user_id}.json', 'rb').read())
        # Add the new answer from POST to current JSON
        config_data["data"].append(new_answer)
        with open(f'answers/{user_id}.json', 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)
        return f"Data for {user_id} updated!"


@app.route('/questions/<question_id>', methods=['GET'])
def question(question_id):
    question_data = open('questions.json', 'rb').read()
    question_data = json.loads(question_data)
    for question in question_data:
        if question["id"] == int(question_id):
            return question
    return "Question not found!"


@app.route('/questions/', methods=['GET'])
def questions():

    question_data = open('questions.json', 'rb').read()
    question_data = json.loads(question_data)
    print(question_data)
    return jsonify(question_data)


@app.route('/config/<user_id>', methods=['GET'])
def config(user_id):
    config_data = open('users.json', 'rb').read()
    config_data = json.loads(config_data)
    for user in config_data:
        if user["id"] == int(user_id):
            return user
    return "User config not found!"


@app.route('/login/<user_id>', methods=['GET'])
def login(user_id):
    config_data = open('users.json', 'rb').read()
    config_data = json.loads(config_data)
    for user in config_data:
        if user["id"] == int(user_id):
            return {"status": True}
    return {"status": False}


def generate_new_id():
    config_data = open('users.json', 'rb').read()
    config_data = json.loads(config_data)
    taken_ids = [user["id"] for user in config_data]
    available_ids = [item for item in range(
        100000, 999999) if item not in taken_ids]
    return random.choice(available_ids)

# Send {"name": "<Name for user>"} in POST


@app.route('/register', methods=['POST'])
def register():
    user_id = generate_new_id()
    user_name = request.get_json()["name"]
    if len(user_name) < 1:
        return "Bad username given!"
    new_user = {
        "id": user_id,
        "name": user_name,
        "config": {
            "answering": {
                "yes_no": {
                    "enabled": True,
                    "icon": True
                },
                "slider": {
                    "enabled": True
                },
                "voice_recording": {
                    "enabled": True
                },
                "digital_clock": True
            },
            "question": {
                "text_to_speech": True
            }
        }
    }

    answer_data = {
        "answers": [],
        "patientID": user_id
    }

    config_data = open('users.json', 'rb').read()
    config_data = json.loads(config_data)
    config_data.append(new_user)
    with open(f'users.json', 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=4)
    with open(f'answers/{user_id}.json', 'w', encoding='utf-8') as f:
        json.dump(answer_data, f, ensure_ascii=False, indent=4)

    return new_user