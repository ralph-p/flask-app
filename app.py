from flask import Flask, jsonify, request, Response, json
from store import notes, add_game_to_DB, find_all_notes
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Welcome to the notes app'
    })
@app.route('/notes')
def all_notes():
    return jsonify({
        'notes': find_all_notes(),
    })

@app.route('/notes/<note_id>')
def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == note_id:
            return jsonify({
                "note": note,
            })

@app.route('/notes/add', methods=['POST'])
def add_game():
    print(json.loads(request.data))
    data = request.get_json()
    try:
        note = data['note']
        time = data['time']
        if note and time:
            data = add_game_to_DB(note, int(time))
            return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
