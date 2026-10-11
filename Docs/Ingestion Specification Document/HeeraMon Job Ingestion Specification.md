

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

**Job Ingestion Specification** Ingestion Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-05|
|---|---|
|**Title**|Job Ingestion Specification|
|**Classification**|Ingestion Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|SRS (HM-DOC-02), AI / Agent Spec (HM-DOC-04)|



## **Contents** 

|**1**|**Purpose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**2**|
|---|---|---|
|**2**|**Ingestion Flow**<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**2**|
|**3**|**Job Sources** . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**2**|
|**4**|**Job Normalization** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**2**|
|**5**|**Deduplication** . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**3**|
|**6**|**Validation and Quality** . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**3**|
|**7**|**Freshness**. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**4**|
|**8**|**Source Reliability**<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**4**|
|**9**|**Legal and Operational Constraints**. . . . . . . . . . . .|. . . . . . . . . .<br>**5**|
|**10 **|**Boundaries**<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**5**|
|**11 **|**Success Criteria**<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**5**|
|**12 **|**Document Control** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>**6**|



1 

Job Ingestion Specification 

HeeraMon 

### **1 Purpose** 

This document defines how HeeraMon discovers, collects, normalizes, validates, deduplicates, and stores job opportunities from external sources. 

The goal is to create a reliable internal job dataset that the matching and agent systems can use consistently. 

### **2 Ingestion Flow** 

The ingestion pipeline is: 

**Discover** _→_ **Fetch** _→_ **Extract** _→_ **Normalize** _→_ **Validate** _→_ **Deduplicate** _→_ **Store** _→_ **Evaluate** 

Job ingestion should be separated from job matching. The ingestion system produces clean, structured job records; HeeraMon then evaluates those records against user preferences. 

### **3 Job Sources** 

HeeraMon should support a source-adapter approach so new sources can be added without changing the rest of the system. 

Potential source types include: 

- Public job APIs 

- RSS/Atom feeds 

- Public job boards 

- Company career pages 

- Structured job postings / JSON-LD 

- Other legally and technically accessible sources 

The initial implementation should begin with a small number of reliable and accessible sources rather than attempting to cover the entire internet. 

Each source adapter should have a consistent interface for retrieving job data. 

### **4 Job Normalization** 

Different sources may describe the same job differently. 

HeeraMon should convert incoming postings into a common internal format containing, where available: 

- Job title 

- Company 

Page 2 of 6 

Job Ingestion Specification 

HeeraMon 

- Description 

- Responsibilities 

- Required skills 

- Preferred skills 

- Salary / compensation 

- Location 

- Work arrangement 

- Working hours 

- Employment type 

- Experience requirements 

- Education requirements 

- Benefits 

- Application URL 

- Source 

- Original posting date 

- Last-seen timestamp 

- Job expiration/status information 

Fields that are unavailable should remain unknown/null, not be fabricated. 

### **5 Deduplication** 

The same opportunity may appear across multiple sources. 

HeeraMon should detect likely duplicates using available identifiers and normalized attributes such as: 

- source/job ID; 

- application URL; 

- company; 

- normalized job title; 

- location; 

- posting similarity. 

Duplicate detection should preserve source information where useful rather than creating multiple independent opportunities. 

### **6 Validation and Quality** 

Before a job becomes available for matching, HeeraMon should perform basic validation. 

Page 3 of 6 

Job Ingestion Specification 

HeeraMon 

#### At minimum: 

- Job title should exist. 

- Company should be identifiable where possible. 

- Description should contain usable information. 

- Application destination should be valid where applicable. 

- Clearly malformed records should be rejected. 

- Expired or unavailable jobs should be marked appropriately. 

HeeraMon should preserve uncertainty instead of filling gaps with guesses. 

### **7 Freshness** 

Job postings change over time. 

The ingestion system should track: 

- first discovered time; 

- last checked time; 

- source update time when available; 

- active/expired status; 

- changes to important fields. 

Repeated ingestion should update existing records rather than blindly creating new ones. 

### **8 Source Reliability** 

Sources should be treated independently. 

A source may become: 

- temporarily unavailable; 

- rate-limited; 

- structurally changed; 

- stale; 

- inaccessible; 

- inconsistent. 

A failure in one source should not stop the entire ingestion system. 

Source-specific errors should be logged and observable. 

Page 4 of 6 

Job Ingestion Specification 

HeeraMon 

### **9 Legal and Operational Constraints** 

HeeraMon should only use job information through sources and access methods that are permitted for the intended use. 

The ingestion system should respect applicable: 

- Terms of Service; 

- robots/access restrictions; 

- API limits; 

- rate limits; 

- copyright and data-use requirements. 

The system should prefer APIs, feeds, public structured data, and permitted access methods over fragile or aggressive scraping. 

### **10 Boundaries** 

The initial release does not need: 

- dozens of job-source integrations; 

- complete internet-wide coverage; 

- sophisticated web crawling; 

- real-time ingestion; 

- perfect duplicate detection; 

- advanced job-data enrichment; 

- paid job-data infrastructure. 

The architecture should make additional source adapters possible later without redesigning the matching system. 

### **11 Success Criteria** 

The ingestion system is successful when HeeraMon can: 

1. Collect jobs from several usable sources. 

2. Convert different source formats into one internal job format. 

3. Detect and reduce duplicate opportunities. 

4. Preserve unknown information honestly. 

5. Track job freshness and availability. 

6. Handle individual source failures gracefully. 

7. Provide clean job records to the matching and agent systems. 

Page 5 of 6 

Job Ingestion Specification 

HeeraMon 

**Core principle:** HeeraMon does not need every job on the internet. It needs a sufficiently reliable stream of structured, usable opportunities for the personal job-search loop to work. 

### **12 Document Control** 

**<mark>Version Date Author</mark>** **<u><mark>/</mark></u>** **<mark>Role Changes</mark>** ~~—~~ 1.0 September 30, 2026 Product <u>/</u> Engineering Initial release **Approval:** This document defines the job ingestion behavior for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Poadorn/<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 6 of 6 

