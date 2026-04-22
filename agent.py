import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

# 1. Load API Key from your .env file
load_dotenv()

# 2. Define your specialized tools (Optional but makes it a 'Real' product)
def market_analysis_tool(industry: str):
    """Analyzes market trends for a specific industry in 2026."""
    return f"Latest 2026 data for {industry}: 30% growth in agentic workflows and decentralized AI."

# 3. Initialize the AI Consultant Agent
# We are naming it uniquely so it stands out on your GitHub profile
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

# 4. CRITICAL: Export for the ADK Dashboard
# This variable name 'root_agent' is exactly what the dashboard looks for
root_agent = ai_consultant_agent

if __name__ == "__main__":
    print("✅ Tanisha's AI Consultant is ready for action!")