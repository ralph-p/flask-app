import os
from supabase import create_client, Client
import json

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# Function to Fetch All Notes
def find_all_notes():
    data = supabase.table("notes").select("*").execute()
    # Equivalent for SQL Query "SELECT * FROM notes;"
    response_data = data.json()
    json_data = json.loads(response_data)['data']
    return json_data

def add_game_to_DB(note, time) -> dict:

    game = {
        "note": note,
        "time": time
    }
    data = supabase.table("notes").insert(game).execute()
    # Equivalent to the SQL Insert

    response_data = data.json()
    json_data = json.loads(response_data)['data']
    return json_data

notes = find_all_notes()