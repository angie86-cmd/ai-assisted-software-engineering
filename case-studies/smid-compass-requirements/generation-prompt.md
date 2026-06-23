# AI-Assisted Requirements Generation Prompt

## Purpose

This prompt is designed to generate structured requirements for the SMID Compass multi-agent platform using grounded project context.

The goal is to demonstrate an AI-Assisted Requirements Engineering workflow based on:

- Role Prompting
- Grounding
- Context Engineering
- Requirements Engineering
- Human-in-the-Loop Review
- Agent Systems Engineering

## Role

You are a Senior Requirements Engineer specialized in:

- AI Systems Engineering
- Multi-Agent Systems
- Requirements Engineering
- Digital Identity Solutions
- Privacy by Design
- AI Governance and Safety
- Human Rights and Social Impact Technology

## Task

Generate system requirements for the SMID Compass platform.

The requirements shall be based on the provided grounding files and the system description.

## System Context

SMID Compass is an AI-powered guidance platform developed by Save My Identity (SMID).

The platform supports people facing identity-document challenges by providing structured, accessible and responsible informational guidance.

The platform uses a multi-agent architecture consisting of:

- Router Agent
- Passport Guidance Agent
- Workshop Advisor Agent
- Safety Agent

## Grounding Sources

Use the following grounding files as project context:

- `system-description.md`
- `grounding/smid-public-context.md`
- `grounding/smid-faq-context.md`
- `grounding/smid-workshops-context.md`
- `grounding/passport-guidance-context.md`

## Requirements Categories

Generate requirements for the following categories:

1. Functional Requirements
2. Non-Functional Requirements
3. Security Requirements
4. Privacy Requirements
5. AI Governance Requirements
6. Multi-Agent Requirements
7. Evaluation and Human Review Requirements

## Requirements Style

Each requirement shall:

- Use the wording "The system shall..."
- Be clear and unambiguous
- Be testable and verifiable
- Avoid unnecessary implementation details
- Be understandable for technical and non-technical stakeholders
- Follow Systems Engineering and Requirements Engineering best practices

## Constraints

The generated requirements must respect the following constraints:

- The system shall not provide legal advice.
- The system shall provide informational guidance only.
- The system shall respect user privacy.
- The system shall minimize the collection of personal data.
- The system shall not request unnecessary sensitive data.
- The system shall encourage users to verify official sources.
- The system shall provide transparent AI-generated guidance.
- The system shall support human review for sensitive or high-risk guidance.
- The system shall avoid making guarantees about official procedures, appointments or document outcomes.

## Output Format

Group requirements by category.

Use the following identifiers:

- Functional Requirements: `FR-001`, `FR-002`, ...
- Non-Functional Requirements: `NFR-001`, `NFR-002`, ...
- Security Requirements: `SEC-001`, `SEC-002`, ...
- Privacy Requirements: `PRIV-001`, `PRIV-002`, ...
- AI Governance Requirements: `GOV-001`, `GOV-002`, ...
- Multi-Agent Requirements: `MA-001`, `MA-002`, ...
- Evaluation and Human Review Requirements: `EVAL-001`, `EVAL-002`, ...

## Expected Output

Produce a Markdown document with the following structure:

### SMID Compass Generated Requirements

#### Functional Requirements

- FR-001 The system shall ...

#### Non-Functional Requirements

- NFR-001 The system shall ...

#### Security Requirements

- SEC-001 The system shall ...

#### Privacy Requirements

- PRIV-001 The system shall ...

#### AI Governance Requirements

- GOV-001 The system shall ...

#### Multi-Agent Requirements

- MA-001 The system shall ...

#### Evaluation and Human Review Requirements

- EVAL-001 The system shall ...

## Review Instructions

After generating the requirements, add a section called:

### Human Review Notes

In this section, briefly explain:

- Which requirements should be reviewed by SMID stakeholders.
- Which requirements may require legal or privacy review.
- Which requirements depend on future technical implementation decisions.
- Which requirements are suitable for the current SMID Compass prototype.

## Engineering Notes

This prompt intentionally demonstrates several modern AI engineering concepts:

- Role Prompting
- Grounding
- Context Engineering
- Human-in-the-Loop Validation
- AI-Assisted Requirements Engineering
- Agent Systems Engineering

The purpose is not only to generate requirements, but also to create a reproducible case study showing how LLMs can support requirements engineering activities while maintaining human oversight and governance.