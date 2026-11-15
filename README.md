# MCP Server Examples — Calculator & Weather

A small collection of **Model Context Protocol (MCP)** server examples built with [FastMCP](https://github.com/jlowin/fastmcp). The repository demonstrates how Python functions can be exposed as tools over HTTP, with request logging and an external API integration.

## Included servers

| Server | Port | MCP tool | What it does |
|---|---:|---|---|
| Calculator | `8001` | `add_numbers` | Adds two numbers |
| Calculator | `8001` | `divide_numbers` | Divides one number by another |
| Weather | `8002` | `get_temperature` | Looks up a place and returns the remaining hourly temperature forecast for today |

The weather server uses the public [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) and [Forecast API](https://open-meteo.com/en/docs). No API key is configured in this project for those calls; an internet connection is required.

## Requirements

- Python 3.13
- pip
- Internet access for the weather example

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/erfantk25-lab/nackademin-mcp-demo.git
cd nackademin-mcp-demo

python3.13 -m venv .venv
```

Activate it and install the dependencies.

**macOS / Linux**
```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Windows PowerShell**
```powershell
.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the servers

Start each server in a separate terminal from the repository root, with the virtual environment activated.

**Terminal 1 — Calculator**
```bash
python -m calculator_mcp.calculator_mcp
``

The calculator MCP endpoint is available at `http://127.0.0.1:8001/mcp`.

**Terminal 2 — Weather**
```bash
python -m weather_mcp.weather_server
``

The weather MCP endpoint is available at `http://127.0.0.1:8002/mcp`.

Keep both terminals running while connecting an MCP-compatible client.

## Example tool calls

Use an MCP-compatible client to call the tools:

- `add_numbers(a=12, b=5)` → `17`
- `divide_numbers(a=10, b=2)` → `5`
- `get_temperature(location="Stockholm")` → place details and hourly temperatures in °C for the rest of the current day

The weather response uses the `Europe/Stockholm` timezone. If a place cannot be resolved, the tool returns an error message in its response.

## Project structure

```text
.
├── calculator_mcp/
│   └── calculator_mcp.py       # Calculator MCP server
├── weather_mcp/
│   ├── weather_server.py       # Weather MCP server and tool definition
│   └── weather_client.py       # Open-Meteo geocoding and forecast requests
├── config/
│   ├── custom_logging_config.py
│   └── logging_config.py
├── requirements.txt
└── README.md
```

Both servers attach the shared request-logging middleware from `config/`.

## Verification and current scope

This repository currently documents manual end-to-end verification through an MCP client; it does not include an automated test suite. A useful next improvement would be unit tests for the calculator tools and mocked HTTP tests for the weather client.

The examples are intended for local development and learning. Do not expose the servers to an untrusted network without adding appropriate authentication, access controls, and deployment hardening.
