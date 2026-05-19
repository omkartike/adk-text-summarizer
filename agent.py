#Copy the following code and paste it in your agent.py file

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
