from pathlib import Path
import openai
from openai import OpenAI
import autogen
import json
import os
import re
from pathlib import Path

# Change the directories to pick up the files. Ensure you use your own OpenAI API Keys
with open("locations.json", 'r', encoding='utf-8') as f:
        path = json.load(f)

configurations_path = path[0]["configurations_path"]
# configurations_path = "G:/My Drive/Data-Centric Solutions/07. Blog Posts/AutoGen 2 - Flights/"

config_list_gpt = autogen.config_list_from_json(
    env_or_file="configurations.json",
    file_location=configurations_path,
    filter_dict={
        "model": ["gpt-4-1106-preview"],
        # "model": ["gpt-3.5-turbo-16k"]
    },

)
api_key = config_list_gpt[0]['api_key']
print(api_key)

client = OpenAI(api_key=api_key)


def generate_speech_files_from_json(json_file, client, output_directory, model_rap_name):
    """
    Generate speech files from a JSON file containing conversation data.

    Args:
        json_file (str): Path to the JSON file containing conversation data.
        client (OpenAI): Client for the text-to-speech API.
        output_directory (str): Directory to save the output MP3 files.
    """
    # Read the conversation data from the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        conversation_data = json.load(f)

    # Assign voices to each participant
    voices = {
        'G_Turbo': 'echo',
        model_rap_name: 'onyx',
        'judge': 'alloy'
    }

    # Create the output directory if it doesn't exist
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Process each message in the conversation
    for message in conversation_data:
        if message['name'] == 'host':
            continue  # Skip messages from host

        # Extract the turn number and participant name
        turn_match = re.search(r'Round (\d+)', message['content'])
        turn_number = turn_match.group(1) if turn_match else '0'
        participant = message['name']

        # Determine the file name
        filename = f"{participant}_{turn_number}.mp3"
        file_path = Path(output_directory) / filename

        # Generate speech
        response = client.audio.speech.create(
            model="tts-1",
            voice=voices.get(participant),
            input=message['content']
        )

        # Save to file
        response.stream_to_file(str(file_path))
        print(f"Generated speech file: {file_path}")

# Example usage
# Reading from the file 'rap_name.txt'
with open('rap_name.txt', 'r', encoding='utf-8') as file:
    model_rap_name = file.read()

json_file_path = f'{model_rap_name}/specific_conversation_data.json'  # Replace with the path to your JSON file
output_dir = f'{model_rap_name}/output_speech_files'
generate_speech_files_from_json(json_file_path, client, output_dir, model_rap_name)