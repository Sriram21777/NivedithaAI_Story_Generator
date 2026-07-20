# NivedithaAI_Story_Generator
This is a story generator that creates unique and creative story based on user provided prompts. the application features a simple and interactive user interface built with gradio, allowing user to enter a story ideas ,genre, characters and length and instantly generates engaging stories.

Project Link: https://huggingface.co/spaces/user314r/new-space-Lecture2

# 📚 NivedithaAI Story Generator

An AI-powered story generation application built using **Gradio** and **Google Gemini AI**. The application allows users to provide a story plot and instantly generates a creative story, extracts the characters involved, and provides a concise summary.

---

## 🚀 Features

* ✨ Generate unique and creative stories from a simple story plot.
* 📖 AI-generated story of approximately 250 words.
* 👥 Automatic extraction of characters appearing in the story.
* 📄 AI-generated summary of the story.
* 🎨 Clean and interactive Gradio-based user interface.
* ⚡ Powered by Google's Gemini Generative AI model.

---

## 🖥️ User Interface

The application consists of four main sections:

### 📝 Story Plot

Enter the idea or prompt for your story.

Example:

```
A young archaeologist discovers a hidden underground city beneath the Sahara Desert.
```

---

### 📖 Generated Story

Displays the AI-generated story based on the given plot.

---

### 👥 Characters

Lists all the important characters appearing in the generated story.

Example:

```
• Maya
• Professor Ethan
• The Guardian
```

---

### 📄 Story Summary

Provides a short 2–3 sentence summary of the generated story.

---

## 🛠️ Technologies Used

* Python 3.10+
* Gradio
* Google Gemini API
* python-dotenv

---

## 📦 Project Structure

```
NivedithaAI_Story_Generator/
│
├── app.py                 # Main application
├── .env                   # Stores Gemini API Key
├── requirements.txt
├── README.md
└── assets/                # (Optional images/icons)
```

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/NivedithaAI_Story_Generator.git

cd NivedithaAI_Story_Generator
```

---

### 2. Create a Virtual Environment (Optional)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install gradio google-generativeai python-dotenv
```

---

## 🔑 Setting Up Gemini API

Create a file named

```
.env
```

Add your Gemini API key

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain a Gemini API key from Google AI Studio.

---

## ▶️ Running the Application

Run

```bash
python app.py
```

The application will start on

```
http://127.0.0.1:7860
```

or a public Gradio URL if

```python
share=True
```

is enabled.

---

# 📖 Code Explanation

## 1. Importing Libraries

```python
import gradio as gr
import os
import google.generativeai as genai
from dotenv import load_dotenv
```

### Purpose

* **gradio** builds the web interface.
* **os** accesses environment variables.
* **google.generativeai** communicates with the Gemini model.
* **dotenv** loads API keys from the `.env` file.

---

## 2. Loading Environment Variables

```python
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

Loads the Gemini API key securely from the `.env` file instead of hardcoding it.

---

## 3. Configuring Gemini

```python
genai.configure(api_key=api_key)
```

Authenticates the application with Google's Gemini API.

---

## 4. Loading the AI Model

```python
model = genai.GenerativeModel("gemini-3.5-flash")
```

Creates an instance of the Gemini Flash model, optimized for fast text generation.

---

## 5. Story Generation Function

```python
def generate_story(plot):
```

This function accepts the story plot entered by the user.

It sends a carefully designed prompt to Gemini asking it to produce:

* A story
* Character list
* Summary

---

## 6. Prompt Engineering

```python
prompt = f"""
...
"""
```

The prompt instructs Gemini to return the output in a structured format:

```
Story:

Characters:

Summary:
```

This makes it easier to extract each section.

---

## 7. Calling Gemini

```python
response = model.generate_content(prompt)
```

Gemini generates the complete response based on the supplied prompt.

---

## 8. Parsing the Response

The response is divided into three sections.

```python
Story
Characters
Summary
```

If parsing fails, the application safely returns the generated text and placeholder values instead of crashing.

---

## 9. Building the Interface

The application uses **Gradio Blocks**.

### Story Plot

```python
gr.Textbox()
```

Allows users to enter the story prompt.

---

### Generate Button

```python
gr.Button()
```

Triggers AI story generation.

---

### Story Output

Displays the generated story.

---

### Characters Output

Displays extracted character names.

---

### Summary Output

Displays a concise story summary.

---

## 10. Event Handling

```python
generate.click(...)
```

When the user clicks **Generate Story**, Gradio:

1. Reads the story plot.
2. Sends it to Gemini.
3. Receives the generated response.
4. Updates all output sections automatically.

---

## 11. Launching the Application

```python
demo.launch(share=True)
```

Starts the Gradio server.

When `share=True`, Gradio also generates a temporary public URL that can be shared with others.

---

# 📚 Dependencies

| Package             | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| gradio              | Builds the interactive web interface                  |
| google-generativeai | Connects the application to Google's Gemini AI model  |
| python-dotenv       | Loads environment variables from the `.env` file      |
| os                  | Reads environment variables from the operating system |

---

## requirements.txt

```text
gradio
google-generativeai
python-dotenv
```

---

## Future Enhancements

* 🎭 Genre selection (Fantasy, Mystery, Sci-Fi, Romance, Horror, etc.)
* 👥 User-defined character names.
* 📏 Adjustable story length (Short, Medium, Long).
* 🖼️ AI-generated illustrations for stories.
* 📥 Export stories as PDF or DOCX.
* 🔊 Text-to-Speech narration.
* 🌐 Multi-language story generation.
* 📚 Story history and favorites.

---

## Project Link

Hugging Face Space:

[https://huggingface.co/spaces/user314r/new-space-Lecture2](https://huggingface.co/spaces/user314r/new-space-Lecture2)

---

## Author

Developed as an AI-powered storytelling application using **Gradio** and **Google Gemini AI** to demonstrate interactive generative AI capabilities with a user-friendly web interface.

You can customize the repository URL and author section before publishing the project.
