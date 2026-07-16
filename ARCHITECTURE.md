# 🏛️ PALACE AI - Architecture

## Overview

PALACE AI is the corporate knowledge engine of El Palacio ERP.

Its purpose is to centralize company knowledge, process business documents and answer questions using Artificial Intelligence.

PALACE AI Core must be independent of any interface, AI provider or deployment platform.

---

# Vision

PALACE AI is not a chatbot.

PALACE AI is a Knowledge Management Engine.

The chatbot, Streamlit application, ERP integration or API are only clients that consume the Core.

---

# Project Principles

## 1. Core First

The business logic must always live inside the Core.

Interfaces are replaceable.

---

## 2. Technology Independent

The Core must never depend on:

- OpenAI
- LangChain
- Streamlit
- Oracle
- FAISS
- Chroma
- PostgreSQL

Technologies may change.

The business should not.

---

## 3. Single Responsibility

Every class should have one responsibility.

Examples:

Document → represents a business document.

Chunk → represents a fragment of a document.

KnowledgeBase → manages company knowledge.

---

## 4. Domain Driven

The project is organized around business concepts.

Not around technologies.

Correct:

Document

Chunk

KnowledgeBase

Incorrect:

PdfDocument

OpenAIDocument

FaissDocument

---

## 5. Replaceable Infrastructure

Every external dependency should be replaceable.

Today:

OpenAI

Tomorrow:

Ollama

Nothing inside Core should change.

---

# Architecture

Presentation

↓

Application

↓

Core (Domain)

↓

Infrastructure

---

# Domain

Entities

- Document
- Chunk
- Question
- Answer

Domain Services

- KnowledgeBase

---

# Current Scope (V1)

Supported Areas

- Human Resources
- Accounting

Supported Formats

- PDF
- CSV

---

# Future Scope

Possible future integrations

- ERP
- REST API
- Streamlit
- CLI
- Slack
- Microsoft Teams

Supported formats

- DOCX
- XLSX
- PPTX
- HTML
- JSON
- Markdown

---

# Development Rules

Code language

English

Application language

Spanish

README

Spanish

Commit messages

English

User Interface

Spanish