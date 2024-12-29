# Chatbot AI with Text-to-Speech (TTS)

This project implements a simple AI chatbot that responds to user inputs with text-to-speech (TTS) output. The chatbot is designed to engage in natural language conversations, and it uses OpenAI's GPT model to generate responses. The system also integrates text-to-speech functionality to make the chatbot's responses audible.

## Features

- **Natural Language Processing (NLP):** Uses OpenAI's GPT model to understand and generate human-like text responses.
- **Text-to-Speech (TTS):** The chatbot's responses are converted into speech using the pyttsx3 library.
- **User Interaction:** The chatbot engages in an interactive conversation, responding to user inputs in a friendly and supportive manner.
- **Customizable Voices:** You can configure the voice settings for TTS, including selecting different male or female voices.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `openai`: To interact with OpenAI's GPT models.
- `pyttsx3`: For text-to-speech functionality.
- `pyttsx3` requires `pyaudio` for audio output.

You can install the required dependencies using `pip`:

```bash
pip install openai pyttsx3 pyaudio
