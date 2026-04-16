# mcp_server.py
from tools import add_numbers, multiply_numbers  # import your tool functions


class MCPServer:
    def __init__(self):
        self.tools = {
            "add_numbers": add_numbers,
            "multiply_numbers": multiply_numbers
        }

    def call_tool(self, name, args):
        if name not in self.tools:
            raise Exception(f"Tool '{name}' not allowed")
        return self.tools[name](**args)
