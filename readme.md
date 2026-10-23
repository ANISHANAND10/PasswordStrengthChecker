# Cybersecurity Student Project: Password Strength Checker

A small web app built with Python and Flask. It checks basic password characteristics and displays suggestions.

## Files
- `app.py` — the complete application
- `requirement.txt` — Python dependency list (as requested)
- `readme.md` — this guide
- `Project_Report.docx` — project report

## Requirements
- Python 3.10 or newer
- Internet connection only if Flask needs to be installed

## Run on Windows
1. Install Python from https://www.python.org/downloads/ and select **Add Python to PATH** during setup.
2. Open Command Prompt in this project folder.
3. (Optional, recommended) Create a virtual environment:
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install the dependency:
   ```bat
   python -m pip install -r requirement.txt
   ```
5. Start the app:
   ```bat
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.
7. Press `Ctrl+C` in the terminal to stop the server.

## How to test
Use a made-up sample password. Try examples such as `hello`, `Welcome123`, and `River!Stone2026`. Do not enter a password that you use for a real account.

## How it works
The app checks five simple characteristics: 12+ characters, lowercase, uppercase, number, and symbol. Each satisfied check adds one point. Scores 0–2 are marked Weak, 3–4 Moderate, and 5 Strong by basic checks.

## Limitations
- This is an educational demo, not a professional password auditing tool.
- It does not check breached-password databases, estimate entropy, or assess password reuse.
- A high score does not guarantee a password is secure.
- The app does not save the password, but it is still best to use only made-up test values.
- For a real deployment, use production security settings, HTTPS, and appropriate server configuration.

## Suggested project title
**Cybersecurity Awareness Tool: Password Strength Checker**
