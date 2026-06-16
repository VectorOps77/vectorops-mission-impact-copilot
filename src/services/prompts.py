def story_prompt(user_input: str) -> str:
    return f"""
Create an outcome-based project story from the following input:

{user_input}

Return the response in this exact format:

## Story Title
A clear title for the project story.

## Problem Statement
Describe the client or mission problem being solved.

## Intended Outcome
Describe what success looks like and what improves.

## Suggested KPIs
List 3 measurable KPIs that align to the problem and intended outcome.

## Quality Notes
Explain whether the story is outcome-focused and leadership-ready.

Rules:
- Focus on mission impact.
- Avoid vague task-only language.
- Do not invent specific metrics unless clearly labeled as assumptions.
- Make the language professional and executive-ready.
"""


def kpi_prompt(user_input: str) -> str:
    return f"""
Build a measurable KPI from this idea:

{user_input}

Return the response in this exact format:

## KPI Name
## Reference
Examples: User Time Saved, Cost Avoidance, Accuracy, Customer Satisfaction, Rework Rate

## Baseline
Current state before improvement.

## Basis of Estimate
Where the baseline came from.

## Target
Desired future state.

## Unit of Measure
Examples: hours, dollars, percent, count.

## Calculation
Formula or method for calculating the KPI.

## How This Helps the Client
Explain the business or mission value.

Rules:
- KPI must be measurable.
- KPI must connect to a clear problem.
- Do not invent hard numbers unless clearly labeled as assumptions.
"""


def monthly_update_prompt(user_input: str) -> str:
    return f"""
Convert these raw monthly notes into a professional MSR-style update:

{user_input}

Return the response in this exact format:

## Solution Delivered
What work was completed this month?

## Outcome Achieved
What changed, improved, or moved forward because of the work?

## Customer Feedback
Only include feedback if it was provided. Otherwise say: Not provided.

## Risks / Issues
List risks, issues, or blockers.

## Action Items
Create a table with: Action Item | Owner | Due Date

## Suggested KPI Updates
Recommend measurable values that should be tracked.

Rules:
- Use outcome-focused language.
- Do not exaggerate.
- Do not invent customer feedback.
- If data is missing, recommend what should be tracked.
"""


def quality_check_prompt(user_input: str) -> str:
    return f"""
Review this project reporting content:

{user_input}

Evaluate it using this structure:

## Alignment Score
Score from 1 to 5.

## Activity-Focused Issues
Identify anything that sounds like task reporting instead of outcome reporting.

## Missing Metrics
Identify missing measurable data.

## Recommended Rewrite
Rewrite the content to be clearer, measurable, and leadership-ready.

## Final Readiness Decision
Ready / Needs Revision

Rules:
- Be direct.
- Do not rewrite with fake metrics.
- Clearly explain what would make the content stronger.
"""