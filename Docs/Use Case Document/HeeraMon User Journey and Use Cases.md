

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

**User Journeys and Use Cases** Use Case Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-03|
|---|---|
|**Title**|User Journeys and Use Cases|
|**Classification**|Use Case Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|SRS (HM-DOC-02), Product Vision (HM-DOC-01)|



## **Contents** 

|**1**|**Pur**|**pose**<br>. .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>**2**|
|---|---|---|---|---|
|**2**|**Cor**|**e User J**|**ourney**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>**3**|
|**3**|**Jou**|**rney A —**|**First-Time User** . . . . . . . . . . . . . . . . . . . . .|. . .<br>**4**|
||3.1|Scenario|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>4|
||3.2|Flow . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>4|
||3.3|Example|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>4|
|**4**|**Jou**|**rney B —**|**Continuous Job Search** . . . . . . . . . . . . . . . . .|. . .<br>**5**|
||4.1|Scenario|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>5|
||4.2|Flow . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>5|
|**5**|**Jou**|**rney C —**|**Close Match and Trade-Off Discussion** . . . . . . .|. . .<br>**6**|
||5.1|Scenario|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>6|
|**6**|**Jou**|**rney D —**|**Learning From User Decisions** . . . . . . . . . . . .|. . .<br>**7**|
||6.1|Example|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>7|
|**7**|**Jou**|**rney E —**|**Selecting a Job for Application** . . . . . . . . . . . .|. . .<br>**8**|
||7.1|Scenario|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>8|
||7.2|Flow . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>8|
|**8**|**Jou**|**rney F —**|**Application Review and Human Approval** . . . . .|. . .<br>**10**|
|**9**|**Jou**|**rney G —**|**Returning User**<br>. . . . . . . . . . . . . . . . . . . . .|. . .<br>**11**|
|**10 **|**Pri**|**mary Use**|**Cases**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>**12**|
||10.1|UC-01 —|Describe Desired Job<br>. . . . . . . . . . . . . . . . . . . .|. . .<br>12|
||10.2|UC-02 —|Modify Preferences<br>. . . . . . . . . . . . . . . . . . . . .|. . .<br>12|
||10.3|UC-03 —|Search for Jobs. . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>12|
||10.4|UC-04 —|Present a Match . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>12|
||10.5|UC-05 —|Investigate a Job. . . . . . . . . . . . . . . . . . . . . . .|. . .<br>13|
||10.6|UC-06 —|Accept or Reject Opportunity<br>. . . . . . . . . . . . . . .|. . .<br>13|
||10.7|UC-07 —|Prepare Application . . . . . . . . . . . . . . . . . . . . .|. . .<br>13|
||10.8|UC-08 —|Review Application . . . . . . . . . . . . . . . . . . . . .|. . .<br>13|
||10.9|UC-09 —|Submit Application . . . . . . . . . . . . . . . . . . . . .|. . .<br>13|
||10.1|0UC-10 —|Learn From Interaction . . . . . . . . . . . . . . . . . . .|. . .<br>13|
|**11 **|**Exc**|**eptional **|**/ Failure Journeys** . . . . . . . . . . . . . . . . . . . . .|. . .<br>**14**|
|**12 **|**Doc**|**ument C**|**ontrol** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>**15**|



1 

User Journeys and Use Cases 

HeeraMon 

### **1 Purpose** 

This document describes how users interact with HeeraMon and defines the primary user journeys and use cases. 

The objective is to translate the requirements in the Software Requirements Specification into understandable real-world workflows. 

Page 2 of 15 

User Journeys and Use Cases 

HeeraMon 

### **2 Core User Journey** 

The central HeeraMon experience is: 

#### **Describe** _→_ **Understand** _→_ **Search** _→_ **Evaluate** _→_ **Inform** _→_ **Discuss** _→_ **Decide** _→_ **Apply** 

The user should not need to repeatedly configure searches. HeeraMon maintains the user’s job-seeking context and continues searching in the background. 



<!-- Start of picture text -->
User opens Bird Introduces User Describes eee<br>HeeraMon HeeraMon Desired Job Preferences<br>Classifies MemoryRetrieval Cc»<br>vi ; into updated<br>Ask User €S AAlarification 1. Hard Constraints Memory,<br>Needed? 2. Soft Constraints<br>3. Learned Preferences<br>——> cenere Fow<br>—? Fetee Pats Save Begin Job 1 @) search |<br>——> Success Path Preferences Search | Periodically<br>——> Time-Dependent Flow Leseeeseeqeeseeeeed<br>UscateRetreval<br>Yes Meaningful Evaluate Normalize + Discover Jobs<br>Match? Matches Deduplicate<br>No<br>Proceed<br>>) Notifyo  User InvestigatesUser DecidesUser *| applicationPrepare<br>Reject<br>Memory<br>Update<br>Updated Learn if Approved (Approve/Edit/<br>[Approve]<br>Memory Useful ‘Submission Cancel)<br><!-- End of picture text -->

**Figure 1:** End-to-end user journey from describing desired work to job discovery, evaluation, decision, and application. 

Page 3 of 15 

User Journeys and Use Cases 

HeeraMon 

### **3 Journey A — First-Time User** 

#### **3.1 Scenario** 

A new user opens HeeraMon for the first time. 

#### **3.2 Flow** 

1. HeeraMon introduces itself through the bird character. 

2. The user is invited to describe what their next job should be like. 

3. The user describes requirements naturally. 

4. HeeraMon extracts relevant preferences. 

5. HeeraMon identifies potential ambiguities. 

6. HeeraMon asks short clarification questions only where necessary. 

7. The resulting preferences are stored. 

8. HeeraMon confirms the understood requirements. 

9. The user can modify or correct them. 

10. HeeraMon begins searching for suitable jobs. 

#### **3.3 Example** 

#### **User:** 

_“I want at least 40k BDT, an AI/ML role, maximum 30 minutes commute, around 7 hours a day, friendly colleagues and enough life outside work.”_ 

HeeraMon may interpret this as: 

#### **Must have** 

- Minimum salary: 40k BDT 

- AI/ML-related role 

- Maximum commute: approximately 30 minutes 

#### **Preferred** 

- Approximately 7-hour workday 

- Friendly workplace 

- Good work-life balance 

If the classification is uncertain, HeeraMon asks instead of assuming. 

Page 4 of 15 

User Journeys and Use Cases 

HeeraMon 

- **4 Journey B — Continuous Job Search** 

- **4.1 Scenario** 

The user has already described their preferences and leaves HeeraMon. 

HeeraMon continues searching according to the configured search schedule. 

#### **4.2 Flow** 

1. Background search begins. 

2. Available job sources are queried. 

3. New jobs are collected. 

4. Jobs are normalized and duplicates removed. 

5. Jobs are evaluated against the user’s preferences. 

6. Strong matches and meaningful close matches are identified. 

7. HeeraMon decides whether the opportunity is worth notifying the user about. 

8. The user receives a notification or sees the opportunity when returning to HeeraMon. 

9. The user can request details. 

The user should not need to manually initiate every search. 

Page 5 of 15 

User Journeys and Use Cases 

HeeraMon 

### **5 Journey C — Close Match and Trade-Off Discussion** 

#### **5.1 Scenario** 

HeeraMon finds a job that does not perfectly satisfy every preference. 

_“I found a close match. It meets your salary and AI/ML requirements, but the commute is approximately one hour instead of thirty minutes, and the workday is eight hours instead of seven.”_ 

The user may ask: 

_“What else does it offer?”_ 

HeeraMon provides the relevant information. 

The user may then: 

- Accept the trade-off 

- Reject the opportunity 

- Ask for more information 

- Change a preference 

- Ask HeeraMon to continue searching 

The user’s decision may contribute to learned preferences when appropriate. 

Page 6 of 15 

User Journeys and Use Cases 

HeeraMon 

### **6 Journey D — Learning From User Decisions** 

HeeraMon should gradually understand what the user actually values. 

#### **6.1 Example** 

HeeraMon repeatedly presents opportunities around 35k BDT. 

The user repeatedly rejects them because of salary. 

HeeraMon may later infer that salary below a certain threshold is generally unacceptable. However, inferred preferences should not silently become permanent hard constraints. 

When useful, HeeraMon can confirm: 

_“You have rejected several opportunities below 40k because of salary. Should I treat 40k as your minimum from now on?”_ 

The user decides. 

Page 7 of 15 

User Journeys and Use Cases 

HeeraMon 

- **7 Journey E — Selecting a Job for Application** 

- **7.1 Scenario** 

The user decides that a discovered job is worth pursuing. 

#### **7.2 Flow** 

1. User selects or tells HeeraMon to proceed. 

2. HeeraMon retrieves the available application information. 

3. HeeraMon prepares the application using the user’s stored profile and CV. 

4. HeeraMon identifies information that is missing or uncertain. 

5. HeeraMon presents the proposed application information to the user. 

6. User reviews the information. 

7. User may correct or cancel. 

8. HeeraMon proceeds only after explicit approval. 

9. HeeraMon submits through a supported application workflow. 

10. HeeraMon reports the result. 

Page 8 of 15 

User Journeys and Use Cases 

HeeraMon 



<!-- Start of picture text -->
Describes<br>Preferences<br>Search<br>Jobs<br>Normallze/<br>Filter<br>Evaluate<br>Match<br>Notify<br>Match<br>Ask For<br>Detalls<br>Explain<br>Trade -offs<br>Approve<br>Application Prepare<br>Application<br>Review/Edit<br>& Explicit<br>Approval.<br>Report |<br>Result<br><!-- End of picture text -->

**Figure 2:** Detailed interaction between the user, HeeraMon agent, job sources, matching system, and application workflow. 

Page 9 of 15 

User Journeys and Use Cases 

HeeraMon 

### **8 Journey F — Application Review and Human Approval** 

HeeraMon must not silently submit consequential information. 

Before submission, the user should see important fields such as: 

- Name 

- Contact information 

- Education 

- Experience 

- Skills 

- CV 

- Cover letter where applicable 

- Answers to application questions 

- Other information being submitted 

The user can: 

- **Approve** _→_ Submit 

- **Edit** _→_ Review again 

- **Cancel** _→_ Return to job 

HeeraMon must never invent qualifications or experience to complete an application. 

Page 10 of 15 

User Journeys and Use Cases 

HeeraMon 

### **9 Journey G — Returning User** 

When a user returns after a period away, HeeraMon should preserve continuity. 

The user may see: 

- New relevant jobs 

- Previously discussed jobs 

- Application progress 

- Preference changes 

- Pending decisions 

- Important notifications 

The user should be able to continue the conversation without reconstructing their requirements. 

Page 11 of 15 

User Journeys and Use Cases 

HeeraMon 

### **10 Primary Use Cases** 

**10.1 UC-01 — Describe Desired Job** 

**Actor:** User **Goal:** Tell HeeraMon what kind of work they want. **Precondition:** User has access to HeeraMon. 

#### **Main flow:** 

1. User starts a conversation. 

2. User describes desired work naturally. 

3. HeeraMon interprets the description. 

4. HeeraMon asks clarification questions if required. 

5. Preferences are stored. 

6. HeeraMon confirms the result. 

**Outcome:** A usable preference profile exists. 

**10.2 UC-02 — Modify Preferences** 

**Actor:** User 

**Goal:** Change previously established requirements. 

#### **Example:** 

_“Actually, I’m willing to commute for 45 minutes if the salary is at least 50k.”_ HeeraMon updates the relevant preference while preserving unrelated preferences. 

#### **10.3 UC-03 — Search for Jobs** 

**Actor:** HeeraMon 

**Goal:** Discover newly available opportunities. 

#### **Main flow:** 

1. Trigger scheduled search. 

2. Query available sources. 

3. Collect jobs. 

4. Normalize and deduplicate. 

5. Evaluate against user preferences. 

6. Store relevant opportunities. 

#### **10.4 UC-04 — Present a Match** 

**Actor:** HeeraMon 

**Goal:** Inform the user about a meaningful opportunity. 

Page 12 of 15 

User Journeys and Use Cases 

HeeraMon 

HeeraMon presents the opportunity and summarizes important matches, mismatches, and uncertainties. 

#### **10.5 UC-05 — Investigate a Job** 

**Actor:** User 

**Goal:** Ask questions about a job. 

The user can request details about salary, responsibilities, company, commute, working hours, benefits, requirements, or other available information. 

#### **10.6 UC-06 — Accept or Reject Opportunity** 

**Actor:** User 

**Goal:** Record a decision about an opportunity. 

The decision may affect future learned preferences. 

#### **10.7 UC-07 — Prepare Application** 

**Actor:** User + HeeraMon 

**Goal:** Prepare an application for an accepted opportunity. 

HeeraMon uses available user information and identifies missing or uncertain information. 

#### **10.8 UC-08 — Review Application** 

**Actor:** User 

**Goal:** Verify what HeeraMon intends to submit. 

The user can edit, approve, or cancel. 

#### **10.9 UC-09 — Submit Application** 

**Actor:** User + HeeraMon 

**Goal:** Submit an approved application through a supported workflow. **Precondition:** User has explicitly approved the final application. **Outcome:** Application is submitted or a clear failure state is reported. 

#### **10.10 UC-10 — Learn From Interaction** 

**Actor:** HeeraMon 

**Goal:** Improve future recommendations using relevant user decisions and conversations. 

Learned preferences must remain distinguishable from explicit user requirements. 

Page 13 of 15 

User Journeys and Use Cases 

HeeraMon 

### **11 Exceptional / Failure Journeys** 

HeeraMon should have defined behavior when: 

- A job source is unavailable. 

- A job disappears after being discovered. 

- Important job information is missing. 

- Two sources provide conflicting information. 

- A job is clearly outdated. 

- AI interpretation is uncertain. 

- Application information is incomplete. 

- An external application system fails. 

- A notification cannot be delivered. 

- The user changes preferences while a background search is running. 

In all cases, HeeraMon should prefer transparency and recoverability over pretending that the operation succeeded. 

Page 14 of 15 

User Journeys and Use Cases 

HeeraMon 

### **12 Document Control** 

**<mark>Version Date Author</mark>** **<u><mark>/</mark></u>** **<mark>Role Changes</mark>** 1.0 September 30, 2026 Product <u>/</u> Engineering Initial release ~~[dt~~ 

**Approval:** This document defines the primary user journeys and use cases for HeeraMon. All subsequent design and implementation work must remain consistent with these workflows. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Posden!<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 15 of 15 

