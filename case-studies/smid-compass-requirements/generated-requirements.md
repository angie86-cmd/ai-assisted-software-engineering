### SMID Compass Generated Requirements

#### Functional Requirements

- FR-001 The system shall provide structured informational guidance to users facing identity-document challenges.
- FR-002 The system shall support users including stateless persons, refugees, migrants, NGOs, volunteers and community organizations.
- FR-003 The system shall provide general passport and identity-document guidance based on available SMID knowledge sources.
- FR-004 The system shall provide general orientation about Venezuelan passport processes, including SAIME-related steps, without guaranteeing outcomes.
- FR-005 The system shall inform users that passport procedures depend on official rules, location, applicant status and consular availability.
- FR-006 The system shall encourage users to verify current passport, migration and consular information through official sources.
- FR-007 The system shall provide workshop-related information, including topics, registration guidance, access expectations and certification criteria.
- FR-008 The system shall help users identify relevant workshop topics based on their stated interests and needs.
- FR-009 The system shall clearly state that SMID provides educational information, general guidance and verified resources rather than legal advice or legal representation.
- FR-010 The system shall recommend professional legal advice or official institutional support when a user appears to need individualized legal assistance.

#### Non-Functional Requirements

- NFR-001 The system shall present guidance in language that is understandable to both technical and non-technical users.
- NFR-002 The system shall provide responses that are accessible, respectful and appropriate for users in vulnerable documentation, migration or displacement contexts.
- NFR-003 The system shall maintain consistent disclaimers that its guidance is informational and AI-generated.
- NFR-004 The system shall provide responses that are concise enough for practical use while preserving essential cautions and next steps.
- NFR-005 The system shall support reliable routing of user requests to the appropriate specialized agent.
- NFR-006 The system shall be designed to support future updates to official-source references, workshop information and SMID guidance materials.
- NFR-007 The system shall avoid making definitive claims about changing official procedures unless supported by reviewed and current knowledge sources.

#### Security Requirements

- SEC-001 The system shall warn users not to share account credentials, passwords or SAIME login information with third parties.
- SEC-002 The system shall warn users about unofficial intermediaries, fraudulent promises and paid services that claim to guarantee official outcomes.
- SEC-003 The system shall not request payment card data, account passwords, government portal credentials or other unnecessary sensitive security information.
- SEC-004 The system shall protect any user-provided information from unauthorized access according to the platform security controls selected for implementation.
- SEC-005 The system shall restrict administrative access to configuration, grounding sources and safety controls to authorized maintainers.
- SEC-006 The system shall log safety-relevant system events in a way that supports review without exposing unnecessary personal data.

#### Privacy Requirements

- PRIV-001 The system shall minimize the collection of personal data during user interactions.
- PRIV-002 The system shall not request unnecessary sensitive personal data, including identity numbers, passport numbers, full document images or account credentials.
- PRIV-003 The system shall allow users to receive general guidance without providing identifying personal details whenever possible.
- PRIV-004 The system shall inform users when personal information is not needed to answer a general guidance question.
- PRIV-005 The system shall process user information according to privacy-by-design principles.
- PRIV-006 The system shall avoid storing sensitive personal data unless storage is explicitly required, justified and approved by SMID stakeholders.
- PRIV-007 The system shall support deletion, retention and access-control policies for user interaction data according to future SMID privacy decisions.

#### AI Governance Requirements

- GOV-001 The system shall clearly disclose when guidance is generated or supported by AI.
- GOV-002 The system shall not provide legal advice, legal representation or document-processing services.
- GOV-003 The system shall not claim to replace public authorities, consulates, legal professionals or official institutions.
- GOV-004 The system shall avoid guarantees about appointment availability, passport delivery times, official approvals or document outcomes.
- GOV-005 The system shall provide human-rights-oriented guidance that respects dignity, inclusion and access to rights.
- GOV-006 The system shall use grounding sources approved by SMID as the basis for passport, workshop and organizational guidance.
- GOV-007 The system shall identify high-risk or sensitive user requests that may require escalation to human review.
- GOV-008 The system shall maintain traceability between generated guidance categories and the approved SMID knowledge sources used to support them.

#### Multi-Agent Requirements

- MA-001 The system shall include a Router Agent that receives user requests and routes them to the appropriate specialized agent.
- MA-002 The system shall include a Passport Guidance Agent that provides informational guidance about identity documents and passport-related topics.
- MA-003 The system shall include a Workshop Advisor Agent that provides informational guidance about SMID workshops, training sessions and educational activities.
- MA-004 The system shall include a Safety Agent that checks responses for safety, privacy and governance compliance before delivery where required.
- MA-005 The system shall route passport, SAIME, document-preparation and consular-process questions to the Passport Guidance Agent.
- MA-006 The system shall route workshop topic, registration, access, participation and certification questions to the Workshop Advisor Agent.
- MA-007 The system shall route ambiguous, mixed or sensitive requests through coordination logic that selects the relevant agent or requests clarification.
- MA-008 The system shall prevent specialized agents from bypassing shared safety, privacy and no-legal-advice constraints.

#### Evaluation and Human Review Requirements

- EVAL-001 The system shall support human review of requirements, grounding sources and response behavior before production use.
- EVAL-002 The system shall support review by SMID stakeholders for alignment with organizational mission, tone, service boundaries and human-rights approach.
- EVAL-003 The system shall support legal or privacy review for requirements involving legal-advice boundaries, personal data handling, retention and escalation.
- EVAL-004 The system shall be evaluated against test cases covering passport guidance, workshop guidance, privacy-sensitive requests and legal-advice boundary cases.
- EVAL-005 The system shall be evaluated for refusal and redirection behavior when users request legal advice, guaranteed outcomes or official procedure completion.
- EVAL-006 The system shall support periodic review of grounded content to identify outdated passport, consular, workshop or organizational information.
- EVAL-007 The system shall document known limitations of the current prototype, including reliance on available grounding files and absence of official procedure execution.

### Human Review Notes

SMID stakeholders should review the functional, AI governance and multi-agent requirements to confirm that the system reflects SMID's mission, service boundaries, workshop practices and human-rights approach.

Legal or privacy review may be required for requirements related to legal-advice boundaries, sensitive personal data, retention policies, escalation workflows, user warnings and any future storage of interaction data.

Several requirements depend on future technical implementation decisions, including access controls, logging, data retention, traceability, agent coordination logic, response review workflows and integration with updated knowledge sources.

The requirements most suitable for the current SMID Compass prototype are those covering informational guidance, workshop routing, passport guidance disclaimers, privacy minimization, AI transparency, no-legal-advice boundaries and human review before public deployment.
