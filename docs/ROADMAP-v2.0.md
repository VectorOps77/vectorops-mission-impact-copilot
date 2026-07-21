# VectorOps Mission Impact Copilot — v2.0.0 Roadmap

**Target release:** August 25, 2026  
**Release branch strategy:** feature branches into `main` through pull requests  
**Primary goal:** evolve the current Streamlit MVP into a cleaner, tested, secure, and deployable VectorOps AI Studio foundation.

---

## 1. Release Objective

Version `v2.0.0` will stabilize the application architecture, formalize reusable document templates, improve testing and security gates, and prepare the project for staged Azure deployment with rollback procedures.

The release focuses on making the app easier to maintain, easier to extend, and stronger as a GitHub portfolio project for AI, DevSecOps, cloud deployment, and technical program management.

---

## 2. Current Baseline

The current application includes:

- Streamlit UI
- OpenAI integration
- Prompt library
- Schema library
- Word document generation using `python-docx`
- Docker containerization
- GitHub Actions CI/CD
- Ruff linting
- Bandit security scanning
- `pip-audit` dependency scanning
- Pytest unit tests
- Trivy container scanning
- Azure Container Registry deployment
- Azure Container Apps hosting
- Initial selectable document template system

Because the live repository files were not available when this roadmap was written, Milestone M0 must verify the actual `main` branch before refactoring begins.

---

## 3. Six-Week Release Plan

### Week 1 — M0: Baseline Verification and Roadmap PR

**Goal:** Confirm the repository state and commit the v2.0 roadmap before making code changes.

**Work items:**

- Pull latest `main`
- Run the app locally
- Confirm current tabs and document generation behavior
- Confirm CI/CD workflow status
- Confirm Azure deployment is still live
- Commit this roadmap into `docs/ROADMAP-v2.0.md`
- Open the `docs/v2-roadmap` pull request

**Acceptance criteria:**

- Roadmap exists in `/docs`
- Documentation PR is reviewed and merged
- Current app behavior is documented before refactor work starts

---

### Week 2 — M1: Shared Template Registry

**Goal:** Replace scattered template definitions with a shared versioned template registry.

**Work items:**

- Create a template registry module
- Add template IDs, names, descriptions, sections, styles, and versions
- Add validation for required template fields
- Connect AI Studio and Document Generator to the same registry
- Preserve current template behavior while cleaning the structure

**Acceptance criteria:**

- Five versioned templates are available through one registry
- Streamlit dropdowns pull from the registry
- Document Generator uses the same template definitions as AI Studio
- Unit tests validate the registry

---

### Week 3 — M2: Architecture Refactor

**Goal:** Move business logic out of `app.py` and into service modules.

**Target architecture:**

```text
app.py
src/
├── config/
│   ├── prompt_library.py
│   ├── schema_library.py
│   └── template_registry.py
├── llm/
│   ├── client.py
│   └── providers.py
├── services/
│   ├── prompt_service.py
│   ├── template_service.py
│   ├── document_service.py
│   └── export_service.py
├── exporters/
│   ├── docx_exporter.py
│   ├── pdf_exporter.py
│   └── pptx_exporter.py
└── tests/
```

**Work items:**

- Keep `app.py` focused on UI orchestration
- Move prompt construction into a prompt service
- Move template handling into a template service
- Move document/export logic into exporter modules
- Add provider abstraction for LLM calls

**Acceptance criteria:**

- `app.py` is smaller and easier to read
- Core logic is testable outside Streamlit
- Existing features still work after refactor
- Unit tests cover the refactored services

---

### Week 4 — M3: Testing and AI Evaluation Gates

**Goal:** Raise confidence in the application before adding more features.

**Work items:**

- Add unit tests for template registry
- Add unit tests for prompt construction
- Add tests for document generation
- Add integration test for prompt + template workflow
- Add lightweight AI evaluation tests for required sections, non-invention behavior, and output completeness
- Enforce 80% coverage gate

**Acceptance criteria:**

- Pytest passes locally
- CI enforces test execution
- Coverage gate is configured at 80%
- AI evaluation checks validate required output sections

---

### Week 5 — M4: DevSecOps Hardening

**Goal:** Strengthen the pipeline with security, supply chain, and provenance checks.

**Work items:**

- Generate SBOM for application dependencies
- Maintain AI inventory documentation
- Confirm Bandit security scan
- Confirm `pip-audit` dependency scan
- Confirm Trivy container scan
- Add build provenance / artifact attestation workflow where supported
- Document security controls in `/docs/SECURITY.md`

**Acceptance criteria:**

- SBOM artifact is generated in CI
- Security scans run on pull requests or release builds
- AI inventory documents models, environment variables, and data handling assumptions
- Build provenance milestone is documented and implemented where practical

---

### Week 6 — M5: Staged Azure Deployment, Smoke Tests, and Release Tag

**Goal:** Prepare a professional release flow with validation and rollback.

**Work items:**

- Add staged deployment plan
- Add smoke test checklist
- Add rollback procedure
- Confirm Azure Container App deployment flow
- Tag release as `v2.0.0`
- Update deployment guide and lessons learned

**Acceptance criteria:**

- Smoke test checklist exists
- Rollback guide exists
- Azure deployment is validated after release
- GitHub release tag `v2.0.0` is created

---

## 4. Versioned Templates

The v2.0 release should include five stable, versioned templates using a shared registry.

### Template 1 — Executive Brief v1

**Use case:** Leadership-ready summary of a project, risk, deployment, or milestone.

**Sections:**

- Executive Summary
- Key Accomplishments
- Current Status
- Risks / Issues
- Recommended Next Steps

---

### Template 2 — MSR Report v1

**Use case:** Monthly status reporting.

**Sections:**

- Reporting Period
- Summary of Work Completed
- Outcomes Achieved
- Risks / Issues
- Next Month Priorities

---

### Template 3 — Technical Report v1

**Use case:** Technical implementation or architecture write-up.

**Sections:**

- Overview
- Technical Approach
- System Components
- Security Considerations
- Operational Impact
- Next Steps

---

### Template 4 — KPI Report v1

**Use case:** Measurable performance reporting.

**Sections:**

- KPI Name
- Purpose
- Measurement Method
- Target / Benchmark
- Client Benefit
- Reporting Frequency

---

### Template 5 — DevSecOps Report v1

**Use case:** CI/CD, security scanning, cloud deployment, and pipeline documentation.

**Sections:**

- Pipeline Overview
- Security Controls
- Testing Gates
- Deployment Flow
- Findings / Risks
- Recommended Improvements

---

## 5. Target Application Architecture

The v2.0 architecture should separate responsibilities clearly.

```text
Streamlit UI
   ↓
Prompt Service
   ↓
Template Service
   ↓
LLM Provider
   ↓
Export Service
   ↓
DOCX / PDF / PPTX output
```

### Streamlit UI

Responsible for:

- Tabs
- User input
- Dropdowns
- Buttons
- Displaying output
- Download controls

### Prompt Service

Responsible for:

- Combining user notes, prompt instructions, and selected template sections
- Preventing unsupported facts or invented metrics
- Formatting model instructions consistently

### Template Service

Responsible for:

- Loading templates
- Validating required fields
- Returning selected template sections
- Supporting future template versions

### LLM Provider

Responsible for:

- OpenAI client calls
- Provider abstraction
- Error handling
- Future local or Azure OpenAI support

### Export Service

Responsible for:

- Generating downloadable files
- Routing output to DOCX, PDF, PPTX, or Excel exporters
- Keeping export logic outside Streamlit

---

## 6. GitHub Issues

### Issue 1 — Add v2.0 Roadmap

**Acceptance criteria:**

- `docs/ROADMAP-v2.0.md` exists
- Roadmap includes milestones, issues, testing, security, deployment, and rollback plan
- PR is documentation-only

---

### Issue 2 — Verify Current Main Branch Baseline

**Acceptance criteria:**

- App runs locally from `main`
- Existing tabs are documented
- Existing CI status is captured
- Azure app status is verified

---

### Issue 3 — Create Shared Template Registry

**Acceptance criteria:**

- Template registry exists under `src/config`
- Templates include ID, name, description, sections, style, and version
- Unit tests validate required fields

---

### Issue 4 — Connect AI Studio to Template Registry

**Acceptance criteria:**

- AI Studio template dropdown uses shared registry
- Prompt output reflects selected template sections
- Model instructions prevent invented facts or metrics

---

### Issue 5 — Connect Document Generator to Template Registry

**Acceptance criteria:**

- Document Generator template dropdown uses shared registry
- DOCX output uses selected template sections
- Existing document generation still works

---

### Issue 6 — Refactor Prompt Logic into Service Layer

**Acceptance criteria:**

- Prompt construction moves out of `app.py`
- Prompt service has unit tests
- Streamlit UI only passes selected inputs to the service

---

### Issue 7 — Refactor Export Logic

**Acceptance criteria:**

- Export logic is separated from Streamlit UI
- DOCX export is handled through exporter module
- Tests confirm exported files are created successfully

---

### Issue 8 — Add Provider Abstraction

**Acceptance criteria:**

- OpenAI logic is wrapped in provider module
- Provider errors are handled cleanly
- Future provider support is documented

---

### Issue 9 — Add AI Evaluation Tests

**Acceptance criteria:**

- Tests confirm required sections appear in generated outputs
- Tests check that missing metrics are not invented
- Tests validate basic completeness and formatting

---

### Issue 10 — Enforce Coverage Gate

**Acceptance criteria:**

- Test coverage reporting is added
- CI fails below 80% coverage
- Coverage output is available in CI logs

---

### Issue 11 — Add SBOM and AI Inventory

**Acceptance criteria:**

- SBOM generated during CI or release workflow
- AI inventory document exists
- Security documentation includes model, data, secrets, and deployment notes

---

### Issue 12 — Add Smoke Test and Rollback Documentation

**Acceptance criteria:**

- Smoke test checklist exists
- Rollback guide exists
- Release validation steps are documented
- Deployment guide references rollback process

---

## 7. Testing Strategy

### Unit Tests

Targets:

- Template registry
- Prompt service
- Template service
- Export service
- LLM provider wrapper

### Integration Tests

Targets:

- Prompt + template workflow
- Template + DOCX export workflow
- Application configuration loading

### AI Evaluation Tests

Targets:

- Required section presence
- No invented metrics
- No unsupported assumptions
- Output completeness
- Basic leadership-ready formatting

### Coverage Gate

Target:

```text
Minimum coverage: 80%
```

---

## 8. DevSecOps Requirements

The pipeline should include:

```text
GitHub push / pull request
   ↓
Ruff linting
   ↓
Bandit security scan
   ↓
pip-audit dependency scan
   ↓
Pytest unit and integration tests
   ↓
Coverage gate
   ↓
SBOM generation
   ↓
Docker build
   ↓
Trivy container scan
   ↓
Build provenance / artifact attestation
   ↓
Push image to Azure Container Registry
   ↓
Deploy to Azure Container Apps
   ↓
Smoke test
```

---

## 9. AI Inventory

The project should document:

- Model provider
- Model name
- Environment variables
- Secrets storage location
- Data sent to the model
- Data not allowed in prompts
- Human review requirements
- Known limitations
- Prompt templates
- Output validation approach

---

## 10. Deployment Plan

### Azure Resources

```text
Resource Group:
rg-vectorops-copilot-dev

Azure Container Registry:
vectoropscopilotacr

Container Apps Environment:
vectorops-copilot-env

Container App:
vectorops-mission-impact-copilot

Application Port:
8501
```

### Deployment Flow

```text
Merge to main
   ↓
GitHub Actions workflow starts
   ↓
Tests and scans run
   ↓
Docker image builds
   ↓
Container image is scanned
   ↓
Image is pushed to Azure Container Registry
   ↓
Azure Container App is updated
   ↓
Smoke test confirms app availability
```

---

## 11. Smoke Test Checklist

After deployment, validate:

- App loads successfully
- Story Assistant tab opens
- KPI Builder tab opens
- Monthly Update Assistant tab opens
- Quality Checker tab opens
- Document Generator tab opens
- AI Studio tab opens
- AI Studio can generate output
- Document Generator can create a Word file
- No secrets appear in logs
- Azure Container App revision is healthy

---

## 12. Rollback Plan

If deployment fails:

1. Identify the last healthy Azure Container App revision
2. Re-route traffic to the last healthy revision
3. Confirm app loads successfully
4. Open a GitHub issue documenting the failed release
5. Revert the faulty commit or open a hotfix branch
6. Re-run CI/CD after the fix
7. Document the incident in lessons learned

---

## 13. Documentation Updates

The following docs should exist or be updated:

```text
docs/ARCHITECTURE.md
docs/DEPLOYMENT_GUIDE.md
docs/LESSONS_LEARNED.md
docs/ROADMAP-v2.0.md
docs/SECURITY.md
docs/AI_INVENTORY.md
docs/ROLLBACK.md
```

---

## 14. Immediate Branch and PR Scope

### Branch

```bash
git checkout main
git pull origin main
git checkout -b docs/v2-roadmap
```

### Files

```text
docs/ROADMAP-v2.0.md
```

### Commit Message

```bash
git add docs/ROADMAP-v2.0.md
git commit -m "docs: add v2.0 release roadmap"
git push -u origin docs/v2-roadmap
```

### Pull Request Title

```text
docs: add VectorOps Mission Impact Copilot v2.0 roadmap
```

### Pull Request Summary

```text
Adds the v2.0 roadmap for VectorOps Mission Impact Copilot, including the six-week release plan, shared template registry, target architecture, GitHub-ready issues, testing gates, DevSecOps milestones, Azure deployment validation, smoke testing, and rollback documentation.
```

### Pull Request Validation

```text
Documentation-only change. No application behavior changed.
```

---

## 15. Definition of Done for v2.0.0

Version `v2.0.0` is complete when:

- Shared template registry is implemented
- Five versioned templates are available
- AI Studio and Document Generator use the same template system
- Core logic is moved out of `app.py`
- Unit and integration tests pass
- AI evaluation tests are included
- 80% test coverage gate is active
- SBOM and AI inventory are documented
- Container scanning is active
- Build provenance milestone is addressed
- Azure deployment is staged and validated
- Smoke test checklist passes
- Rollback process is documented
- Release is tagged as `v2.0.0`

---

## 16. Strategic Outcome

This release turns VectorOps Mission Impact Copilot from a working MVP into a stronger reusable platform foundation.

The result should demonstrate:

- AI product development
- Streamlit application architecture
- Prompt and template engineering
- Secure DevSecOps practices
- GitHub Actions CI/CD
- Azure container deployment
- Documentation discipline
- Technical program management maturity

This is the release where the app stops being “just a cool project” and starts looking like a real product foundation. Clean architecture, clean pipeline, clean receipts.
