

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

**Matching & Preference Specification** Matching Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-06|
|---|---|
|**Title**|Matching & Preference Specification|
|**Classification**|Matching Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|SRS (HM-DOC-02), AI / Agent Spec (HM-DOC-04)|



## **Contents** 

|**1**|**Purpose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**2**|
|---|---|
|**2**|**Preference Model**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**2**|
|**3**|**Preference Types**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**2**|
||3.1<br>Hard Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>2|
||3.2<br>Soft Preferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
||3.3<br>Learned Preferences. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
||3.4<br>Unknown<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
|**4**|**Preference Priority**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**3**|
|**5**|**Job Matching** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**3**|
|**6**|**Matching Logic** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**4**|
|**7**|**Trade-Off Handling** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**4**|
|**8**|**Learning From Decisions** . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**5**|
|**9**|**Explainability** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**5**|
|**10**|**Boundaries**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**6**|
|**11**|**Success Criteria**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**6**|
|**12**|**Document Control** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>**7**|



1 

Matching & Preference Specification 

HeeraMon 

### **1 Purpose** 

This document defines how HeeraMon represents user preferences and determines how well a job fits those preferences. 

The goal is not to produce a generic job-ranking score. The goal is to determine whether an opportunity is worth the user’s attention and why. 

### **2 Preference Model** 

User preferences should be represented as structured records derived from natural-language conversation. 

Each preference should contain, where applicable: 

- Preference type 

- Value 

- Priority 

- Source 

- Confidence 

- Status 

- Timestamp 

#### **Example:** 

1 <mark>`Category: Salary`</mark> 

- 2 <mark>`Value: 40 ,000 BDT`</mark> 

- 3 <mark>`Type: Hard`</mark> 

- 4 <mark>`Source: User explicitly stated`</mark> 

- 5 <mark>`Confidence: High`</mark> 

### **3 Preference Types** 

HeeraMon uses four important classifications: 

#### **3.1 Hard Requirements** 

Conditions that normally must be satisfied. 

Examples: 

- Minimum salary 

- Remote-only requirement 

- Required location 

- Required employment type 

Page 2 of 7 

Matching & Preference Specification 

HeeraMon 

A job violating a hard requirement should normally not be presented as a normal match. 

#### **3.2 Soft Preferences** 

Desirable conditions that can be traded off. 

Examples: 

- Short commute 

- Flexible hours 

- Lunch benefits 

- Preferred technology stack 

A job can remain relevant while failing one or more soft preferences. 

#### **3.3 Learned Preferences** 

Preferences inferred from repeated user behavior or previous decisions. 

Example: User repeatedly rejects jobs below 40k. 

HeeraMon may infer that salary is important, but should ask for confirmation before permanently treating the inferred threshold as a hard requirement. 

#### **3.4 Unknown** 

Information that has not been established. 

Unknown must never be treated as either satisfied or violated without evidence. 

### **4 Preference Priority** 

When preferences conflict, HeeraMon should generally consider them in this order: 

**Explicit Hard Requirement** _→_ **Confirmed Preference** _→_ **Soft Preference** _→_ **Inferred Preference** 

However, the agent should ask the user when a conflict materially affects the recommendation. 

Temporary conversational requests should not automatically become permanent preferences. 

### **5 Job Matching** 

Matching should consider both constraint satisfaction and overall fit. 

For each job, HeeraMon should determine: 

- Hard requirements satisfied? 

Page 3 of 7 

Matching & Preference Specification 

HeeraMon 

- Soft preferences satisfied? 

- Important preferences unknown? 

- Major conflicts? 

- Relevant trade-offs? 

- Confidence in the assessment? 

A useful internal representation is: 

|1|`Job`|||
|---|---|---|---|
|2||`Hard`|`constraints`|
|3|||`Satisfied`|
|4|||`Violated`|
|5|||`Unknown`|
|6||`Soft`|`preferences`|
|7|||`Satisfied`|
|8|||`Not`<br>`satisfied`|
|9|||`Unknown`|
|10||`Trade`|`-offs`|
|11||`R`|`elevant`<br>`differences`|



### **6 Matching Logic** 

Matching should follow a staged approach: 

1. **Eligibility check** — Identify violations of explicit hard requirements. 

2. **Preference comparison** — Compare remaining jobs against soft and confirmed preferences. 

3. **Trade-off identification** — Identify meaningful advantages and disadvantages. 

4. **Uncertainty assessment** — Identify important missing or unreliable information. 

5. **Fit explanation** — Generate a concise explanation of why the job is or is not worth considering. 

The system may use numerical scores internally where useful, but a score must not replace the underlying reasoning or explanation. 

### **7 Trade-Off Handling** 

HeeraMon should not blindly reject every imperfect job. 

#### **Example:** 

- 1 <mark>`User preference:`</mark> 2 <mark>`Salary 40k`</mark> 3 <mark>`Commute 30 minutes`</mark> 

- 4 <mark>`AI/ML role`</mark> 

5 <mark>`7-hour workday preferred`</mark> 

Page 4 of 7 

Matching & Preference Specification 

HeeraMon 

6 

- 7 <mark>`Job:`</mark> 

- 8 <mark>`Salary: 45k`</mark> 

- 9 <mark>`Commute: ~60 minutes`</mark> 

- 10 <mark>`AI/ML: Yes`</mark> 

- 11 <mark>`Workday: 8 hours`</mark> 

HeeraMon should explain: 

_Salary and role match your requirements, but the commute and working hours are worse than your preferences._ 

The user can then decide whether the trade-off is acceptable. 

If the violated condition is explicitly hard, the job should normally be excluded unless the user has allowed exceptions. 

### **8 Learning From Decisions** 

User actions provide evidence about preferences. 

Examples: 

- Repeatedly rejecting low-salary jobs 

- Consistently accepting remote roles 

- Rejecting long commutes 

- Asking repeatedly about work-life balance 

HeeraMon may use these patterns to improve future matching. 

However: 

#### **Observed behavior** _̸_ = **confirmed requirement.** 

When an inferred preference becomes important enough to materially change future results, HeeraMon should request confirmation. 

### **9 Explainability** 

Every meaningful recommendation should be explainable in human terms. 

The user should be able to understand: 

- Why this job was considered. 

- What matches their preferences. 

- What does not match. 

- What information is unknown. 

- What trade-offs exist. 

Page 5 of 7 

Matching & Preference Specification 

HeeraMon 

- Which preference influenced the decision. 

HeeraMon should avoid presenting unexplained numbers such as: 

_“Match score: 87%”_ 

without providing the underlying reasoning. 

### **10 Boundaries** 

The initial release does not require: 

- sophisticated machine-learning recommendation models; 

- complex behavioral prediction; 

- embeddings-based ranking everywhere; 

- large-scale personalization models; 

- perfect commute calculations; 

- automated estimation of unknown job attributes. 

Deterministic filtering combined with structured preference comparison and LLM-assisted interpretation is sufficient. 

The architecture should allow more advanced ranking and personalization to be added later. 

### **11 Success Criteria** 

The matching system is successful when HeeraMon can: 

1. Convert natural-language preferences into structured requirements. 

2. Distinguish hard, soft, learned, and unknown preferences. 

3. Exclude or appropriately flag hard-constraint violations. 

4. Identify meaningful matches. 

5. Explain important trade-offs. 

6. Preserve uncertainty instead of inventing facts. 

7. Learn useful patterns from user decisions. 

8. Ask for confirmation when inferred preferences become consequential. 

9. Improve future recommendations based on confirmed preferences. 

**Core principle:** A job is not valuable because it scores highly. It is valuable when HeeraMon can explain why it fits the user’s priorities and whether the remaining tradeoffs are worth considering. 

Page 6 of 7 

Matching & Preference Specification 

HeeraMon 

### **12 Document Control** 

**<mark>Version Date Author</mark>** **<u><mark>/</mark></u>** **<mark>Role Changes</mark>** 1.0 September 30, 2026 Product <u>/</u> Engineering Initial release ~~[dt~~ 

**Approval:** This document defines the matching and preference behavior for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Posden!<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 7 of 7 

