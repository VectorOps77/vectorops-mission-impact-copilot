# Architecture Overview

## System Purpose

VectorOps Mission Impact Copilot is an AI-powered Technical PM assistant that helps convert raw project notes into structured project stories, KPI summaries, monthly updates, quality reviews, and downloadable Word documents.

## High-Level Architecture

```text
User
 ↓
Streamlit Web App
 ↓
OpenAI API
 ↓
AI-generated PM content
 ↓
Document Generator
 ↓
Downloadable Word document

