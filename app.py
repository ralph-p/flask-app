from flask import Flask, jsonify
from store import notes
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Welcome to the notes app'
    })
@app.route('/notes')
def all_notes():
    return jsonify({
        'notes': notes,
    })

@app.route('/notes/<note_id>')
def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == int(note_id):
            return jsonify({
                "note": note,
            })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
