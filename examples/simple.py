"""
Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
"""

from dotenv import load_dotenv

from browser_use import Agent, ChatGoogle

load_dotenv()

agent = Agent(
	task='Find the number of total number of stars present in the pinned project github.com/ash310u',
    llm=ChatGoogle(model='gemini-flash-latest'),
)
agent.run_sync()
