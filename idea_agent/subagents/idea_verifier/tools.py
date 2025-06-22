from typing import Any, Dict

from google.adk.tools.tool_context import ToolContext


def exit_loop(tool_context: ToolContext) -> Dict[str, Any]:
    """
    アイデアが条件を満たした時のみ呼ばれる関数です。
    ループを終了します。

    Args:
        tool_context: Context for tool execution

    Returns:
        Empty dictionary
    """
    print("\n----------- LOOP 終了条件が達成された -----------")
    print("アイデアが実現可能的であり、ループ終了すると判断されました。")
    print("ループから抜けます。")
    print("------------------------------------------\n")

    tool_context.actions.escalate = True
    return {}
