

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

## **API Specification** 

API Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-10|
|---|---|
|**Title**|API Specification|
|**Classification**|API Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**|Technical Architecture (HM-DOC-07), SRS (HM-|
|**ments**|DOC-02)|



## **Contents** 

|**1**|**Purpose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
|---|---|---|
|**2**|**API Principles** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
|**3**|**Authentication** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**2**|
|**4**|**Core Endpoints** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**3**|
||4.1<br>Authentication<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||4.2<br>Conversations . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||4.3<br>Preferences<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||4.4<br>Jobs . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||4.5<br>Matches . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||4.6<br>Notifications . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||4.7<br>Applications . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
|**5**|**Background Operations**. . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**5**|
|**6**|**Request and Response Design**<br>. . . . . . . . . . . .|. . . . . . . . . . . .<br>**5**|
|**7**|**Pagination** . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**5**|
|**8**|**Validation** . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**6**|
|**9**|**Error Handling** . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**6**|
|**10 **|**Rate Limiting** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**6**|
|**11 **|**API and Agent Boundary** . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**7**|
|**12 **|**Boundaries**<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**7**|
|**13 **|**Success Criteria**<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**7**|
|**14 **|**Document Control** . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>**8**|



1 

API Specification 

HeeraMon 

### **1 Purpose** 

This document defines the primary API contract for HeeraMon. 

The API connects the frontend with backend services and provides controlled access to user data, conversations, jobs, preferences, matches, notifications, and application workflows. 

The API should remain versioned, authenticated, validated, and independent of the frontend implementation. 

### **2 API Principles** 

The API should: 

- use predictable resource-oriented endpoints; 

- validate all incoming data; 

- enforce authentication and authorization server-side; 

- return structured responses; 

- provide meaningful error responses; 

- avoid exposing internal implementation details; 

- keep LLM output behind controlled backend logic; 

- support future API versioning. 

Proposed base path: 

```
/api/v1
```

### **3 Authentication** 

Authentication should be handled through the chosen authentication provider, with the backend validating the authenticated user’s identity. 

Every user-specific endpoint must verify that the requested resource belongs to the authenticated user. 

Authentication should support frictionless providers where practical, such as: 

- Google; 

- GitHub; 

- email-based authentication. 

The API must never trust a user-supplied `user` ~~`i`~~ `d` as proof of authorization. 

Page 2 of 8 

API Specification 

HeeraMon 

### **4 Core Endpoints** 

#### **4.1 Authentication** 

Authentication may primarily be handled by the authentication provider rather than custom application endpoints. 

#### **4.2 Conversations** 

```
GET/conversations
POST/conversations
GET/conversations /{ conversation_id }
POST/conversations /{ conversation_id }/ messages
```

Responsibilities: 

- retrieve conversation history; 

- create conversations; 

- send messages; 

- return HeeraMon responses. 

The backend controls agent/tool execution. 

#### **4.3 Preferences** 

|`GET`|`/preferences`|
|---|---|
|`POST`|`/preferences`|
|`PATCH`|`/preferences /{ preference_id}`|
|`DELETE `|`/preferences /{ preference_id}`|



Responsibilities: 

- retrieve current preferences; 

- create/update preferences; 

- allow user corrections; 

- manage learned preferences. 

Important preference changes should be validated and persisted by the backend. 

#### **4.4 Jobs** 

|`GET`<br>`GET`|`/jobs`<br>`/jobs /{ job_id}`|
|---|---|



Responsibilities: 

- retrieve available jobs; 

Page 3 of 8 

API Specification 

HeeraMon 

- retrieve detailed job information; 

- support filtering and pagination. 

Users should not directly control internal ingestion operations through public endpoints. 

#### **4.5 Matches** 

|`GET`|`/matches`|
|---|---|
|`GET`|`/matches /{ match_id}`|
|`POST`|`/matches /{ match_id }/ decision`|



Responsibilities: 

- retrieve relevant opportunities; 

- inspect match explanations; 

- record user decisions. 

#### **4.6 Notifications** 

|`GET`|`/notifications`|
|---|---|
|`PATCH`|`/notifications /{ notification_id }`|



Responsibilities: 

- retrieve notifications; 

- mark notifications as read; 

- expose notification status. 

#### **4.7 Applications** 

|`POST`|`/applications`|
|---|---|
|`GET`|`/applications`|
|`GET`|`/applications /{ application_id }`|
|`PATCH`|`/applications /{ application_id}`|
|`POST`|`/applications /{ application_id }/ prepare`|
|`POST`|`/applications /{ application_id }/ approve`|
|`POST`|`/applications /{ application_id }/ cancel`|



#### Responsibilities: 

- create application workflows; 

- prepare application information; 

- retrieve application state; 

- allow editing; 

- handle explicit approval; 

- cancel applications. 

Page 4 of 8 

API Specification 

HeeraMon 

The approve operation must be enforced by backend logic as the human-approval boundary. 

### **5 Background Operations** 

Internal background workers may use private service interfaces for: 

- job ingestion; 

- job normalization; 

- deduplication; 

- matching; 

- notification generation; 

- scheduled searches; 

- agent tasks. 

These operations do not need to be exposed as public user-facing endpoints. 

### **6 Request and Response Design** 

Responses should use consistent structured formats. 

Example: 

```
{
"data ":{},
"error ":null ,
"meta ":{}
}
```

Successful responses should provide the requested resource or operation result. 

Errors should provide enough information for the frontend to recover without exposing sensitive internal details. 

### **7 Pagination** 

Collection endpoints should support pagination. 

Examples: 

```
GET/jobs?page =1& limit =20
GET/matches?page =1& limit =20
GET/ notifications?page =1& limit =20
```

The API should avoid returning unnecessarily large datasets. 

Cursor-based pagination may be introduced later where required by scale. 

Page 5 of 8 

API Specification 

HeeraMon 

### **8 Validation** 

The backend should validate: 

- request structure; 

- field types; 

- allowed values; 

- resource ownership; 

- application state transitions; 

- required fields. 

LLM-generated structured output must also be validated before being persisted or used for consequential actions. 

### **9 Error Handling** 

The API should use appropriate HTTP status codes and consistent error structures. Common cases include: 

|`400`|`Invalid`<br>`request`|
|---|---|
|`401`|`Unauthenticated`|
|`403`|`Unauthorized`|
|`404`|`Resource`<br>`not found`|
|`409`|`Invalid`<br>`state/conflict`|
|`422`|`Validation`<br>`error`|
|`429`|`Rate`<br>`limited`|
|`500`|`Internal`<br>`server`<br>`error`|
|`503`|`External`<br>`service`<br>`unavailable`|



Errors should be safe for users while detailed internal information is logged server-side. 

### **10 Rate Limiting** 

Rate limiting should protect: 

- public endpoints; 

- authentication-related operations; 

- expensive agent operations; 

- job searches; 

- application workflows. 

Limits should be configurable rather than hard-coded throughout the application. 

Page 6 of 8 

API Specification 

HeeraMon 

### **11 API and Agent Boundary** 

The LLM agent should not receive unrestricted API or database access. Instead: 

**Agent** _→_ **Approved Tool** _→_ **Backend Service** _→_ **Database / External Service** Tools should expose only the operations required for the current task. 

This ensures that agent reasoning remains separated from application authorization and business logic. 

### **12 Boundaries** 

The initial release does not require: 

- a public developer API; 

- third-party API keys for users; 

- GraphQL; 

- microservice-to-microservice APIs; 

- real-time WebSocket infrastructure unless required by the implementation; 

- extensive API documentation portals. 

OpenAPI documentation should nevertheless be generated for the internal REST API. 

### **13 Success Criteria** 

The API is successful when it can securely support: 

1. Authentication and user access. 

2. Conversations with HeeraMon. 

3. Preference management. 

4. Job retrieval. 

5. Match retrieval and decisions. 

6. Notifications. 

7. Application preparation and review. 

8. Explicit application approval. 

9. Background service operations. 

**Core principle:** The API is the controlled boundary between HeeraMon’s interface, agent, persistent data, and external systems. 

Page 7 of 8 

API Specification 

HeeraMon 

### **14 Document Control** 

**<mark>Version Date Author</mark>** **<u><mark>/</mark></u>** **<mark>Role Changes</mark>** 1.0 September 30, 2026 Product <u>/</u> Engineering Initial release ~~[dt~~ **Approval:** This document defines the API contract for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Posdon)<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 8 of 8 

