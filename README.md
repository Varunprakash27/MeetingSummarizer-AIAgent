# MeetingSummarizer-AIAgent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Supported-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-lightgreen)
![Status](https://img.shields.io/badge/Status-Production-green)

## Overview

MeetingSummarizer-AIAgent is an AI-powered application that transforms raw meeting transcripts into structured summaries. It leverages OpenAI's GPT-4o via LangChain Agents to generate clear outputs including meeting topics, discussion summaries, action items, and participants. This tool can serve teams looking to automate note-taking and post-meeting documentation.

---

## Features

- Extracts key elements from meeting transcripts:
  - Meeting topic
  - Summary of discussions
  - Action items
  - Participants

- Saves the output as a timestamped summary file
- Utilizes LangChain Tool-Calling Agent and Pydantic for validation
- Clean, modular code structure for easy extension and integration

---

## Project Structure

```
MeetingSummarizer-AIAgent/
├── main.py                 # Agent logic and summary parsing
├── tools.py                # Tool class used for saving output
├── meeting_transcript.txt  # Sample input file
├── .env                    # API key (excluded from version control)
├── .gitignore              # Ignored files and folders
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Varunprakash27/MeetingSummarizer-AIAgent.git
cd MeetingSummarizer-AIAgent
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Activate on macOS/Linux
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up API credentials**

Create a `.env` file in the project root with the following:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Usage

1. Replace the content in `meeting_transcript.txt` with your own meeting transcript.

2. Run the application:

```bash
python main.py
```

3. The output will include:
   - Structured response printed in the terminal
   - A formatted summary saved in `meeting_summary.txt`

---

## Example Output

**Timestamp:** 2025-07-24 15:42:10  
**Meeting Topic:** Q2 Marketing Strategy  
**Summary:** Discussion around campaign performance, audience targeting, and planning for the upcoming product release.  
**Action Items:**
- Alice to compile email engagement data  
- Bob to draft Q2 ad creatives  
- Carol to schedule stakeholder sync-up  
**Participants:** Alice, Bob, Carol, David

---

## Built With

- Python 3.9+
- OpenAI GPT-4o
- LangChain
- Pydantic
- python-dotenv

---

## Extensions

- Integrate with platforms like Slack, Google Meet, or Zoom
- Automate email dispatch of summaries
- Add support for live multi-session meeting summaries
- Enable semantic search over archived summaries

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Author

Developed by **Varun Prakash**
For questions or contributions, feel free to create an issue or submit a pull request.

---
