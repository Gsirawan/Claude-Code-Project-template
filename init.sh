#!/bin/bash

# Exit on any error
set -e

echo "🌀 Creating Python virtual environment..."
python -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip
# pip install (more libs) and it will be saved in req.txt after.
pip install -r requirements.txt

echo "{^_^} Save requirements..."
# Save requirements
pip freeze > requirements.txt

echo "🌱 Initializing Git repository..."
git init
git add .
git commit -m "Initial setup from base template"

echo "🚀 Setup complete."
