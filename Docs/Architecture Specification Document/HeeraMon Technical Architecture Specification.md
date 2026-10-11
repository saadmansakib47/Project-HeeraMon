

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

**Technical Architecture Specification** Architecture Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-07|
|---|---|
|**Title**|Technical Architecture Specification|
|**Classification**|Architecture Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|SRS (HM-DOC-02), AI / Agent Spec (HM-DOC-04)|



## **Contents** 

|**1**|**Pu**|**rpose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**2**|
|---|---|---|---|
|**2**|**Arc**|**hitectural Principle** . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**2**|
|**3**|**Hig**|**h-Level Components**<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**3**|
||3.1|Frontend . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.2|Backend API<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.3|Agent Layer . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.4|Job Ingestion Layer . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||3.5|Matching Layer . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||3.6|Background Worker / Scheduler . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||3.7|Database. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||3.8|External Services . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
|**4**|**Pro**|**posed Stack** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**5**|
||4.1|Frontend . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
||4.2|Backend . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
||4.3|Database / Authentication . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
||4.4|Agent Orchestration<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
||4.5|LLM . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
|**5**|**Ag**|**ent Architecture**<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**6**|
|**6**|**LL**|**M Provider Abstraction**<br>. . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**6**|
|**7**|**Da**|**ta and State** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**6**|
|**8**|**Bac**|**kground Execution** . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**7**|
|**9**|**Rel**|**iability and Failure Isolation**<br>. . . . . . . . . . . .|. . . . . . . . . . .<br>**7**|
|**10 **|**Sec**|**urity Boundaries** . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**11 **|**Cos**|**t Strategy** . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**12 **|**Arc**|**hitectural Boundaries**<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**13 **|**Suc**|**cess Criteria**<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**9**|
|**14 **|**Do**|**cument Control** . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**9**|



1 

Technical Architecture Specification 

HeeraMon 

### **1 Purpose** 

This document defines the technical architecture of HeeraMon. 

The architecture should be: 

- production-oriented from the start; 

- simple enough for a small team or individual developer; 

- inexpensive to operate initially; 

- testable and observable; 

- replaceable and extensible; 

- suitable for future background agents and larger job volume. 

The architecture should avoid unnecessary complexity without creating a dead end for future versions. 

**2 Architectural Principle** 

HeeraMon follows an: 

#### **LLM-assisted, not LLM-dependent** 

architecture. 

The LLM should handle tasks where language understanding and reasoning provide real value, such as: 

- interpreting user messages; 

- extracting preferences; 

- understanding job descriptions; 

- resolving ambiguity; 

- explaining trade-offs; 

- deciding when a tool is useful. 

Deterministic software should handle tasks such as: 

- authentication; 

- database operations; 

- filtering; 

- deduplication; 

- scheduling; 

- notifications; 

- state management; 

- security; 

Page 2 of 10 

Technical Architecture Specification 

HeeraMon 

- rate limiting; 

- validation. 

This reduces cost, improves reliability, and makes the system easier to test. 

### **3 High-Level Components** 

HeeraMon consists of the following major components: 

#### **3.1 Frontend** 

Responsible for: 

- conversational interface; 

- onboarding; 

- job presentation; 

- preference visibility and editing; 

- notifications; 

- application review; 

- authentication. 

#### **3.2 Backend API** 

Responsible for: 

- business logic; 

- authentication/session handling; 

- user and job data access; 

- orchestration between frontend, agent, and services; 

- API endpoints; 

- security and validation. 

#### **3.3 Agent Layer** 

Responsible for: 

- conversation reasoning; 

- preference extraction; 

- job interpretation; 

- trade-off reasoning; 

- tool selection; 

- conversational decisions. 

The system uses one agent with multiple tools, rather than a multi-agent architecture. 

Page 3 of 10 

Technical Architecture Specification 

HeeraMon 

#### **3.4 Job Ingestion Layer** 

Responsible for: 

- source adapters; 

- fetching jobs; 

- normalization; 

- validation; 

- deduplication; 

- freshness tracking. 

#### **3.5 Matching Layer** 

Responsible for: 

- deterministic constraint filtering; 

- preference comparison; 

- candidate selection; 

- structured match information. 

The LLM may interpret or explain results, but should not be required for every basic filtering operation. 

#### **3.6 Background Worker / Scheduler** 

Responsible for: 

- periodic job searches; 

- source ingestion; 

- matching new jobs; 

- notification triggering; 

- maintenance tasks. 

#### **3.7 Database** 

Responsible for persistent application state including: 

- users; 

- preferences; 

- conversations; 

- jobs; 

- matches; 

- applications; 

- notifications; 

Page 4 of 10 

Technical Architecture Specification 

HeeraMon 

- agent state; 

- source metadata. 

#### **3.8 External Services** 

May include: 

- LLM providers; 

- job sources; 

- authentication providers; 

- email/push notification services; 

- external application systems. 

External dependencies should be isolated behind service interfaces where practical. 

### **4 Proposed Stack** 

The initial implementation may use: 

#### **4.1 Frontend** 

- Next.js 

- TypeScript 

- Tailwind CSS 

- Framer Motion 

#### **4.2 Backend** 

- Python 

- FastAPI 

#### **4.3 Database / Authentication** 

- PostgreSQL 

- Supabase 

#### **4.4 Agent Orchestration** 

- LangGraph 

#### **4.5 LLM** 

- Provider abstraction supporting hosted or compatible models 

The exact hosting provider may remain flexible during implementation. 

These choices are implementation defaults, not permanent product requirements. 

Page 5 of 10 

Technical Architecture Specification 

HeeraMon 

### **5 Agent Architecture** 

HeeraMon should use: 

#### **One agent + multiple deterministic tools** 

Example tools may include: 

- `get` ~~`u`~~ `ser preferences` 

- `update` ~~`u`~~ `ser preferences` 

- `search` ~~`j`~~ `obs` 

- `get` ~~`j`~~ `ob details` 

- `compare` ~~`j`~~ `ob to preferences` 

- `get` ~~`u`~~ `ser profile` 

- `get` ~~`c`~~ `v` 

- `prepare` ~~`a`~~ `pplication` 

- `save` ~~`d`~~ `ecision` 

- `send` ~~`n`~~ `otification` 

The agent should call tools when necessary rather than directly manipulating application state through uncontrolled model output. 

### **6 LLM Provider Abstraction** 

LLM access should be isolated behind a provider layer. 

Conceptually: 

**HeeraMon Agent** _→_ **LLM Provider Interface** _→_ **Selected Model** 

The provider may later support: 

- HeeraMon-hosted models/API access; 

- OpenAI; 

- Google; 

- Anthropic; 

- compatible local/open models; 

- user-provided API keys where appropriate. 

The rest of the application should not depend directly on one model provider. 

### **7 Data and State** 

PostgreSQL should be the primary source of truth for persistent application data. 

Page 6 of 10 

Technical Architecture Specification 

HeeraMon 

Agent state should be persisted where required for: 

- continuing conversations; 

- background execution; 

- interrupted workflows; 

- human approval steps; 

- application preparation; 

- future agent resumption. 

Transient model output should not be treated as authoritative application state. 

### **8 Background Execution** 

Continuous job seeking must not depend on the user keeping the browser open. 

Background processes should be able to: 

1. retrieve new jobs; 

2. normalize and store them; 

3. evaluate relevant users; 

4. identify meaningful matches; 

5. create notifications; 

6. allow the user to resume the conversation later. 

Background jobs should be idempotent where practical so that retries do not create duplicate records or actions. 

### **9 Reliability and Failure Isolation** 

External failures should not bring down the core application. 

Examples: 

- LLM unavailable _→_ conversational functions may degrade, while stored data remains accessible. 

- Job source unavailable _→_ other sources continue operating. 

- Notification failure _→_ notification can be retried. 

- Application site unavailable _→_ application remains pending rather than being falsely marked successful. 

Important operations should have: 

- timeouts; 

- retries where appropriate; 

Page 7 of 10 

Technical Architecture Specification 

HeeraMon 

- error logging; 

- clear failure states. 

### **10 Security Boundaries** 

Security-sensitive operations should remain under deterministic backend control. 

The LLM must not independently control: 

- authentication; 

- authorization; 

- secrets; 

- unrestricted database access; 

- arbitrary code execution; 

- final application submission. 

Tool permissions should follow least privilege. 

User approval must be enforced by application logic, not merely by an instruction in the system prompt. 

### **11 Cost Strategy** 

The system should target minimal or zero infrastructure cost during development and early experimentation where practical. 

Cost should be controlled through: 

- deterministic filtering before LLM calls; 

- limited background search frequency; 

- caching; 

- deduplication; 

- concise prompts; 

- model/provider flexibility; 

- free-tier infrastructure where appropriate; 

- avoiding unnecessary agent calls. 

The architecture should allow paid infrastructure and higher-capacity models to be introduced later without major redesign. 

### **12 Architectural Boundaries** 

The initial release does not require: 

Page 8 of 10 

Technical Architecture Specification 

HeeraMon 

- microservices; 

- Kubernetes; 

- multiple autonomous agents; 

- complex event-driven infrastructure; 

- dedicated vector databases; 

- a large data warehouse; 

- advanced distributed systems; 

- custom ML ranking infrastructure. 

A modular application with clear service boundaries is preferred over premature distributed architecture. 

### **13 Success Criteria** 

The architecture is successful when it can support the complete core loop: 

**User** _→_ **Conversation** _→_ **Preferences** _→_ **Job Ingestion** _→_ **Matching** _→_ **Agent Reasoning** _→_ **Notification** _→_ **User Decision** _→_ **Application Preparation** _→_ 

#### **Human Approval** 

while remaining: 

- understandable; 

- testable; 

- secure; 

- affordable; 

- observable; 

- replaceable where external providers are concerned; 

- extensible toward future versions. 

**Core principle:** Build the system as a small production system, not as a disposable prototype. 

### **14 Document Control** 

|**Version**|**Date**|**Author **|**/ Role**|**Changes**|
|---|---|---|---|---|
|1.0|September 30, 2026|Product /|Engineering|Initial release|



**Approval:** This document defines the technical architecture for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

Page 9 of 10 

Technical Architecture Specification 

HeeraMon 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Doodle<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 10 of 10 

