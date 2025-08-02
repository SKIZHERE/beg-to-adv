from pathlib import Path
from openai import OpenAI

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)
speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)