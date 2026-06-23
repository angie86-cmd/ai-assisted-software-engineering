# SMID Compass – AI-Assisted Requirements Engineering Case Study

## Overview

This case study demonstrates an AI-Assisted Requirements Engineering workflow applied to the SMID Compass platform.

The objective was to explore how Large Language Models (LLMs) can support the generation of structured requirements for an AI-powered multi-agent system while maintaining human review and governance.

The case study was inspired by practical experience with AI-assisted requirements generation and adapted to a public, reproducible example based on the SMID Compass project.

---

## About SMID Compass

SMID Compass is an AI-powered guidance platform developed by Save My Identity (SMID).

The platform supports people facing identity-document challenges by providing structured informational guidance and educational resources.

The current concept is based on a multi-agent architecture consisting of:

- Router Agent
- Passport Guidance Agent
- Workshop Advisor Agent
- Safety Agent

The system is intended to provide informational guidance while respecting privacy, transparency and human-rights principles.

---

## Objectives

This case study demonstrates:

- AI-Assisted Requirements Engineering
- Prompt Engineering
- Grounding
- Context Engineering
- Human-in-the-Loop Validation
- Multi-Agent Systems Engineering
- AI Governance Considerations

---

## Project Structure

```text
smid-compass-requirements/
├── README.md
├── system-description.md
├── generation-prompt.md
├── generated-requirements.md
└── grounding/
    ├── smid-public-context.md
    ├── smid-faq-context.md
    ├── smid-workshops-context.md
    └── passport-guidance-context.md
```

---

## Workflow

The requirements generation process followed these steps:

### 1. System Definition

A high-level system description was created describing:

- Purpose
- Users
- Multi-agent architecture
- Constraints
- Knowledge sources

### 2. Grounding

Project-specific context was provided through grounding documents covering:

- SMID organizational context
- Frequently asked questions
- Workshop information
- Passport guidance information

### 3. Requirements Generation

An AI system was instructed to act as a Senior Requirements Engineer and generate requirements using:

- Role Prompting
- Grounding
- Context Engineering
- Requirements Engineering principles

### 4. Human Review

Generated requirements were reviewed and refined to ensure:

- Consistency
- Clarity
- Governance alignment
- Privacy considerations
- Organizational relevance

---

## Generated Requirement Categories

The generated requirements cover:

- Functional Requirements
- Non-Functional Requirements
- Security Requirements
- Privacy Requirements
- AI Governance Requirements
- Multi-Agent Requirements
- Evaluation and Human Review Requirements

---

## Key Learnings

This exercise demonstrates that LLMs can accelerate the creation of an initial requirements baseline when provided with:

- Clear objectives
- Domain-specific context
- Grounding documentation
- Explicit quality criteria

The quality of the generated requirements depended more on the provided context and knowledge sources than on complex prompt wording alone.

This observation aligns with modern approaches such as Context Engineering and Agent Systems Engineering.

---

## Current Scope

This repository represents a prototype and educational case study.

The generated requirements are intended for exploration and discussion purposes and do not constitute a finalized system specification.

---

## Future Enhancements

Potential future extensions include:

- GDPR Compliance Requirements
- EU AI Act Considerations
- Human Oversight Procedures
- Agent Evaluation Frameworks
- Agent Observability Requirements
- Security Threat Modeling
- Risk Management Requirements
- Knowledge Base Governance
- Multi-language Support

---

## Relation to Modern AI Engineering

This project demonstrates the evolution from traditional Prompt Engineering toward:

- Context Engineering
- Grounding
- AI-Assisted Requirements Engineering
- Agent Systems Engineering

Rather than relying solely on prompt wording, the project uses domain knowledge, structured context and human review to improve the quality and reliability of generated requirements.

---

## Disclaimer

This project is an educational and demonstrational case study.

It is not intended to provide legal advice, migration advice or official procedural guidance.

Users should always verify relevant information through official and authoritative sources.