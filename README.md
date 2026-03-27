# adk-text-summarizer
Text summarization AI agent built with Google ADK + Gemini 2.5 Flash for Gen AI Academy APAC. Deployed on Cloud Run with HTTP API &amp; web UI. Simple, scalable, production-ready. Made with ❤️ for learning and showcasing modern AI deployment patterns!



🤖 Text Summarization AI Agent (ADK + Gemini + Cloud Run)
<div align="center">

A production-ready AI agent built with Google's Agent Development Kit (ADK) that performs text summarization using Gemini, deployed on Google Cloud Run with an HTTP endpoint.

🎓 Gen AI Academy APAC Edition Project Submission<br>
⭐ Showcased on GitHub for portfolio purposes

</div>

📖 Table of Contents
Overview<br>
Features<br>
Architecture<br>
Tech Stack<br>
Project Structure<br>
Prerequisites<br>
Installation & Setup<br>
Deployment Steps<br>
How to Use<br>
Testing<br>
API Documentation<br>
Screenshots<br>
Troubleshooting<br>
Future Enhancements<br>
Credits & References<br>
License<br>
Contact<br>

🎯 Overview
This project demonstrates the implementation of a single AI agent using Google's Agent Development Kit (ADK) that performs text summarization using the Gemini 2.5 Flash model. The agent is deployed on Google Cloud Run and is callable via an HTTP endpoint, returning valid responses for given text inputs.


*LIVE DEMO SECTION -->>>>

## 🎯 **Live Demo**
**[https://text-summarizer-agent-863588964400.asia-south1.run.app](https://text-summarizer-agent-863588964400.asia-south1.run.app)**

**Status: 100% Production Ready! ✅ Tested live - works perfectly!**


📸 Live Demo Screenshots





✅ Project Requirements Met
| Requirement                 | Status                                |
| --------------------------- | ------------------------------------- |
| Built using ADK             | ✅ Implemented with google-adk==1.14.0 |
| Uses Gemini model           | ✅ gemini-2.5-flash for inference      |
| Single clearly defined task | ✅ Text summarization                  |
| HTTP endpoint callable      | ✅ Deployed on Cloud Run               |
| Returns valid response      | ✅ JSON response with summary          |
| Simple capability           | ✅ Summarization (not complex logic)   |

✨ Features
🧠 AI-Powered Summarization: Automatically condenses long text into concise, readable summaries<br>

⚡ Fast Response: Uses Gemini 2.5 Flash for minimal latency<br>

🌐 Serverless Deployment: Hosted on Google Cloud Run with auto-scaling<br>

🔌 HTTP REST API: Callable via standard HTTP POST requests<br>

🖥️ Built-in Web UI: Includes ADK developer interface for easy testing<br>

🔐 Secure: Uses Google Cloud IAM and service accounts<br>

📦 Production-Ready: Containerized with Docker and proper IAM permissions<br>

🎓 Educational: Perfect for learning ADK, Cloud Run, and AI agent architecture<br>

🏗️ Architecture<br>
┌─────────────────┐     HTTP Request     ┌──────────────────┐
│                 │  ──────────────────> │                  │
│   Client /      │                      │   Google Cloud   │
│   Browser       │  <─────────────────  │      Run         │
│                 │     JSON Response    │  (ADK Agent)     │
└─────────────────┘                      └────────┬─────────┘
                                                 │
                                                 │ API Call
                                                 │<br>
                                          ┌──────▼───────┐
                                          │              │
                                          │   Gemini     │
                                          │  2.5 Flash   │
                                          │   (Vertex AI)│
                                          │              │
                                          └──────────────┘
Flow Description-<br>

1) User sends HTTP POST request with text to summarize<br>
2)Cloud Run receives request and routes to ADK agent<br>
3)Agent processes text using Gemini model<br>
4)Summary is returned as JSON response<br>

🛠️ Tech Stack
| Component      | Technology        | Purpose                        |
| -------------- | ----------------- | ------------------------------ |
| AI Framework   | Google ADK 1.14.0 | Agent development & deployment |
| AI Model       | Gemini 2.5 Flash  | Text summarization inference   |
| Hosting        | Google Cloud Run  | Serverless container hosting   |
| Container      | Docker            | Application containerization   |
| API Framework  | FastAPI           | HTTP endpoint handling         |
| Python Version | 3.13-slim         | Runtime environment            |
| Authentication | Google IAM        | Service account permissions    |
| Registry       | Artifact Registry | Container image storage        |
| CI/CD          | Cloud Build       | Automated deployment           |

📁 Production File Structure ->>>
text_summarizer_agent/<br>
├── .env                      # Environment variables (API key, model)<br>
├── requirements.txt          # Python dependencies<br>
├── agent.py                  # Main ADK agent definition<br>
├── __init__.py              # Python package initializer<br>
└── Dockerfile               # Container configuration (optional)<br>
File Descriptions -><br>
| File             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| agent.py         | Defines the text summarization agent with Gemini model and instructions |
| requirements.txt | Lists Python dependencies (google-adk, python-dotenv)                   |
| .env             | Stores API keys and configuration (DO NOT commit to git)                |
| Dockerfile       | Container definition for Cloud Run deployment                           |
| __init__.py      | Makes the directory a Python package                                    |

📋 Prerequisites<br>
Before running this project, ensure you have:<br>

Required Accounts & Services<br>
✅ Google Account (personal, not work/school)<br>

✅ Google Cloud Project with billing enabled<br>

✅ Google Cloud SDK (gcloud) installed on your machine<br>

✅ Python 3.11+ installed<br>

🚀 Future Enhancements<br>
1->Potential improvements for future versions:<br>
2->Add support for multiple summarization styles (brief, detailed, bullet points)<br>
3->Implement text length-based routing (short vs. long texts)<br>
4->Add sentiment analysis alongside summarization<br>
5->Support file uploads (PDF, DOCX summarization)<br>
6->Implement caching for repeated texts<br>
7->Add usage analytics dashboard<br>
8->Multi-language summarization support<br>
9->Batch processing for multiple texts<br>
10->Integration with Google Drive/Docs<br>

Now lets come to the commands section ->>><br>

  🚀 Installation & Setup<br>
Step 1: In Cloud terminal set up your project using following command ->
```bash
gcloud config set project [PROJECT_ID]
```

Enable Required APIs
```bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com
```
Step 2: Set Up Virtual Environment (Recommended)
```bash
cd && mkdir text_summarizer_agent && cd text_summarizer_agent
```
Step 3: Install the requirements 
```bash
cloudshell edit requirements.txt
```
After creating requirements txt add the following code to it ->>
```bash
google-adk==1.14.0
langchain-community==0.3.27
wikipedia==1.4.0
```
Next step -> in terminal create a virtual environment using the below mentioned command ->
```bash
uv venv
source .venv/bin/activate
```
Step 4: Configure Environment Variables
Create a .env file in the root directory:
Using the below command your env file will be created.
```bash
# 1. Set the variables in your terminal first
PROJECT_ID=$(gcloud config get-value project)
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
SA_NAME=lab2-cr-service

# 2. Create the .env file using those variables
cat <<EOF > .env
PROJECT_ID=$PROJECT_ID
PROJECT_NUMBER=$PROJECT_NUMBER
SA_NAME=$SA_NAME
SERVICE_ACCOUNT=${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
MODEL="gemini-2.5-flash"
EOF
```
Step 5: Creating the workflow for agent to work --->>
Copy Paste following command in your terminal to create the agent.py file
```bash
import os
from dotenv import load_dotenv
from google.adk import Agent

load_dotenv()
model_name = os.getenv("MODEL", "gemini-2.5-flash")

# 🧠 Summarizer Agent (FIXED - no {text}!)
summarizer_agent = Agent(
    name="text_summarizer",
    model=model_name,
    description="Text summarization specialist",
    instruction="""
You are an expert text summarization assistant.

Your job: Take any input message and summarize it into 2-4 clear sentences.

RULES:
- Capture only MAIN IDEAS
- Remove fluff, examples, repetition  
- Keep original meaning
- Natural, readable output

Always respond with a summary of whatever text the user provides.
    """,
    output_key="summary"
)

# 🚪 Root Agent (routes to summarizer)
root_agent = Agent(
    name="summarizer_root",
    model=model_name,
    description="Text summarization service entry point",
    instruction="""
Welcome to Text Summarizer Pro! 🚀

Send me any text, article, email, or document and I'll summarize it perfectly.

Just paste your text and I'll create a concise 2-4 sentence summary.

Examples of what to summarize:
- News articles
- Research papers  
- Meeting notes
- Long emails

When user sends text → transfer to text_summarizer immediately.
    """,
    sub_agents=[summarizer_agent]
)

__all__ = ["root_agent"]
```
This will finnaly create our main working agent that will perform tasks 

Step 6: Deplyoment --->>
Make sure your file looks like this 
```bash
text_summarizer_agent/
├── .env
├── __init__.py
├── agent.py
└── requirements.txt
```
#Now finnaly deploy your agent using ADK CLI
enter the following command ->>
```bash
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=asia-south1 \
  --service_name=text_summarizer_agent \
  --with_ui \
  . \
  -- \
  --labels=dev-apac-2026-track1-project \
  --service-account=$SERVICE_ACCOUNT
```
Then you will be prompted with 2 new commands just simply type "Y" and press enter after that your deployment process will start.

Last Step : Test the deployed agent 
#Manual Testing Checklist

Agent responds to "Hello" greeting
Long text (500+ words) is summarized to 2-4 sentences
Short text is rephrased concisely
Summary maintains original meaning
Response time < 5 seconds
Invalid input returns appropriate error message

🙏 Credits & References -->><br>
*[Official Documentation](https://google.github.io/adk-docs/)<br>
*[Google Agent Development Kit (ADK) Docs](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview)<br>
*[ADK Cloud Run Deployment Guide](https://google.github.io/adk-docs/deploy/cloud-run/)<br>
*[Gemini API Documentation](https://ai.google.dev/gemini-api/docs)<br>
*[Cloud Run Documentation](https://cloud.google.com/run)<br>

Tutorials & Codelabs -->><br>
*[Build and Deploy ADK Agent on Cloud Run](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/5-deploying-agents/deploy-an-adk-agent-to-cloud-run#0)<br>
*[Building AI Agents with ADK: The Foundation](https://codelabs.developers.google.com/devsite/codelabs/build-agents-with-adk-foundation#9)<br>

#Important -><br>
Gen AI Academy APAC Edition - This project was created as part of the Google Gen AI Academy APAC program
Inspired by Google's best practices for AI agent development and deployment and its a part of module that we have to provide project in order to complete it.

📬 Contact<br>
Author: Om Kartike<br>
Email: omkartikk2910@outlook.com<br>
GitHub: [@omkartike](https://github.com/omkartike)<br>
Location: Delhi,New Delhi,India-110059<br>
Currently: Computer Science Student <br>

Let's Connect!<br>
💼 LinkedIn: [Om Kartike](https://www.linkedin.com/in/om-kartike)<br>
🐙 GitHub: [@omkartike](https://github.com/omkartike)<br>
📧 Email: omkartik2910@gmail.com ---->> alternate email<br>

🎓 Google Gen AI Academy APAC Participant<br>

⭐ Show Your Support<br>
If this project helped you learn about AI agents, ADK, or Cloud Run:<br>
⭐ Star this repository (it helps others find it!)<br>
🍴 Fork it and build your own version<br>
📢 Share it with your network<br>
💬 Leave feedback in the issues section<br>

<div align="center">

Made with ❤️ using Google ADK, Gemini, and Cloud Run<br>
🎓 Part of Google Gen AI Academy APAC Edition 2026<br>

</div>





