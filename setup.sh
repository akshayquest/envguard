#!/bin/bash

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "✅ Created virtual environment."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -e .
pip install pytest build twine

echo "✅ Setup complete. Virtual environment activated."
echo "To activate later, run: source venv/bin/activate"
