import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

load_dotenv()

def ai_market_insight(topic: str):
    """Fetches specialized 2026 AI trends for a specific topic."""
    return f"In 2026, {topic} is pivoting toward autonomous agentic reasoning and edge-deployment."


my_agent = LlmAgent(
    name="Nova_Consultant_Pro",
    model="gemini-2.5-flash",
    instruction="""
    You are 'Nova Consultant Pro', an elite AI Research and Strategy agent.
    You were developed by Tanisha, an M.Tech AI student and researcher.
    
    Your expertise includes:
    - Computer Vision pipelines (specifically YOLOv8/v10 and GAN-based enhancement).
    - Deep Learning research and Federated Learning strategies.
    - AI-driven business startup consulting.

    Persona:
    - Be professional, structured, and highly technical.
    - Always provide a 3-step action plan for any strategy request.
    - If asked about your origin, mention you are a specialized product of Tanisha's AI Research Suite.
    """,
    description="Professional AI Strategy Agent specializing in Deep Learning and Business.",
    tools=[ai_market_insight]
)


root_agent = my_agent

if __name__ == "__main__":
    print("🚀 Nova Consultant Pro is live and initialized!")
    print("Run 'adk web .' in your terminal to chat with me in the browser.")