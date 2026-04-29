# Microservice Project — Group 10

A microservice-based software development infrastructure built with Python (Flask), C# (.NET 10), and Docker. The system includes three application services orchestrated via Docker Compose, integrated with a full DevOps toolchain.

---

## Services

| Service | Language | Port | Description |
|---|---|---|---|
| User Service | Python / Flask | 5001 | CRUD API for user management |
| Order Service | Python / Flask | 5002 | Order management with user validation |
| Notification Service | C# / .NET 10 | 5003 | Sends alerts to Slack via Incoming Webhook |

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 4.x or later
- [Git](https://git-scm.com/)
- [.NET 10 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) (for Notification Service)
- Python 3.11+ (optional — for `asana_cli.py`)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/beyzazulal/microservice_project.git
cd microservice_project
```

### 2. Start all services

```bash
docker compose up -d --build
```

### 3. Verify services are running

```
GET http://localhost:5001/health   →  { "status": "ok", "service": "user-service" }
GET http://localhost:5002/health   →  { "status": "ok", "service": "order-service" }
```

### 4. Stop all services

```bash
docker compose down
```

---

## API Reference

### User Service — `localhost:5001`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get a user by ID |
| POST | `/users` | Create a user (`name`, `email` required) |
| PUT | `/users/<id>` | Update a user |
| DELETE | `/users/<id>` | Delete a user |
| GET | `/health` | Health check |

### Order Service — `localhost:5002`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/orders` | Get all orders |
| GET | `/orders/<id>` | Get an order by ID |
| POST | `/orders` | Create an order (`user_id`, `product` required) |
| PUT | `/orders/<id>/status` | Update order status |
| DELETE | `/orders/<id>` | Delete an order |
| GET | `/health` | Health check |

### Notification Service — `localhost:5003`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/notify` | Send a message to Slack (`message` required) |

---

## Quick Test

```bash
# Create a user
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"Beyza\", \"email\": \"beyza@test.com\"}"

# Create an order
curl -X POST http://localhost:5002/orders \
  -H "Content-Type: application/json" \
  -d "{\"user_id\": 1, \"product\": \"Laptop\"}"

# Send a Slack notification
curl -X POST http://localhost:5003/api/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Order created successfully!\"}"
```

---

## Project Structure

```
microservice_project/
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── order-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── NotificationService/
│   └── NotificationService/
│       ├── Program.cs
│       ├── NotificationService.csproj
│       └── Dockerfile
├── docker-compose.yml
├── asana_cli.py
└── README.md
```

---

## DevOps Toolchain

| Tool | Purpose |
|---|---|
| Jira | Kanban board — task tracking with GitHub integration |
| Confluence | Technical documentation linked to Jira tickets |
| Slack | Team communication + automated push notifications |
| Asana | Supplementary task management via REST API |
| Gitea | Self-hosted Git platform (~100 MB RAM) |
| GitHub | Cloud version control with Jira Smart Commits |

---

## Asana CLI (Optional)

```bash
pip install requests
python asana_cli.py                           # List all tasks
python asana_cli.py move <task_id> <section>  # Move a task to a section
```

---

## Team

**Beyza Zülal Odabaşı · Rumeysa Semiz** — Group 10


