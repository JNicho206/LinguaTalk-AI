#!/bin/bash

# Create directories
mkdir -p app/models app/routes app/services app/templates app/static/css app/static/js app/static/img app/utils app/tests venv

# Create __init__.py files for making directories as Python packages
touch app/__init__.py app/models/__init__.py app/routes/__init__.py app/services/__init__.py app/utils/__init__.py app/tests/__init__.py

# Create Python files for models, routes, services, and utilities
touch app/models/user.py app/routes/main.py app/routes/api.py app/services/speech_recognition.py app/utils/helpers.py app/tests/test_routes.py

# Create basic HTML template and static files
echo "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Language Learning App</title></head><body><h1>Welcome to the Language Learning App</h1></body></html>" > app/templates/index.html
touch app/static/css/style.css
touch app/static/js/script.js

# Create project files
echo "Flask==2.0.1" > requirements.txt  # Example, you can specify your required versions
touch config.py
echo "SECRET_KEY=your_secret_key_here" > .env
echo "*.pyc" > .gitignore
echo "/venv/" >> .gitignore
echo "/.env" >> .gitignore

# Create the main application file and README
echo "from flask import Flask" > run.py
echo "app = Flask(__name__)" >> run.py
echo "@app.route('/')" >> run.py
echo "def index():" >> run.py
echo "    return 'Hello, World!'" >> run.py
echo "if __name__ == '__main__':" >> run.py
echo "    app.run(debug=True)" >> run.py

echo "# Language Learning App" > README.md
echo "This is a language learning application developed using Flask." >> README.md
echo "" >> README.md
echo "## Setup" >> README.md
echo "Instructions to set up and run the application." >> README.md
