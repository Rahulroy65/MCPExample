from mcp_server import MCPServer
from mcp_client import MCPClient
from llama_groq import llama_reply  # <-- This replaces Claude

def main():
    server = MCPServer()
    client = MCPClient(server)

    tools = ["add_numbers", "multiply_numbers"]  # List of available MCP tools

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Call your LLaMA-based function
        response = llama_reply(user_input, tools)

        # Check if LLaMA wants to call a tool
        if response.get("type") == "tool_call":
            result = client.run_tool(
                response["tool"],
                response.get("arguments", {})
            )
            print("LLaMA:", result)
        else:
            print("LLaMA:", response.get("content"))

if __name__ == "__main__":
    main()
