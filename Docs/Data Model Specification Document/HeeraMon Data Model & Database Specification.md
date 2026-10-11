

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

**Data Model / Database Specification** Data Model Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-08|
|---|---|
|**Title**|Data Model / Database Specification|
|**Classification**|Data Model Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|Technical Architecture (HM-DOC-07), SRS (HM-<br>DOC-02)|



## **Contents** 

|**1**|**Pur**|**pose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
|---|---|---|---|
|**2**|**Des**|**ign Principles**. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
|**3**|**Cor**|**e Entities** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
||3.1|User . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>2|
||3.2|User Preference . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||3.3|Conversation<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||3.4|Message . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||3.5|Job . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||3.6|Job Source . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||3.7|Job Source Record<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||3.8|Match . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>5|
||3.9|User Decision . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>5|
||3.10|Application<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>6|
||3.11|Notification . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>6|
||3.12|Agent Run / Task. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>6|
|**4**|**Cor**|**e Relationships**. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**7**|
|**5**|**Ent**|**ity-Relationship Diagram** . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**8**|
|**6**|**Im**|**portant Data Rules**<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**8**|
||6.1|Preference History<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
||6.2|Job Deduplication. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
||6.3|User Isolation . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
||6.4|Application State . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
||6.5|Agent State . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>9|
||6.6|Unknown Values<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>9|
|**7**|**Ind**|**exing and Performance** . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**9**|
|**8**|**Bo**|**undaries**<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**9**|
|**9**|**Suc**|**cess Criteria**<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**9**|
|**10 **|**Do**|**cument Control** . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**10**|



1 

Data Model <u>/</u> Database Specification 

HeeraMon 

### **1 Purpose** 

This document defines the persistent data model for HeeraMon. 

The database should provide a reliable source of truth for: 

- users; 

- preferences; 

- conversations; 

- jobs; 

- matches; 

- decisions; 

- applications; 

- notifications; 

- ingestion sources; 

- agent/background state. 

PostgreSQL is the proposed database. 

### **2 Design Principles** 

The data model should: 

- keep persistent application state separate from temporary LLM output; 

- preserve user decisions and preference history; 

- distinguish explicit preferences from learned preferences; 

- preserve job-source information; 

- support background processing; 

- support auditability of consequential actions; 

- avoid unnecessary duplication; 

- remain extensible for future versions. 

### **3 Core Entities** 

#### **3.1 User** 

Represents an authenticated HeeraMon user. 

Key information: 

- id 

- authentication/provider identifiers 

- name 

Page 2 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

- contact information 

- profile information 

- created/updated timestamps 

#### **3.2 User Preference** 

Represents a requirement or preference extracted from conversation. 

Key information: 

- id 

- user ~~i~~ d 

- category 

- value 

- type: hard / soft / learned 

- source: explicit / confirmed / inferred 

- confidence 

- status 

- created/updated timestamps 

Preference history should be preserved where changes affect future matching. 

#### **3.3 Conversation** 

Represents a user-agent conversation or conversation thread. 

Key information: 

- id 

- user ~~i~~ d 

- title/context metadata 

- created/updated timestamps 

#### **3.4 Message** 

Represents an individual conversational message. 

Key information: 

- id 

- conversation ~~i~~ d 

- role 

- content 

- metadata 

- timestamp 

Page 3 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

#### **3.5 Job** 

Represents a normalized job opportunity. 

Key information: 

- id 

- title 

- company 

- description 

- location 

- salary 

- work arrangement 

- employment type 

- requirements 

- benefits 

- application URL 

- status 

- first-seen/last-seen timestamps 

#### **3.6 Job Source** 

Represents where a job originated. 

Key information: 

- id 

- source name 

- source type 

- source URL/configuration 

- status 

- last successful sync 

- error information 

#### **3.7 Job Source Record** 

Represents the relationship between a normalized job and its original source record. 

This allows HeeraMon to preserve source-specific identifiers and URLs while maintaining one normalized job. 

Key information: 

- id 

- job ~~i~~ d 

Page 4 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

- source ~~i~~ d 

- external job ID 

- source URL 

- source metadata 

- first-seen/last-seen timestamps 

#### **3.8 Match** 

Represents HeeraMon’s evaluation of a job for a specific user. 

Key information: 

- id 

- user ~~i~~ d 

- job ~~i~~ d 

- eligibility status 

- match information 

- satisfied preferences 

- violated preferences 

- unknown information 

- trade-offs 

- explanation 

- created/updated timestamps 

A match belongs to both a user and a job. 

#### **3.9 User Decision** 

Represents a user’s response to an opportunity. Examples: 

- interested 

- rejected 

- saved 

- proceed to application 

- ignored 

Key information: 

- id 

- user ~~i~~ d 

- job ~~i~~ d 

Page 5 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

- decision 

- reason/context where available 

- timestamp 

These decisions provide evidence for future preference learning. 

#### **3.10 Application** 

Represents an application workflow for a specific user and job. 

Key information: 

- id 

- user ~~i~~ d 

- job ~~i~~ d 

- status 

- prepared application data 

- submission status 

- external application identifier where available 

- timestamps 

Possible statuses include: 

**draft** _→_ **review** _→_ **approved** _→_ **submitted** 

with appropriate failure/cancellation states. 

#### **3.11 Notification** 

Represents a notification generated for a user. 

Key information: 

- id 

- user ~~i~~ d 

- notification type 

- related entity 

- message/content 

- read status 

- delivery status 

- timestamp 

#### **3.12 Agent Run / Task** 

Represents a background or significant agent execution. 

Page 6 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

Useful for tracking: 

- task type; 

- status; 

- input/context references; 

- execution timestamps; 

- errors; 

- retry information. 

This supports observability and resumable background workflows. 

### **4 Core Relationships** 

The main relationships are: 

- One User has many Preferences. 

- One User has many Conversations. 

- One Conversation has many Messages. 

- One User can have many Matches. 

- One Job can have many Matches across different users. 

- One User can make many Decisions. 

- One Job can have many Decisions from different users. 

- One User can have many Applications. 

- One Job can have applications from multiple users. 

- One Job Source can contain many source records. 

- One Job can have records from multiple sources. 

- One User can receive many Notifications. 

- One User can have many Agent Runs / Tasks. 

Page 7 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

### **5 Entity-Relationship Diagram** 



<!-- Start of picture text -->
[—weroecicefe |<br>cl<br>[afm<br>|<br>a 2 [_erteene||<br>= a |<br>om SS ia, oy<br>‘eligibility status ‘authentication /provider identifiers] vee<br>a a<br>mesaen a {|coma<br>ef | refer | | eid<br>Os ‘|<br>1]ig cd coettotee tontonne roecenter.<br>le re<br>. —<br>~~ je vette<br>onene a<br><!-- End of picture text -->

**Figure 1:** Core HeeraMon entity-relationship model. 

### **6 Important Data Rules** 

#### **6.1 Preference History** 

Preference changes should not silently overwrite important historical context. 

#### **6.2 Job Deduplication** 

Multiple source records may point to the same normalized job. 

#### **6.3 User Isolation** 

A user’s private data must only be accessible within their authorized account context. 

#### **6.4 Application State** 

Application status must be controlled by backend logic and explicit user actions, not by arbitrary LLM output. 

Page 8 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

#### **6.5 Agent State** 

LLM-generated state should not become authoritative unless validated and persisted by application logic. 

#### **6.6 Unknown Values** 

Unknown job or preference information should remain explicitly unknown rather than represented as guessed values. 

### **7 Indexing and Performance** 

The system should index frequently queried fields such as: 

- user IDs; 

- job status; 

- source IDs; 

- external job IDs; 

- job URLs; 

- preference ownership; 

- match ownership; 

- application status; 

- timestamps used for background processing. 

Indexes should be added based on actual query patterns rather than indiscriminately. 

### **8 Boundaries** 

The initial release does not require: 

- a separate data warehouse; 

- complex analytics schemas; 

- a dedicated vector database; 

- distributed databases; 

- large-scale event sourcing; 

- advanced recommendation-specific storage. 

The relational PostgreSQL model should remain the primary source of truth. 

### **9 Success Criteria** 

The data model is successful when it can reliably represent: 

1. A user’s identity and profile. 

Page 9 of 10 

Data Model <u>/</u> Database Specification 

HeeraMon 

2. Their explicit and learned preferences. 

3. Their conversations and decisions. 

4. Normalized jobs and their sources. 

5. User-specific job matches. 

6. Application preparation and submission state. 

7. Notifications. 

8. Background agent activity. 

**Core principle:** The database should preserve the history and state needed to make HeeraMon continuous, explainable, and trustworthy. 

### **10 Document Control** 

**<mark>Version Date Author</mark>** **<u><mark>/</mark></u>** **<mark>Role Changes</mark>** ~~<mark>—_—_—_—_—</mark>~~ 1.0 September 30, 2026 Product <u>/</u> Engineering Initial release 

**Approval:** This document defines the persistent data model for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Posden!<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 10 of 10 

