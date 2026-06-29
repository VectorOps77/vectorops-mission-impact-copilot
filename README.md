![CI - Quality and Security](https://github.com/VectorOps77/vectorops-mission-impact-copilot/actions/workflows/ci.yml/badge.svg)

# VectorOps Mission Impact Copilot

VectorOps Mission Impact Copilot is an AI-powered project management assistant built with Python, Streamlit, and the OpenAI API. The application helps technical project managers convert raw project notes into structured, leadership-ready content such as project stories, KPI summaries, monthly updates, quality reviews, and downloadable Word documents.

This project is part of my DevSecOps and LLM portfolio. It demonstrates practical use of AI, secure API key handling, document generation, GitHub version control, and the foundation for future Azure deployment.

---

## Problem Statement

Project managers often collect updates from emails, meetings, spreadsheets, dashboards, and stakeholder conversations. These updates are usually unstructured and require manual rewriting before they are ready for leadership reports, monthly status reports, or client-facing communication.

This creates several challenges:

* Inconsistent reporting language
* Manual rework
* Weak connection between work performed and business outcomes
* Limited visibility into risks, blockers, and measurable impact
* Time-consuming document preparation

---

## Solution

VectorOps Mission Impact Copilot uses AI to convert raw project notes into structured, outcome-focused content. The application helps users generate:

* Project stories
* KPI summaries
* Monthly status updates
* Risk and issue summaries
* Quality and alignment reviews
* Downloadable Word documents

The goal is to reduce manual reporting effort while improving clarity, consistency, and executive readiness.

---

## Key Features

### Story Creation Assistant

Generates an outcome-based project story from raw project ideas or problem statements.

Output includes:

* Story title
* Problem statement
* Intended outcome
* Suggested KPIs
* Quality notes

### KPI Builder

Helps convert KPI ideas into measurable performance indicators.

Output includes:

* KPI name
* Reference category
* Baseline
* Target
* Unit of measure
* Calculation
* Client benefit

### Monthly Update Assistant

Converts raw monthly notes into structured MSR-style content.

Output includes:

* Solution delivered
* Outcome achieved
* Customer feedback
* Risks/issues
* Action items
* Suggested KPI updates

### Quality & Alignment Checker

Reviews draft content for quality, clarity, and measurable outcomes.

Output includes:

* Alignment score
* Activity-focused issues
* Missing metrics
* Recommended rewrite
* Final readiness decision

### Document Generator

Creates downloadable Word documents from generated AI content using `python-docx`.

Supported outputs include:

* MSR drafts
* Project stories
* KPI reports
* Quality reviews
* Executive briefs
* Status reports
* Meeting summaries

---

## Tech Stack

* Python
* Streamlit
* OpenAI API
* python-dotenv
* python-docx
* Pydantic
* Git/GitHub

Planned DevSecOps tools:

* GitHub Actions
* Ruff
* Pytest
* Bandit
* pip-audit
* Docker
* Trivy
* Azure App Service or Azure Container Apps
* Azure Key Vault
* Terraform

---

## Security Practices

This project uses secure environment variable handling.

The real OpenAI API key is stored in a local `.env` file:

```env
OPENAI_API_KEY=your_real_api_key_here
MODEL_NAME=gpt-4.1-mini
```

The `.env` file is excluded from GitHub using `.gitignore`.

The repository includes a safe `.env.example` file:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4.1-mini
```

Security controls planned for the pipeline:

* Secret scanning
* Dependency vulnerability scanning
* Static code analysis
* Container vulnerability scanning
* Secure deployment using Azure Key Vault

---

## Project Structure

```text
vectorops-mission-impact-copilot/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── src/
│   ├── llm/
│   │   └── client.py
│   ├── services/
│   │   ├── prompts.py
│   │   └── document_service.py
│   ├── models/
│   └── utils/
├── sample_data/
├── tests/
└── docs/
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/VectorOps77/vectorops-mission-impact-copilot.git
cd vectorops-mission-impact-copilot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Create a `.env` file

```bash
touch .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_real_api_key_here
MODEL_NAME=gpt-4.1-mini
```

### 5. Run the app

```bash
python3 -m streamlit run app.py
```

---

## Sample Use Case

Input:

```text
Project reporting is currently manual and inconsistent. Team members submit updates in different formats, making it difficult for leadership to understand project health, risks, and measurable outcomes.
```

Generated output may include:

* Executive summary
* Project health assessment
* Risks and issues
* Action items
* Suggested KPIs
* Downloadable Word document

---

## DevSecOps Roadmap

### Phase 1: CI/CD Foundation

* Add GitHub Actions workflow
* Run linting with Ruff
* Run tests with Pytest
* Run security scan with Bandit
* Run dependency scan with pip-audit

### Phase 2: Containerization

* Add Dockerfile
* Build container image
* Scan image with Trivy
* Prepare for Azure deployment

### Phase 3: Azure Deployment

* Deploy app to Azure App Service or Azure Container Apps
* Store secrets in Azure Key Vault
* Configure environment variables securely

### Phase 4: Infrastructure as Code

* Create Terraform configuration
* Provision Azure resources
* Add Terraform validation and security scanning

### Phase 5: Expanded AI Studio

Future versions will include:

* Prompt library
* Schema library
* Multiple document templates
* GitHub portfolio artifact generator
* Azure architecture summary generator
* DevSecOps pipeline report generator

---

## Portfolio Goals

This project demonstrates:

* LLM application development
* Streamlit app development
* OpenAI API integration
* Secure API key management
* Word document generation
* GitHub version control
* DevSecOps pipeline planning
* Technical project management automation
* Azure deployment readiness

---

## Disclaimer

This project uses fictional and sanitized sample data only. It does not include proprietary, client-sensitive, government-sensitive, or employer-owned data.

All AI-generated content should be reviewed by a human before being used in any official report or client-facing document.

---

## Author

Aaron Thomas
VectorOps LLC
