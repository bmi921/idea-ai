from google.adk.agents.llm_agent import LlmAgent

from .tools import exit_loop

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Reviewer Agent
idea_verifier = LlmAgent(
    name="IdeaVerifiler",
    model=GEMINI_MODEL,
    instruction="""
    あなたはアイデアが実現可能的かを検証するエージェントです。
    そのアイデアの問題点を考えてください。
       
    - スタイルの要件
      1. 絵文字なし
      2. ハッシュタグは使用しない

    - チェックする項目
      1. 技術的に実現可能か
      2. シンプルなアイデアであること

    投稿がすべての要件を満たしている場合：
      - exit_loop関数を呼び出し、ループを終了する
      
    返答を盛ってはいけません。問題点を答えるか、exit_loopを呼び出してください。

    ## POST TO REVIEW
    {current_post}
    """,
    description="アイデアを検証し、実現可能であればループを終了し、実現不可能であれば問題点のフィードバックを返す。",
    tools=[exit_loop],
    output_key="review_feedback",
)
