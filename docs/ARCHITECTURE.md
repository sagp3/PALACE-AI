# PALACE AI Architecture

## Vision

PALACE AI is a corporate knowledge engine.

Its goal is not to manage documents.

Its goal is to transform business documents into searchable organizational knowledge.

---

# Main Components

## Document Engine

Responsible for document ingestion.

Responsibilities:

- Receive new documents
- Detect changes
- Validate files
- Coordinate processing

---

## Document Repository

Responsible for document persistence.

Responsibilities:

- Register documents
- Version documents
- Detect duplicates
- Keep latest version

---

## Chunk Engine

Responsible for splitting documents.

Responsibilities:

- Chunk generation
- Metadata attribution
- Chunk validation

---

## Embedding Engine

Responsible for vector generation.

Responsibilities:

- Generate embeddings
- Batch processing
- Reindexing

---

## Knowledge Base

Stores searchable knowledge.

---

## Retrieval Engine

Searches relevant chunks.

---

## LLM Engine

Generates answers using retrieved context.

---

## Query Engine

Coordinates the question-answer flow.

---

# Public API

Only one class should be exposed to external systems.

```
PalaceAI
```

Everything else remains internal.
