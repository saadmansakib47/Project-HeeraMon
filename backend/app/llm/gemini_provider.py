import json
import httpx
from typing import List, Dict, Any, Optional
from backend.app.config import settings
from backend.app.llm.base import BaseLLMProvider
from backend.app.llm.mock_provider import MockLLMProvider

class GeminiLLMProvider(BaseLLMProvider):
    """
    Google Gemini LLM Provider with automatic fallback to MockLLMProvider
    if no API key is set or if rate limits occur.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.fallback = MockLLMProvider()

    async def extract_preferences(
        self, 
        message: str, 
        existing_preferences: Optional[List[Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        if not self.api_key:
            return await self.fallback.extract_preferences(message, existing_preferences)

        prompt = f"""You are HeeraMon's preference parser. Extract job and lifestyle preferences from this user statement:
"{message}"

Return a valid JSON array of objects with the following schema:
[
  {{
    "category": "salary|role|location|work_arrangement|hours|culture|benefits|commute",
    "value": "string value",
    "preference_type": "hard" | "soft",
    "confidence": 0.0 - 1.0,
    "raw_query": "phrase from input"
  }}
]
Only return JSON, no markdown formatting or extra text."""

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.2, "response_mime_type": "application/json"}
                }
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return json.loads(text)
        except Exception:
            pass
        return await self.fallback.extract_preferences(message, existing_preferences)

    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        preferences: List[Dict[str, Any]],
        recent_matches: List[Dict[str, Any]],
        user_name: Optional[str] = "Comrade"
    ) -> Dict[str, Any]:
        # If no key, fallback
        if not self.api_key:
            return await self.fallback.generate_response(user_message, conversation_history, preferences, recent_matches, user_name)

        prompt = f"""You are HeeraMon, an AI job-seeking wisdom bird inspired by folklore.
You advise the user thoughtfully, honestly explaining trade-offs, valuing work-life harmony, and upholding human-in-the-loop control.
User: {user_name}
User Message: {user_message}
Understood Preferences: {json.dumps(preferences)}
Recent Job Matches: {json.dumps(recent_matches[:2] if recent_matches else [])}

Generate a JSON object:
{{
  "content": "Conversational advice and observations in your wise, calm voice",
  "suggested_chips": ["2 to 4 quick action chips"],
  "clarification_needed": null or "clarification question"
}}"""

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.5, "response_mime_type": "application/json"}
                }
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return json.loads(text)
        except Exception:
            pass
        return await self.fallback.generate_response(user_message, conversation_history, preferences, recent_matches, user_name)

    async def evaluate_tradeoffs(
        self,
        job: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        return await self.fallback.evaluate_tradeoffs(job, preferences)

    async def draft_application_package(
        self,
        job: Dict[str, Any],
        user_profile: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, str]:
        return await self.fallback.draft_application_package(job, user_profile, preferences)
