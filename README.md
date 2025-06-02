# Langgraph Basics

A simple AI agent framework using LangGraph, Streamlit, and PostgreSQL for persistent memory. This project demonstrates how to build, run, and interact with an agent both via command line and a web interface.

## Features
- In-process agent execution (no external service required)
- Streamlit web chat interface
- Persistent memory using PostgreSQL

## Requirements
- Python 3.11+
- Docker (for PostgreSQL)

## Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd simple-chatbot-with-langgraph
```

### 2. Set up the PostgreSQL database using Docker

Run the following command to start a PostgreSQL instance:

```bash
docker run --name langgraph-postgres 
    -e POSTGRES_USER=postgres 
    -e POSTGRES_PASSWORD=postgres 
    -e POSTGRES_DB=langgraph 
    -p 5432:5432 
    -d postgres:15 
```

This will start a PostgreSQL server accessible at `localhost:5432` with:
- user: `postgres`
- password: `postgres`
- database: `langgraph`

### 3. Install Python dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure environment variables

Edit or create a `.env` file or set the following environment variable as needed:

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/langgraph
```

### 5. Run database migrations (if any)

If your memory module requires migrations, run them here. Otherwise, ensure the tables are created on first run.

### 6. Run the agent via command line

```bash
make run-agent
```

### 7. Run the Streamlit web app

```bash
make run-streamlit
```

Open your browser to the URL shown in the terminal (usually http://localhost:8501).

## Project Structure

```
Basics/
├── src/
│   ├── run_agent.py         # Run the agent from the command line
│   ├── streamlit_app.py     # Streamlit web interface
│   ├── agents/              # Agent logic
│   ├── core/                # Core utilities and config
│   ├── memory/              # Persistent memory (Postgres)
│   └── schemas/             # Data models
├── requirements.txt         # Python dependencies
├── makefile                 # (Optional) Makefile for automation
└── README.md                # This file
```

## Notes
- The agent runs in-process; there is no separate service module.
- Make sure Docker is running before starting the app.
- Stop the PostgreSQL container with `docker stop langgraph-postgres` when done.

## License
MIT
