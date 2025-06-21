# Claude Code Project Template

## ⚡ Why This Template Matters

**This template provides the backbone for any project where Claude Code will be a contributor.** Since Claude doesn't remember what has been done after each session ends, this setup allows you to continue exactly where you left off with Claude by maintaining project context and ensuring session continuity.

### The Problem
- Claude Code sessions are stateless—no memory between conversations
- Project context is lost when starting new sessions
- Repetitive explanations of project structure and goals are required
- Development momentum is lost between sessions

### The Solution
This template solves these issues by providing:
- **CLAUDE.md**: Maintains persistent project context and status
- **Session Management**: Scripts to restore and continue previous work
- **Automated Setup**: Consistent project initialization
- **Context Preservation**: Clear documentation of current state and next steps

---

## How to start and continue with Claude

- Open terminal 
- Run `claude` and send prompt `Read and follow CLAUDE.md instructions`
- For new session (When continuing a project), Prompt Read `.cloude/session_template.md`
- Proceed with your project tasks

---

A comprehensive template repository for Claude Code projects with pre-configured scripts, templates, and development tools.

## 🚀 Features

- **CLAUDE.md Template**: Pre-configured project context file with system prompts and project structure
- **Initialization Script**: Automated setup for Python virtual environment and Git repository
- **Utility Scripts**: Helper scripts for conversations, session management, and screenshots
- **Template Files**: Ready-to-use templates for common project files

## 📁 Structure

```
Claude-Code-Project-template/
├── CLAUDE.md              # Main project context file for Claude Code
├── init.sh                # Project initialization script
├── scripts/               # Utility scripts
│   ├── conversations.py   # Conversation management tools
│   ├── restore_session.py # Session restoration utilities
│   └── screenshot.py      # Screenshot automation
└── templates/             # Template files
    ├── README.md          # Project README template
    └── requirements.txt   # Python dependencies template
```

## 🛠 Quick Start

1. **Use this template** by clicking the "Use this template" button on GitHub
2. **Clone your new repository**:
   ```bash
   git clone https://github.com/yourusername/your-project-name.git
   cd your-project-name
   ```
3. **Run the initialization script**:
   ```bash
   chmod +x init.sh
   ./init.sh
   ```
4. **Customize CLAUDE.md** with your project-specific information
5. **Start coding with Claude Code**!

## 📝 Configuration

### CLAUDE.md
This is the main configuration file for Claude Code projects. Customize it with:
- Your project name and description
- System prompts and requirements
- Project structure documentation
- Current status and next steps

### Initialization Script
The `init.sh` script automatically:
- Creates a Python virtual environment
- Installs dependencies from requirements.txt
- Initializes a Git repository
- Creates an initial commit

## 🔧 Utility Scripts

- **conversations.py**: Tools for managing Claude Code conversations
- **restore_session.py**: Utilities for restoring previous sessions
- **screenshot.py**: Automated screenshot functionality for web development

## 📋 Templates

The `templates/` directory contains starter files:
- `README.md`: Project documentation template
- `requirements.txt`: Python dependencies template

## 🎯 Best Practices

When using this template with Claude Code:
1. Keep CLAUDE.md updated with project progress
2. Use descriptive commit messages
3. Leverage the utility scripts for session management
4. Maintain clean project structure
5. Document your development process

## 🤝 Contributing

Feel free to submit issues and pull requests to improve this template.

## 📄 License

This template is provided as-is for use with Claude Code projects.

---

**Generated with Claude Code** 🤖