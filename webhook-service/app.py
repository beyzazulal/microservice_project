from flask import Flask, jsonify, request
import requests
import re
import os

app = Flask(__name__)

JIRA_DOMAIN    = os.getenv("JIRA_DOMAIN", "beyzazulalodabasi.atlassian.net")
JIRA_EMAIL     = os.getenv("JIRA_EMAIL",  "rumeysasemiz11@gmail.com")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
NOTIFICATION_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8080")

TICKET_PATTERN = re.compile(r'(?:Fixes|Closes|Resolves)\s+([A-Z]+-\d+)', re.IGNORECASE)

def close_jira_ticket(issue_key):
    auth    = (JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {"Content-Type": "application/json"}
    url     = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}/transitions"

    resp = requests.get(url, auth=auth, headers=headers, timeout=5)
    if resp.status_code != 200:
        return False, f"Transitions alinamadi: {resp.status_code}"

    transitions = resp.json().get("transitions", [])
    transition_names = [t["name"] for t in transitions]

    done_keywords = ["done", "tamamlandi", "tamamlandı", "closed", "resolved", "complete", "bitti", "kapandi", "tamam"]
    done_id = None
    for t in transitions:
        if any(kw in t["name"].lower() for kw in done_keywords):
            done_id = t["id"]
            break

    if not done_id:
        return False, f"Done transition bulunamadi. Mevcut: {transition_names}"

    resp = requests.post(url, json={"transition": {"id": done_id}}, auth=auth, headers=headers, timeout=5)
    if resp.status_code == 204:
        return True, "Ticket kapatildi"
    return False, f"Transition hatasi: {resp.status_code}"

def send_notification(message):
    try:
        requests.post(f"{NOTIFICATION_URL}/api/notify", json={"message": message}, timeout=5)
    except Exception:
        pass

@app.route("/webhook", methods=["POST"])
def gitea_webhook():
    data = request.get_json()
    if not data or "commits" not in data:
        return jsonify({"error": "Gecersiz payload"}), 400

    results = []
    for commit in data["commits"]:
        message = commit.get("message", "")
        for issue_key in TICKET_PATTERN.findall(message):
            success, info = close_jira_ticket(issue_key)
            results.append({"issue": issue_key, "success": success})
            if success:
                send_notification(f"Ticket {issue_key} otomatik kapatildi!\nCommit: {message[:80]}")
            else:
                send_notification(f"UYARI: {issue_key} kapatılamadi - {info}")

    return jsonify({"processed": results})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "webhook-service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
