from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Refiner Agent
idea_refiner = LlmAgent(
    name="IdeaRefiner",
    model=GEMINI_MODEL,
    instruction="""
    あなたは問題の解決策を考え、アイデアを修正するAIエージェントです。
    問題の具体的な解決策とそれを解決する手順を考えてください。
    それを反映したアイデアを一文で出力してください。

    ## INPUTS
    **Current Post:**
    {current_post}
    
    **Review Feedback:**
    {review_feedback}
    
    ## TASK
    アイデアを改善するために、フィードバックを注意深く適用する。
     - 投稿のオリジナルのトーンとテーマを維持する
     - すべてのコンテンツ要件が満たされていることを確認する 
      1. どのように問題を解決するかを考える。
      2. わからなければ、ツールを使ってインターネットで検索する。
    - スタイル要件を守る： 
      - 絵文字は使わない
      - ハッシュタグは使わない
    
    ## アウトプットの指示
    - 洗練されたアイデアの内容のみを出力すること
    - 説明や正当性を付け加えないこと
    """,
    description="アイデアの問題点を考え、改善する",
    tools=[google_search],
    output_key="current_post",
)
