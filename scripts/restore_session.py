#!/usr/bin/env python3
"""Restore and manage Claude Code session state."""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

class SessionManager:
    def __init__(self):
        self.state_file = ".claude/session_state.json"
        self.conversations_dir = "conversations"
        
    def save_state(self, state_data):
        """Save current session state."""
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        
        state = {
            "timestamp": datetime.now().isoformat(),
            "working_directory": os.getcwd(),
            "active_files": state_data.get("active_files", []),
            "last_command": state_data.get("last_command", ""),
            "todos": state_data.get("todos", []),
            "current_task": state_data.get("current_task", ""),
            "context": state_data.get("context", {})
        }
        
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def restore_state(self):
        """Restore previous session state."""
        if not os.path.exists(self.state_file):
            print("No previous session found.")
            return None
            
        with open(self.state_file, 'r') as f:
            state = json.load(f)
        
        print("=== Previous Session State ===")
        print(f"Last active: {state['timestamp']}")
        print(f"Working directory: {state['working_directory']}")
        print(f"Current task: {state['current_task']}")
        
        if state['active_files']:
            print("\nActive files:")
            for file in state['active_files']:
                print(f"  - {file}")
        
        if state['todos']:
            print("\nTODOs:")
            for todo in state['todos']:
                print(f"  - {todo}")
        
        # Show git status
        print("\n=== Current Git Status ===")
        subprocess.run(["git", "status", "--short"])
        
        # Show recent commits
        print("\n=== Recent Commits ===")
        subprocess.run(["git", "log", "--oneline", "-5"])
        
        return state
    
    def get_project_summary(self):
        """Generate a comprehensive project summary."""
        summary = []
        
        # Check for README
        if os.path.exists("README.md"):
            with open("README.md", 'r') as f:
                lines = f.readlines()[:10]  # First 10 lines
                summary.append("=== Project README ===")
                summary.extend(lines)
        
        # Check current branch
        branch = subprocess.check_output(
            ["git", "branch", "--show-current"], 
            text=True
        ).strip()
        summary.append(f"\nCurrent branch: {branch}")
        
        # Check for uncommitted changes
        status = subprocess.check_output(
            ["git", "status", "--porcelain"], 
            text=True
        )
        if status:
            summary.append("\nUncommitted changes detected!")
        
        # Check test status
        if os.path.exists("tests/"):
            test_files = list(Path("tests/").glob("test_*.py"))
            summary.append(f"\nTest files found: {len(test_files)}")
        
        return "\n".join(summary)

if __name__ == "__main__":
    sm = SessionManager()
    state = sm.restore_state()
    
    if state:
        print("\n" + sm.get_project_summary())
        print("\n=== Ready to Continue ===")
        print("Claude Code has loaded the previous session context.")