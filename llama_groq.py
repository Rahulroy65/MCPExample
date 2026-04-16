# llama_groq.py

import os
import requests
import json

GROQ_API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def llama_reply(user_input, tools):
    tool_descriptions = "\n".join([f"- {t}" for t in tools])

    # Prompt telling the LLAma model about tool availability
    prompt = f"""
You are a smart assistant with access to the following tools:
{tool_descriptions}

When the user asks something that requires a tool, respond in JSON:
{{"type":"tool_call","tool":"TOOL_NAME","arguments":{{}}}}

Otherwise, respond as regular JSON:
{{"type":"message","content":"TEXT"}}

User: {user_input}
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile", 
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }

    resp = requests.post(API_URL, headers=headers, json=payload)

    text = ""
    if resp.status_code == 200:
        data = resp.json()
        # Extract text from the model's response
        text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    else:
        text = f"Error: {resp.text}"

    try:
        # Try to parse as JSON output
        return json.loads(text)
    except Exception:
        # Fallback to message if JSON fails
        return {"type": "message", "content": text}
