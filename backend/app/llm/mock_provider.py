import re
from typing import List, Dict, Any, Optional
from backend.app.llm.base import BaseLLMProvider

class MockLLMProvider(BaseLLMProvider):
    """
    Deterministic Heuristic AI Provider.
    Guarantees offline reliability, zero external cost, fast responses, 
    and complete fidelity to HeeraMon's design principles.
    """

    async def extract_preferences(
        self, 
        message: str, 
        existing_preferences: Optional[List[Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        extracted = []
        text_lower = message.lower()

        # 1. Salary extraction
        # e.g. "at least 40k BDT", "40k", "50,000 bdt", "minimum 35k"
        salary_match = re.search(r'(?:at least|minimum|around|about|approx)?\s*(\d{1,3}(?:[,\.]\d{3})*|\d+)\s*(k|thousand|bdt|usd|\$)', text_lower)
        if salary_match:
            raw_num = salary_match.group(1).replace(',', '')
            multiplier = 1000 if salary_match.group(2) in ('k', 'thousand') else 1
            num_val = int(float(raw_num) * multiplier)
            currency = "USD" if "$" in salary_match.group(0) or "usd" in salary_match.group(0) else "BDT"
            is_hard = any(kw in text_lower for kw in ["at least", "minimum", "must", "no less than", "strictly"])
            
            extracted.append({
                "category": "salary",
                "value": f"{num_val:,} {currency}",
                "preference_type": "hard" if is_hard else "soft",
                "confidence": 0.95,
                "raw_query": salary_match.group(0).strip()
            })

        # 2. Role extraction
        roles_catalog = [
            ("AI/ML Engineer", ["ai/ml", "ai & ml", "machine learning", "deep learning", "ai role", "ml engineer"]),
            ("Backend Engineer", ["backend", "python developer", "fastapi", "django", "node.js developer"]),
            ("Frontend Engineer", ["frontend", "front-end", "react", "next.js", "ui developer"]),
            ("Full Stack Developer", ["fullstack", "full stack", "full-stack"]),
            ("Data Scientist", ["data science", "data scientist", "data analyst"]),
            ("Mobile Developer", ["mobile developer", "flutter", "react native", "android"]),
            ("DevOps Engineer", ["devops", "cloud engineer", "infrastructure"])
        ]
        for role_name, keywords in roles_catalog:
            if any(kw in text_lower for kw in keywords):
                is_hard = "only" in text_lower or "must be" in text_lower
                extracted.append({
                    "category": "role",
                    "value": role_name,
                    "preference_type": "hard" if is_hard else "soft",
                    "confidence": 0.9,
                    "raw_query": role_name
                })
                break

        # 3. Work Arrangement (remote/hybrid/onsite)
        if "remote" in text_lower or "work from home" in text_lower:
            is_hard = "remote only" in text_lower or "strictly remote" in text_lower or "only remote" in text_lower
            extracted.append({
                "category": "work_arrangement",
                "value": "Remote",
                "preference_type": "hard" if is_hard else "soft",
                "confidence": 0.95,
                "raw_query": "remote"
            })
        elif "hybrid" in text_lower:
            extracted.append({
                "category": "work_arrangement",
                "value": "Hybrid",
                "preference_type": "soft",
                "confidence": 0.9,
                "raw_query": "hybrid"
            })
        elif "onsite" in text_lower or "on-site" in text_lower or "in office" in text_lower:
            extracted.append({
                "category": "work_arrangement",
                "value": "On-site",
                "preference_type": "soft",
                "confidence": 0.9,
                "raw_query": "on-site"
            })

        # 4. Commute time
        commute_match = re.search(r'(\d+)\s*(?:-|to)?\s*(\d+)?\s*(?:minute|min|hour|hr)s?\s*(?:commute|travel)?', text_lower)
        if commute_match and ("commute" in text_lower or "travel" in text_lower or "reach" in text_lower):
            mins = int(commute_match.group(1))
            if "hour" in commute_match.group(0) or "hr" in commute_match.group(0):
                mins = mins * 60
            extracted.append({
                "category": "commute",
                "value": f"Max {mins} mins",
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": commute_match.group(0).strip()
            })

        # 5. Work hours & Work-Life Balance
        hours_match = re.search(r'(\d+)\s*hours?\s*(?:a|per)?\s*(?:day)?', text_lower)
        if hours_match:
            hours = int(hours_match.group(1))
            extracted.append({
                "category": "hours",
                "value": f"~{hours} hours/day",
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": hours_match.group(0).strip()
            })
        elif "work-life balance" in text_lower or "work life balance" in text_lower or "life outside work" in text_lower:
            extracted.append({
                "category": "hours",
                "value": "Healthy work-life balance (~7-8h)",
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": "work-life balance"
            })

        # 6. Culture
        if any(kw in text_lower for kw in ["friendly", "no toxic", "good culture", "collaborative", "respectful", "peaceful"]):
            val = "Friendly & non-toxic workplace"
            if "learning" in text_lower:
                val += " with growth mindset"
            extracted.append({
                "category": "culture",
                "value": val,
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": "workplace culture"
            })

        # 7. Benefits / Perks
        if "lunch" in text_lower or "subsidized lunch" in text_lower or "free food" in text_lower:
            extracted.append({
                "category": "benefits",
                "value": "Subsidized or provided lunch",
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": "subsidized lunch"
            })
        if "insurance" in text_lower or "health" in text_lower:
            extracted.append({
                "category": "benefits",
                "value": "Health insurance",
                "preference_type": "soft",
                "confidence": 0.85,
                "raw_query": "health insurance"
            })

        # 8. Location
        locations = ["Dhaka", "Gulshan", "Banani", "Dhanmondi", "Mohakhali", "Uttara", "Chittagong", "Sylhet"]
        for loc in locations:
            if loc.lower() in text_lower:
                extracted.append({
                    "category": "location",
                    "value": loc,
                    "preference_type": "soft",
                    "confidence": 0.9,
                    "raw_query": loc
                })
                break

        return extracted

    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        preferences: List[Dict[str, Any]],
        recent_matches: List[Dict[str, Any]],
        user_name: Optional[str] = "Comrade"
    ) -> Dict[str, Any]:
        """
        Embody the mythical HeeraMon bird persona: calm, perceptive, articulate,
        advising with care and clarity before crucial career steps.
        """
        user_name = user_name or "Comrade"
        
        pref_summaries = [f"**{p['category'].title()}**: {p['value']} ({p['preference_type']})" for p in preferences]
        pref_str = ", ".join(pref_summaries) if pref_summaries else "your criteria are still broad"

        if not preferences:
            content = (
                f"Greetings, {user_name}. I am HeeraMon, your wisdom bird in the search for meaningful work.\n\n"
                "Share with me in your own words what kind of career and life rhythm you seek. For example:\n"
                "*\"At least 40k BDT, AI/ML role, max 30-minute commute, around 7 hours a day, friendly workplace, and subsidized lunch.\"*\n\n"
                "I will remember what matters to you, seek out fitting opportunities, and explain every trade-off before you decide."
            )
            chips = [
                "AI/ML Engineer, min 45k BDT, Remote",
                "Full Stack Developer in Dhaka, flexible hours",
                "Remote Python Backend, healthy work-life balance"
            ]
            return {"content": content, "suggested_chips": chips, "clarification_needed": None}

        # If matches were found
        if recent_matches:
            top_match = recent_matches[0]
            job = top_match.get("job") or {}
            title = job.get("title", "Opportunity")
            company = job.get("company", "Company")
            score = top_match.get("score", 0)

            trade_offs_text = ""
            if top_match.get("trade_offs"):
                trade_offs_text = "\n\n**Notable Trade-offs to consider:**\n" + "\n".join(f"• {t}" for t in top_match["trade_offs"][:3])

            content = (
                f"I have surveyed the open horizon, {user_name}.\n\n"
                f"I discovered **{title}** at **{company}** (Fit rating: **{score:.0f}%**).\n\n"
                f"{top_match.get('explanation', '')}"
                f"{trade_offs_text}\n\n"
                "Would you like me to prepare an application package for this role, or explore other opportunities?"
            )
            chips = [
                "Prepare application package",
                "Show more details",
                "Show next best match",
                "Adjust my preferences"
            ]
            return {"content": content, "suggested_chips": chips, "clarification_needed": None}

        # No direct matches yet or just registered preferences
        content = (
            f"Understood with clarity, {user_name}. I have committed your preferences to memory:\n"
            + "\n".join([f"• **{p['category'].title()}**: {p['value']} *({p['preference_type']} condition)*" for p in preferences])
            + "\n\nI am now actively scouting our configured job sources. "
            "Whenever an opportunity surfaces, I will evaluate both hard requirements and subtle lifestyle trade-offs before presenting it to you."
        )
        chips = [
            "Find jobs matching now",
            "Set search frequency to daily",
            "Add another preference"
        ]
        return {"content": content, "suggested_chips": chips, "clarification_needed": None}

    async def evaluate_tradeoffs(
        self,
        job: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Deterministic matching and trade-off evaluation.
        """
        satisfied = []
        violated = []
        unknown = []
        trade_offs = []
        score = 70.0 # Base match baseline

        pref_map = {p["category"]: p for p in preferences}
        job_title = job.get("title", "").lower()
        job_desc = job.get("description", "").lower()
        job_salary_min = job.get("salary_min")
        job_salary_max = job.get("salary_max")
        job_commute = job.get("commute_time_minutes")
        job_workday = job.get("workday_hours")
        job_work_mode = job.get("work_arrangement", "").lower()

        # Check role
        if "role" in pref_map:
            p_val = pref_map["role"]["value"].lower()
            if any(term in job_title or term in job_desc for term in p_val.split()):
                satisfied.append(f"Role match: matches your target {pref_map['role']['value']}")
                score += 15.0
            else:
                violated.append(f"Role difference: listing is titled '{job.get('title')}'")
                score -= 15.0

        # Check salary
        if "salary" in pref_map:
            p_val = pref_map["salary"]["value"]
            # Extract number
            nums = re.findall(r'\d+', p_val.replace(',', ''))
            if nums:
                min_desired = float(nums[0])
                if job_salary_min:
                    if job_salary_min >= min_desired:
                        satisfied.append(f"Salary meets expectations ({job_salary_min:,.0f} {job.get('salary_currency', 'BDT')})")
                        score += 15.0
                    elif job_salary_max and job_salary_max >= min_desired:
                        satisfied.append(f"Salary up to {job_salary_max:,.0f} {job.get('salary_currency', 'BDT')} overlaps your goal")
                        score += 10.0
                    else:
                        violated.append(f"Salary below preferred: offers ~{job_salary_min:,.0f} vs your desired {min_desired:,.0f}")
                        trade_offs.append(f"Compensates lower initial salary ({job_salary_min:,.0f}) with potential perks")
                        score -= 20.0
                else:
                    unknown.append("Exact salary package not stated in job posting")

        # Check Work Arrangement
        if "work_arrangement" in pref_map:
            p_mode = pref_map["work_arrangement"]["value"].lower()
            if p_mode in job_work_mode or job_work_mode == "remote":
                satisfied.append(f"Work arrangement ({job.get('work_arrangement')}) fits your preference")
                score += 10.0
            else:
                trade_offs.append(f"Work arrangement is {job.get('work_arrangement')} while you preferred {pref_map['work_arrangement']['value']}")
                score -= 10.0

        # Check Commute
        if "commute" in pref_map:
            if job_commute:
                p_mins = 30
                c_nums = re.findall(r'\d+', pref_map["commute"]["value"])
                if c_nums:
                    p_mins = int(c_nums[0])
                if job_commute <= p_mins:
                    satisfied.append(f"Commute is ~{job_commute} mins (well within your {p_mins} mins target)")
                    score += 10.0
                else:
                    trade_offs.append(f"Commute is ~{job_commute} mins, exceeding your preferred {p_mins} mins")
                    score -= 8.0
            elif job_work_mode == "remote":
                satisfied.append("Zero commute (Full Remote)")
                score += 10.0
            else:
                unknown.append("Specific commute duration unknown until office location confirmed")

        # Check Work hours
        if "hours" in pref_map:
            if job_workday:
                if job_workday <= 8:
                    satisfied.append(f"Standard {job_workday}h working day matches your balance preference")
                    score += 5.0
                else:
                    trade_offs.append(f"Workday can reach {job_workday} hours during peak sprints")
                    score -= 5.0
            else:
                unknown.append("Daily working hours not explicitly quantified")

        # Check Culture / Benefits
        if "benefits" in pref_map:
            job_benefits = [str(b).lower() for b in job.get("benefits", [])]
            if any("lunch" in b for b in job_benefits):
                satisfied.append("Subsidized/provided lunch confirmed in benefits")
                score += 5.0
            else:
                unknown.append("Subsidized lunch not explicitly mentioned in posting")

        score = max(20.0, min(100.0, score))
        eligibility = "eligible"
        if any("hard" == p.get("preference_type") and p.get("category") == "salary" for p in preferences):
            if any("Salary below preferred" in v for v in violated):
                eligibility = "ineligible"

        explanation = (
            f"This opportunity at {job.get('company')} is rated {score:.0f}% compatible. "
            f"It satisfies {len(satisfied)} of your priorities. "
        )
        if trade_offs:
            explanation += f"However, notice {len(trade_offs)} trade-off(s) regarding {' and '.join(t.split()[0].lower() for t in trade_offs)}."

        return {
            "score": round(score, 1),
            "eligibility_status": eligibility,
            "satisfied": satisfied,
            "violated": violated,
            "unknown": unknown,
            "trade_offs": trade_offs,
            "explanation": explanation
        }

    async def draft_application_package(
        self,
        job: Dict[str, Any],
        user_profile: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, str]:
        title = job.get("title", "Role")
        company = job.get("company", "Company")
        user_name = user_profile.get("name", "Applicant")
        user_email = user_profile.get("email", "applicant@example.com")
        skills = user_profile.get("skills", ["Python", "FastAPI", "Machine Learning", "System Design"])

        tailored_notes = (
            f"### Application Summary for {title} at {company}\n"
            f"• **Target Role**: {title}\n"
            f"• **Applicant**: {user_name} ({user_email})\n"
            f"• **Matching Competencies**: {', '.join(skills[:4])}\n"
            f"• **Work Mode Alignment**: Compatible with {job.get('work_arrangement', 'specified')} arrangement\n"
            f"• **Human-in-the-Loop Gate**: Prepared by HeeraMon. Requires explicit approval before transmission."
        )

        cover_letter = (
            f"Dear Hiring Team at {company},\n\n"
            f"I am writing to express my strong interest in the {title} position. "
            f"With a dedicated focus on building reliable software and leveraging modern engineering techniques, "
            f"I was drawn to {company}'s vision and technical direction.\n\n"
            f"My experience spans {', '.join(skills[:3])}, alongside an emphasis on clean architecture and collaborative teamwork. "
            f"I appreciate {company}'s commitment to engineering quality and would welcome the opportunity to discuss how my skill set aligns with your goals.\n\n"
            f"Thank you for your consideration.\n\n"
            f"Warm regards,\n"
            f"{user_name}\n"
            f"{user_email}"
        )

        return {
            "tailored_notes": tailored_notes,
            "cover_letter": cover_letter
        }
