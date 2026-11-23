# Day 39 – Python AI Chatbot

A simple AI-powered terminal chatbot built with Python and Groq API. It can answer user questions, maintain conversation history, and handle API errors.

## Features

- AI-powered responses using Groq API
- Conversation history and context retention
- System prompt customization
- API key management using `.env`
- API key validation
- Error handling with `try-except`
- Empty input validation
- Exit command to close the chatbot
- Simple terminal interface

## Technologies Used

- Python
- Groq API
- OpenAI Python SDK
- python-dotenv

## Project Structure

```text
day39/
│
├── chatbot.py
├── main.py
├── .env
└── README.md
```

**Note:** The `.env` file is excluded from GitHub for security reasons.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DipDay/Python-Automation-60Days.git
```

### 2. Navigate to the project folder

```bash
cd Python-Automation-60Days/day39
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure API Key

Create a `.env` file inside the `day39` folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/keys).

### 5. Run the chatbot

```bash
python chatbot.py
```

## Usage

Start the chatbot and type your questions in the terminal.

```text
=============================================
             PYTHON AI CHATBOT
=============================================
Ask me anything!
Type 'exit' to quit.
---------------------------------------------

You: My name is Dip.

Chatbot: Nice to meet you, Dip!

You: What is my name?

Chatbot: Your name is Dip!

You: exit

Chatbot: Goodbye!
```

## What I Learned

- Working with LLM APIs
- API authentication
- Understanding system, user, and assistant roles
- Prompt engineering basics
- Managing conversation history
- Context management
- Exception handling
- Environment variables and API key security

## Project Status

Completed – Day 39 of the 60 Days Python Automation Challenge.

---

**Author:** Dip Dey  
**Challenge:** Python Automation – 60 Days