from typing import List, Dict, Any
from backend.app.ingestion.base import JobSourceAdapter

class CuratedTechAdapter(JobSourceAdapter):
    @property
    def source_name(self) -> str:
        return "HeeraMon Curated Tech"

    @property
    def source_type(self) -> str:
        return "curated"

    async def fetch_jobs(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": "curated-001",
                "title": "Junior AI/ML Engineer",
                "company": "CognitiveBD Labs",
                "location": "Gulshan-1, Dhaka",
                "work_arrangement": "hybrid",
                "employment_type": "full-time",
                "salary_min": 45000.0,
                "salary_max": 55000.0,
                "salary_currency": "BDT",
                "commute_time_minutes": 35,
                "workday_hours": 7.5,
                "required_skills": ["Python", "PyTorch", "FastAPI", "NLP", "Scikit-Learn"],
                "benefits": ["Subsidized lunch & snacks", "Health coverage", "Annual performance bonus", "Weekly knowledge shares"],
                "culture_notes": "Warm, collaborative culture with flat hierarchy and supportive mentorship.",
                "description": "Join our AI research and deployment squad building specialized NLP solutions for regional languages. Looking for passionate problem solvers eager to advance machine learning applications.",
                "application_url": "https://cognitivebd.example.com/careers/ai-ml-junior"
            },
            {
                "id": "curated-002",
                "title": "Machine Learning Engineer",
                "company": "NeuralApex Technologies",
                "location": "Banani, Dhaka",
                "work_arrangement": "onsite",
                "employment_type": "full-time",
                "salary_min": 50000.0,
                "salary_max": 65000.0,
                "salary_currency": "BDT",
                "commute_time_minutes": 50,
                "workday_hours": 8.0,
                "required_skills": ["Python", "TensorFlow", "Computer Vision", "Docker"],
                "benefits": ["Full catered lunch", "Gym membership allowance", "Medical insurance"],
                "culture_notes": "High intensity, ambitious product development team oriented around fast delivery.",
                "description": "We are seeking a Machine Learning Engineer to work on computer vision pipelines and real-time edge inference systems.",
                "application_url": "https://neuralapex.example.com/jobs/ml-eng"
            },
            {
                "id": "curated-003",
                "title": "Remote Python Backend Developer",
                "company": "CloudForge Global",
                "location": "Remote (Global / South Asia)",
                "work_arrangement": "remote",
                "employment_type": "full-time",
                "salary_min": 60000.0,
                "salary_max": 80000.0,
                "salary_currency": "BDT",
                "commute_time_minutes": 0,
                "workday_hours": 7.0,
                "required_skills": ["Python", "FastAPI", "PostgreSQL", "Docker", "AsyncIO"],
                "benefits": ["Remote work stipend", "Flexible core hours", "Generous annual leave", "Health reimbursement"],
                "culture_notes": "Asynchronous-first culture with deep respect for work-life boundary and deep work blocks.",
                "description": "CloudForge builds developer tools and orchestration APIs. You will design, build, and maintain mission-critical backend services with high concurrency.",
                "application_url": "https://cloudforge.example.com/join-us/backend-python"
            },
            {
                "id": "curated-004",
                "title": "Full Stack Software Engineer",
                "company": "SonarPulse Health",
                "location": "Dhanmondi, Dhaka",
                "work_arrangement": "hybrid",
                "employment_type": "full-time",
                "salary_min": 42000.0,
                "salary_max": 52000.0,
                "salary_currency": "BDT",
                "commute_time_minutes": 25,
                "workday_hours": 7.0,
                "required_skills": ["React", "TypeScript", "Node.js", "PostgreSQL", "Tailwind CSS"],
                "benefits": ["Subsidized lunch", "Flexible arrival window (9-10 AM)", "Festival bonuses"],
                "culture_notes": "Friendly, empathetic healthcare technology team emphasizing patient outcome impact and developer well-being.",
                "description": "Help us build responsive healthcare communication interfaces and clinical workflow applications serving clinics nationwide.",
                "application_url": "https://sonarpulse.example.com/careers/fullstack-eng"
            },
            {
                "id": "curated-005",
                "title": "Data Scientist & AI Researcher",
                "company": "Bengal Insight Labs",
                "location": "Mohakhali, Dhaka",
                "work_arrangement": "hybrid",
                "employment_type": "full-time",
                "salary_min": 55000.0,
                "salary_max": 75000.0,
                "salary_currency": "BDT",
                "commute_time_minutes": 40,
                "workday_hours": 7.5,
                "required_skills": ["Python", "Pandas", "Scikit-Learn", "LLM fine-tuning", "SQL"],
                "benefits": ["Subsidized cafeteria", "Conference attendance sponsorships", "Health coverage"],
                "culture_notes": "Research oriented, encouraging open experimentation and publication.",
                "description": "Bengal Insight Labs is exploring domain-specific language modeling and predictive analytics for logistics and market analysis.",
                "application_url": "https://bengalinsight.example.com/jobs/data-scientist"
            }
        ]

    def normalize_job(self, raw_job: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "title": raw_job.get("title", "Software Engineer"),
            "company": raw_job.get("company", "Tech Company"),
            "description": raw_job.get("description", ""),
            "location": raw_job.get("location", "Remote"),
            "work_arrangement": raw_job.get("work_arrangement", "remote"),
            "employment_type": raw_job.get("employment_type", "full-time"),
            "salary_min": raw_job.get("salary_min"),
            "salary_max": raw_job.get("salary_max"),
            "salary_currency": raw_job.get("salary_currency", "BDT"),
            "commute_time_minutes": raw_job.get("commute_time_minutes"),
            "workday_hours": raw_job.get("workday_hours", 8.0),
            "required_skills": raw_job.get("required_skills", []),
            "benefits": raw_job.get("benefits", []),
            "culture_notes": raw_job.get("culture_notes", ""),
            "application_url": raw_job.get("application_url", ""),
            "external_id": str(raw_job.get("id"))
        }
