# Deployment Guide

## Project

VectorOps Mission Impact Copilot is deployed as a Dockerized Streamlit application using Azure Container Apps.

## Deployment Flow

1. Code is pushed to GitHub.
2. GitHub Actions runs quality and security checks.
3. Docker image is built.
4. Trivy scans the container image.
5. Image is pushed to Azure Container Registry.
6. Azure Container App is updated with the latest image.

## Azure Resources

- Resource Group: `rg-vectorops-copilot-dev`
- Azure Container Registry: `vectoropscopilotacr`
- Azure Container Apps Environment: `vectorops-copilot-env`
- Azure Container App: `vectorops-mission-impact-copilot`

## Security Controls

- OpenAI API key is stored as an Azure Container App secret.
- `.env` file is excluded from GitHub.
- GitHub Actions uses repository secrets for Azure authentication.
- Ruff checks code quality.
- Bandit scans Python security issues.
- pip-audit scans Python dependencies.
- Trivy scans the Docker image for HIGH and CRITICAL vulnerabilities.

## Deployment Command Summary

Manual deployment was first completed using Docker and Azure CLI. The project was then upgraded to automated deployment through GitHub Actions.

## Validation

The app was tested successfully in Azure using the public Azure Container Apps URL.
