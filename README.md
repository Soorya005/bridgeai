# BridgeAI

BridgeAI is a hybrid knowledge assistant project with two services:

1. **LLaMA Service** – A local LLaMA model that responds to queries.  
2. **MCP Gateway** – A FastAPI/Flask API that forwards queries to LLaMA and returns responses.

Both services are containerized using Docker and orchestrated via Docker Compose.

---

## 🛠 Prerequisites

- [Docker](https://www.docker.com/get-started) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) installed  
- Git (to clone the repo)

---

## 📥 Setup

Clone the repository:

```bash
git clone https://github.com/Soorya005/bridgeai.git
cd bridgeai
🚀 Running the project

Start the services using Docker Compose:

docker-compose up -d


This will:

Build the Docker images for both services (if not already built)

Start the llama-service and mcp-gateway containers

Connect both services on the same Docker network automatically

Check running containers:

docker ps

💬 Testing the MCP Gateway

Send a query to the MCP Gateway:

curl "http://localhost:8000/ask?query=Hello"


Expected response:

{
  "query": "Hello",
  "llama_response": {
    "message": "LLaMA model response!"
  }
}

⚙️ Docker Compose

Your docker-compose.yml should look like this:

version: "3.8"
services:
  llama-service:
    build: ./llama-service
    container_name: llama-service
    ports:
      - "5000:5000"

  mcp-gateway:
    build: ./mcp-gateway
    container_name: mcp-gateway
    ports:
      - "8000:8000"
    depends_on:
      - llama-service

📌 Notes

Make sure ports 5000 and 8000 are free on your machine.

Flask is used for MCP Gateway (development server). For production, consider using gunicorn or uvicorn.

Queries sent to MCP Gateway are forwarded to the LLaMA service automatically.

👥 Team Collaboration

Pull the latest changes before starting work:

git pull origin main


Push your changes to a feature branch and create a Pull Request (PR) for review.

✅ Status

LLaMA service ✅

MCP Gateway ✅

Docker Compose integration ✅
