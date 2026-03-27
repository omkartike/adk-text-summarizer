# adk-text-summarizer
Text summarization AI agent built with Google ADK + Gemini 2.5 Flash for Gen AI Academy APAC. Deployed on Cloud Run with HTTP API &amp; web UI. Simple, scalable, production-ready. Made with ❤️ for learning and showcasing modern AI deployment patterns!



🤖 Text Summarization AI Agent (ADK + Gemini + Cloud Run)
<div align="center">

A production-ready AI agent built with Google's Agent Development Kit (ADK) that performs text summarization using Gemini, deployed on Google Cloud Run with an HTTP endpoint.

🎓 Gen AI Academy APAC Edition Project Submission
⭐ Showcased on GitHub for portfolio purposes

</div>

📖 Table of Contents
Overview
Features
Architecture
Tech Stack
Project Structure
Prerequisites
Installation & Setup
Deployment Steps
How to Use
Testing
API Documentation
Screenshots
Troubleshooting
Future Enhancements
Credits & References
License
Contact

🎯 Overview
This project demonstrates the implementation of a single AI agent using Google's Agent Development Kit (ADK) that performs text summarization using the Gemini 2.5 Flash model. The agent is deployed on Google Cloud Run and is callable via an HTTP endpoint, returning valid responses for given text inputs.

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
🧠 AI-Powered Summarization: Automatically condenses long text into concise, readable summaries

⚡ Fast Response: Uses Gemini 2.5 Flash for minimal latency

🌐 Serverless Deployment: Hosted on Google Cloud Run with auto-scaling

🔌 HTTP REST API: Callable via standard HTTP POST requests

🖥️ Built-in Web UI: Includes ADK developer interface for easy testing

🔐 Secure: Uses Google Cloud IAM and service accounts

📦 Production-Ready: Containerized with Docker and proper IAM permissions

🎓 Educational: Perfect for learning ADK, Cloud Run, and AI agent architecture

🏗️ Architecture
┌─────────────────┐     HTTP Request     ┌──────────────────┐
│                 │  ──────────────────> │                  │
│   Client /      │                      │   Google Cloud   │
│   Browser       │  <─────────────────  │      Run         │
│                 │     JSON Response    │  (ADK Agent)     │
└─────────────────┘                      └────────┬─────────┘
                                                 │
                                                 │ API Call
                                                 │
                                          ┌──────▼───────┐
                                          │              │
                                          │   Gemini     │
                                          │  2.5 Flash   │
                                          │   (Vertex AI)│
                                          │              │
                                          └──────────────┘
Flow Description-

1) User sends HTTP POST request with text to summarize
2)Cloud Run receives request and routes to ADK agent
3)Agent processes text using Gemini model
4)Summary is returned as JSON response

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

📁 Project Structure -
text_summarizer_agent/
├── .env                      # Environment variables (API key, model)
├── requirements.txt          # Python dependencies
├── agent.py                  # Main ADK agent definition
├── __init__.py              # Python package initializer
└── Dockerfile               # Container configuration (optional)
File Descriptions ->
| File             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| agent.py         | Defines the text summarization agent with Gemini model and instructions |
| requirements.txt | Lists Python dependencies (google-adk, python-dotenv)                   |
| .env             | Stores API keys and configuration (DO NOT commit to git)                |
| Dockerfile       | Container definition for Cloud Run deployment                           |
| __init__.py      | Makes the directory a Python package                                    |

📋 Prerequisites
Before running this project, ensure you have:

Required Accounts & Services
✅ Google Account (personal, not work/school)

✅ Google Cloud Project with billing enabled

✅ Google Cloud SDK (gcloud) installed on your machine

✅ Python 3.11+ installed

Now lets come to the commands section ->>>

Enable Required APIs
bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com

  🚀 Installation & Setup
Step 1: Clone the Repository
bash
git clone https://github.com/your-username/text-summarizer-agent.git
cd text-summarizer-agent
