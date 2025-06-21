#!/usr/bin/env python3
import json
from datetime import datetime
import os

def save_conversation(messages, project_name):
    """Save conversation for later reference"""
    os.makedirs("conversations", exist_ok=True)
    
    filename = f"conversations/{project_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "project": project_name,
            "messages": messages
        }, f, indent=2)
    
    print(f"Conversation saved: {filename}")

def load_latest_conversation(project_name):
    """Load most recent conversation for a project"""
    conversations = [f for f in os.listdir("conversations") 
                    if f.startswith(project_name) and f.endswith('.json')]
    
    if conversations:
        latest = sorted(conversations)[-1]
        with open(f"conversations/{latest}", 'r') as f:
            return json.load(f)
    return None