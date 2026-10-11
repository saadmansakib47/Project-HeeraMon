

<!-- Start of picture text -->
gen<br><!-- End of picture text -->

# **HeeraMon** 

## **UI / UX Specification** 

UI / UX Specification Document 

**Date of Preparation** : September 30, 2026 

|**Document ID**|HM-DOC-09|
|---|---|
|**Title**|UI / UX Specification|
|**Classification**|UI / UX Specification Document|
|**Status**|Draft|
|**Version**|1.0|
|**Owner**|Product / Engineering|
|**Audience**|All project contributors|
|**Related**<br>**Docu-**<br>**ments**|Product Vision (HM-DOC-01), User Journeys (HM-<br>DOC-03)|



## **Contents** 

|**1**|**Pu**|**rpose**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**2**|
|---|---|---|---|
|**2**|**UX**|**Philosophy** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**2**|
|**3**|**Des**|**ign Principles**. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**2**|
||3.1|Minimalistic . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>2|
||3.2|Conversational First<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.3|Progressive Disclosure<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.4|Explainability . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
||3.5|Human Approval . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>3|
|**4**|**Vis**|**ual Identity** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**4**|
||4.1|Theme . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||4.2|Typography . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
||4.3|Components . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>4|
|**5**|**Th**|**e Bird Character** . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**5**|
|**6**|**Ma**|**in Screens** . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**5**|
||6.1|Screen 1 — Landing / Home . . . . . . . . . . . . . .|. . . . . . . . . . .<br>5|
||6.2|Screen 2 — Conversation View<br>. . . . . . . . . . . .|. . . . . . . . . . .<br>6|
||6.3|Screen 3 — Preferences View<br>. . . . . . . . . . . . .|. . . . . . . . . . .<br>6|
||6.4|Screen 4 — Opportunity View . . . . . . . . . . . . .|. . . . . . . . . . .<br>6|
||6.5|Screen 5 — Job Detail View . . . . . . . . . . . . . .|. . . . . . . . . . .<br>7|
||6.6|Screen 6 — Notification Center<br>. . . . . . . . . . . .|. . . . . . . . . . .<br>7|
||6.7|Screen 7 — Application Review . . . . . . . . . . . .|. . . . . . . . . . .<br>7|
|**7**|**Em**|**pty States** . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**8**|**Loa**|**ding States** . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**9**|**Err**|**or States** . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**8**|
|**10 **|**Acc**|**essibility** . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**9**|
|**11 **|**Sug**|**gested Screen Layout** . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**9**|
|**12 **|**Bo**|**undaries**<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**10**|
|**13 **|**Suc**|**cess Criteria**<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**10**|
|**14 **|**Do**|**cument Control** . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>**10**|



1 

UI <u>/</u> UX Specification 

HeeraMon 

### **1 Purpose** 

This document defines the visual language, interaction principles, screens, and user experience goals for HeeraMon. 

The goal is not to specify pixel-perfect layouts, but to provide sufficient guidance so that frontend implementation remains consistent, minimalistic, and aligned with the product philosophy. 

This document serves as the textual equivalent of early wireframes. 

### **2 UX Philosophy** 

HeeraMon should feel: 

- calm; 

- intelligent; 

- minimal; 

- premium; 

- conversational; 

- trustworthy. 

The interface should reduce complexity rather than expose it. 

Users should feel that: 

_“I am talking to a thoughtful assistant that understands what I want.”_ 

rather than: 

_“I am filling a complicated recruitment form.”_ 

### **3 Design Principles** 

#### **3.1 Minimalistic** 

Only important information should appear. 

Avoid: 

- dashboard overload; 

- excessive menus; 

- unnecessary metrics; 

- clutter. 

Complexity should remain inside the system. 

Page 2 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

#### **3.2 Conversational First** 

Conversation is the primary interface. 

Structured controls may exist where useful, but should support conversation rather than replace it. 

Examples: 

- edit preference button; 

- approve application button; 

- notification list; 

- saved jobs. 

#### **3.3 Progressive Disclosure** 

Show information gradually. 

Example: 

#### **Initial:** 

_“I found a close match.”_ 

#### **Expanded:** 

- salary; 

- location; 

- commute; 

- trade-offs; 

- company information. 

The user should not be overwhelmed. 

#### **3.4 Explainability** 

Important recommendations should include: 

- what fits; 

- what does not fit; 

- what is unknown; 

- why the job was shown. 

#### **3.5 Human Approval** 

Consequential actions should always include review steps. 

Examples: 

- application review; 

Page 3 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

- profile update; 

- external submission. 

- **4 Visual Identity** 

#### **4.1 Theme** 

HeeraMon should appear: 

- clean; 

- modern; 

- premium; 

- calm. 

Preferred style: 

- white background; 

- black text; 

- subtle gray elements; 

- minimal accent colors; 

- soft shadows; 

- moderate spacing; 

- rounded corners. 

#### **4.2 Typography** 

Preferred: 

- Nunito 

- modern sans-serif fonts 

Characteristics: 

- readable; 

- friendly; 

- professional. 

#### **4.3 Components** 

Suggested style: 

#### **Buttons:** 

- black background + white text 

- white background + black border 

Page 4 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

#### **Cards:** 

- white 

- black border or subtle shadow 

**Corner radius:** approximately 10–12 px 

**Animations:** subtle and purposeful 

### **5 The Bird Character** 

The bird is HeeraMon’s personality layer. 

The bird should: 

- feel helpful; 

- feel calm; 

- avoid becoming distracting; 

- support conversation. 

Possible interactions: 

- entering the screen during onboarding; 

- small wing movement; 

- speech bubble; 

- subtle reactions. 

The bird should never dominate the interface. 

The user comes for jobs, not animation. 

### **6 Main Screens** 

#### **6.1 Screen 1 — Landing / Home** 

**Purpose:** Introduce HeeraMon. 

Contains: 

- HeeraMon bird 

- greeting 

- primary text input 

- sign in option 

Example: 

_“Describe your dream job and I will find it for you.”_ 

Page 5 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

#### **6.2 Screen 2 — Conversation View** 

**Purpose:** Main interaction area. 

Contains: 

- conversation history 

- user messages 

- HeeraMon responses 

- suggestion chips 

- notifications where relevant 

This is the primary product surface. 

#### **6.3 Screen 3 — Preferences View** 

**Purpose:** Allow visibility and editing. 

Sections: 

- hard requirements 

- soft preferences 

- learned preferences 

Users should understand: 

- what HeeraMon knows; 

- what HeeraMon inferred; 

- what is uncertain. 

#### **6.4 Screen 4 — Opportunity View** 

**Purpose:** Display a job. 

Contains: 

- title 

- company 

- salary 

- location 

- work arrangement 

- trade-offs 

- explanation 

- actions 

Actions: 

Page 6 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

- save 

- reject 

- investigate 

- proceed 

#### **6.5 Screen 5 — Job Detail View** 

**Purpose:** Deep inspection. 

Contains: 

- description 

- requirements 

- benefits 

- application details 

- HeeraMon explanation 

#### **6.6 Screen 6 — Notification Center** 

Examples: 

- new match; 

- close match; 

- application ready; 

- search updates. 

Notifications should remain concise. 

#### **6.7 Screen 7 — Application Review** 

**Purpose:** Human approval. 

Contains: 

- CV; 

- profile information; 

- application answers; 

- editable fields; 

- approve button; 

- cancel button. 

Approval should be deliberate. 

Page 7 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

### **7 Empty States** 

Examples: 

#### **No jobs:** 

_“I’m still searching. I’ll let you know when I find something promising.”_ 

#### **No preferences:** 

_“Tell me what kind of work you want.”_ 

#### **No notifications:** 

_“Nothing important right now.”_ 

Empty states should feel natural rather than mechanical. 

### **8 Loading States** 

Examples: 

#### **Searching:** 

_“Looking for new opportunities...”_ 

#### **Analyzing:** 

_“Comparing this opportunity with your preferences...”_ 

#### **Preparing application:** 

_“Preparing information for review...”_ 

Users should understand what HeeraMon is doing. 

### **9 Error States** 

Examples: 

#### **Source unavailable:** 

_“I couldn’t reach one of my job sources. I’ll try again later.”_ 

#### **Missing information:** 

_“This company did not provide salary information.”_ 

#### **Application failure:** 

_“The application could not be completed. Nothing was submitted.”_ 

Errors should be: 

- understandable; 

Page 8 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

- recoverable; 

- transparent. 

### **10 Accessibility** 

The interface should consider: 

- keyboard navigation; 

- readable contrast; 

- mobile use; 

- screen sizes; 

- responsive layouts; 

- reduced motion preferences. 

Accessibility should be considered from the start. 

### **11 Suggested Screen Layout** 

The following conceptual layout guides the primary conversational interface. It is illustrative rather than a rigid constraint. 

|`+-`|`-------------`|`-----------------------------------`|`-+`|
|---|---|---|---|
|`|`|`HeeraMon`<br>`Log`|`o`<br>`Notifications`|`|`|
|`+-`|`-------------`|`-----------------------------------`|`-+`|
|`|`|||`|`|
|`|`||`[Bird]`|`|`|
|`|`|||`|`|
|`|`|`"Descr`|`ibe`<br>`your`<br>`dream job`|`|`|
|`|`|`and I `|`will find it for you."`|`|`|
|`|`<br>`+-`|`-------------`|`-----------------------------------`|`|`<br>`-+`|
|`|`|`Conversation`|`Area`|`|`|
|`|`|||`|`|
|`|`|`User: I want `|`AI/ML , 40k, short`<br>`commute.`|`|`|
|`|`|||`|`|
|`|`|`HeeraMon: I `|`found a close`<br>`match ...`|`|`|
|`|`<br>`+-`|`-------------`|`-----------------------------------`|`|`<br>`-+`|
|`|`<br>`+-`|`[ Text`<br>`Input`<br>`-------------`|`.............................. ]`<br>`-----------------------------------`|`|`<br>`-+`|
|`|`|`Quick`<br>`Action`|`s`|`|`|
|`|`<br>`+-`|`Preferences`<br>`-------------`|`|`<br>`Saved`<br>`Jobs`<br>`|`<br>`Notifications`<br>`-----------------------------------`|`|`<br>`-+`|



Key layout intentions: 

- Header remains light and unobtrusive. 

Page 9 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

- Conversation occupies the primary visual space. 

- Input is always reachable. 

- Quick actions support, rather than replace, conversation. 

- The bird appears as a calm presence, not a dominant element. 

### **12 Boundaries** 

The initial release does not require: 

- complex dashboards; 

- analytics panels; 

- excessive gamification; 

- many settings pages; 

- highly detailed visual customization; 

- heavy animation systems. 

The interface should remain: 

**simple** _→_ **conversational** _→_ **informative** _→_ **trustworthy** 

### **13 Success Criteria** 

The UI/UX is successful when users can: 

1. Understand HeeraMon quickly. 

2. Describe preferences naturally. 

3. View and modify preferences. 

4. Understand job recommendations. 

5. Recognize trade-offs. 

6. Make decisions easily. 

7. Review applications confidently. 

8. Feel that HeeraMon is assisting rather than complicating the process. 

**Core principle:** HeeraMon should feel less like a recruitment portal and more like a thoughtful companion helping users navigate their career decisions. 

### **14 Document Control** 

|**Version**|**Date**|**Author **|**/ Role**|**Changes**|
|---|---|---|---|---|
|1.0|September 30, 2026|Product /|Engineering|Initial release|



Page 10 of 11 

UI <u>/</u> UX Specification 

HeeraMon 

**Approval:** This document defines the UI/UX principles and screens for HeeraMon. All subsequent design and implementation work must remain consistent with the principles stated herein. 

_HeeraMon flies to help people find job that fits not only their career, but the life they want to live._ 



<!-- Start of picture text -->
Doodle<br><!-- End of picture text -->

**Saadman Sakib** Product Engineer 

Page 11 of 11 

