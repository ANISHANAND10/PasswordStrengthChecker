"""
Simple Cybersecurity Student Project
Project: Password Strength Checker
Run: python app.py
"""

import re
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Password Strength Checker</title>
  <style>
    :root { color-scheme: light; }
    body { font-family: Arial, sans-serif; background:#f3f6fb; margin:0; color:#182230; }
    .wrap { max-width:720px; margin:50px auto; padding:20px; }
    .card { background:white; border-radius:16px; padding:28px; box-shadow:0 8px 28px #172b4d18; }
    h1 { margin-top:0; color:#173b70; }
    p { line-height:1.55; }
    label { display:block; font-weight:bold; margin:18px 0 8px; }
    input[type=password], input[type=text] { width:100%; box-sizing:border-box; padding:12px; border:1px solid #bac5d5; border-radius:8px; font-size:16px; }
    button { margin-top:14px; padding:12px 18px; background:#1769aa; color:white; border:0; border-radius:8px; font-size:16px; cursor:pointer; }
    button:hover { background:#0e4d82; }
    .result { margin-top:22px; padding:16px; border-radius:10px; background:#eef5ff; }
    .strength { font-size:20px; font-weight:bold; }
    .note { color:#536174; font-size:13px; }
    ul { padding-left:22px; }
    .good { color:#176b3a; } .bad { color:#9d2b2b; }
    footer { margin-top:18px; color:#6b7280; font-size:13px; }
  </style>
</head>
<body>
<div class="wrap">
  <div class="card">
    <h1>🔐 Password Strength Checker</h1>
    <p>A small cybersecurity awareness project that checks basic password characteristics and gives improvement tips.</p>
    <form method="post">
      <label for="password">Enter a sample password</label>
      <input id="password" name="password" type="password" required minlength="1" autocomplete="off"
             placeholder="Type a password to check">
      <button type="submit">Check Strength</button>
    </form>
    {% if result %}
      <div class="result">
        <div class="strength">Result: {{ result.level }}</div>
        <p>{{ result.summary }}</p>
        <p><strong>Score:</strong> {{ result.score }}/5</p>
        <strong>Checks</strong>
        <ul>
        {% for item in result.checks %}
          <li class="{{ 'good' if item[0] else 'bad' }}">{{ '✓' if item[0] else '✗' }} {{ item[1] }}</li>
        {% endfor %}
        </ul>
        <strong>Suggestions</strong>
        <ul>{% for tip in result.tips %}<li>{{ tip }}</li>{% endfor %}</ul>
      </div>
    {% endif %}
    <footer>Privacy note: this demo does not save passwords. For safety, use a made-up sample password, not a password you use for a real account.</footer>
  </div>
</div>
</body>
</html>
"""

def check_password(password: str) -> dict:
    checks = [
        (len(password) >= 12, "At least 12 characters"),
        (bool(re.search(r"[a-z]", password)), "Contains a lowercase letter"),
        (bool(re.search(r"[A-Z]", password)), "Contains an uppercase letter"),
        (bool(re.search(r"\d", password)), "Contains a number"),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Contains a symbol"),
    ]
    score = sum(ok for ok, _ in checks)
    if score <= 2:
        level, summary = "Weak", "This password misses several recommended characteristics."
    elif score <= 4:
        level, summary = "Moderate", "This password meets some recommendations; consider improving it."
    else:
        level, summary = "Strong by basic checks", "It meets all five basic checks, but this is not a guarantee of security."
    tips = [label + "." for ok, label in checks if not ok]
    if not tips:
        tips = ["Prefer a long, unique passphrase and never reuse passwords."]
    return {"score": score, "level": level, "summary": summary, "checks": checks, "tips": tips}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form.get("password", "")
        # The password is processed only in memory for this request; it is not stored.
        result = check_password(password)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=False)
