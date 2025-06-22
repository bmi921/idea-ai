"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
idea_generator = LlmAgent(
    name="InitialPostGenerator",
    model=GEMINI_MODEL,
    instruction="""
    あなたはユーザーから単語を受け取り、連想してアイデアを考えるAIエージェントです。
    必ず、一つのアイデアを生成してください。簡潔に一文でアイデアの内容をまとめてください。
    新規性のあるもので、なるべく面白いアイデアを考えてください。
    
    ## STYLE REQUIREMENTS
    - NO emojis
    - NO hashtags
    
    ## OUTPUT INSTRUCTIONS
    - Return ONLY the idea content
    - Do not add formatting markers or explanations
    
    """,
    description="Generates the initial LinkedIn post to start the refinement process",
    output_key="current_post",
)
