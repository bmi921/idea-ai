from google.adk.agents import LoopAgent, SequentialAgent

from .subagents.idea_generator import idea_generator
from .subagents.idea_refiner import idea_refiner
from .subagents.idea_verifier import idea_verifier

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="PostRefinementLoop",
    max_iterations=10,
    sub_agents=[
        idea_verifier,
        idea_refiner
    ],
    description="Iteratively reviews and refines a LinkedIn post until quality requirements are met",
)

# Create the Sequential Pipeline
root_agent = SequentialAgent(
    name="IdeaAgent",
    sub_agents=[
        idea_generator,  # Step 1: Generate initial post
        refinement_loop,  # Step 2: Review and refine in a loop
    ],
    description="ユーザーから単語を受け取りアイデアを考える。その後、問題と解決策をループして考える。",
)
