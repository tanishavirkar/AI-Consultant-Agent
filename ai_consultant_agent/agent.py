import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

load_dotenv()

def market_analysis_tool(industry: str):
    """Analyzes market trends for a specific industry in 2026."""
    return f"Latest 2026 data for {industry}: 30% growth in agentic workflows and decentralized AI."

ai_consultant_agent = LlmAgent(
    name="Nova_Consultant_Pro",
    model="gemini-2.5-flash",
    instruction="""
    You are an elite AI Strategy and Research Consultant. 
    Your persona is professional, data-driven, and highly intelligent. 
    You were developed by Tanisha, an AI researcher, to help navigate 
    complex business and technical landscapes.
    
    Specialties:
    - Deep Learning & Computer Vision (YOLO/GAN) pipelines.
    - AI Startup Market Entry Strategies.
    - Federated Learning and Model Evaluation (ML Playground).
    
    Response Style:
    - Always provide a structured 3-step execution plan.
    - Use technical terminology where appropriate.
    - Be concise yet visionary.
    """,
    description="Professional AI Research and Business Strategy Agent.",
    tools=[market_analysis_tool]
)

root_agent = ai_consultant_agenta

if __name__ == "__main__":
    print("✅ Tanisha's AI Consultant is ready for action!")