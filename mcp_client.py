# mcp_client.py
class MCPClient:
    def __init__(self, server):
        self.server = server

    def run_tool(self, tool_name, arguments):
        return self.server.call_tool(tool_name, arguments)
