import sys
import requests

ASANA_TOKEN = "YOUR_ASANA_TOKEN_HERE"
PROJECT_ID = "1214271683377823"

HEADERS = {"Authorization": f"Bearer {ASANA_TOKEN}"}
BASE_URL = "https://app.asana.com/api/1.0"

def list_tasks():
    url = f"{BASE_URL}/projects/{PROJECT_ID}/tasks"
    params = {"opt_fields": "name,completed,memberships.section.name"}
    response = requests.get(url, headers=HEADERS, params=params)
    tasks = response.json()["data"]
    for task in tasks:
        section = ""
        if task.get("memberships"):
            section = task["memberships"][0]["section"]["name"]
        status = "✅" if task["completed"] else "⬜"
        print(f"{status} [{section}] {task['name']} (ID: {task['gid']})")

def move_task(task_id, section_name):
    url = f"{BASE_URL}/projects/{PROJECT_ID}/sections"
    response = requests.get(url, headers=HEADERS)
    sections = response.json()["data"]
    target_section = None
    for section in sections:
        if section_name.lower() in section["name"].lower():
            target_section = section
            break
    if not target_section:
        print(f"Bölüm bulunamadı: {section_name}")
        print("Mevcut bölümler:")
        for s in sections:
            print(f"  - {s['name']}")
        return
    url = f"{BASE_URL}/sections/{target_section['gid']}/addTask"
    requests.post(url, headers=HEADERS, json={"data": {"task": task_id}})
    print(f"Task {task_id} -> '{target_section['name']}' bölümüne taşındı!")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        list_tasks()
    elif sys.argv[1] == "move" and len(sys.argv) == 4:
        move_task(sys.argv[2], sys.argv[3])
    else:
        print("Kullanım:")
        print("  python asana_cli.py                    # Tüm taskları listele")
        print("  python asana_cli.py move <id> <bölüm> # Task taşı")
