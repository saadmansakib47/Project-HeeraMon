from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseLLMProvider(ABC):
    @abstractmethod
    async def extract_preferences(
        self, 
        message: str, 
        existing_preferences: Optional[List[Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        """
        Extract structured preferences from natural language.
        Each extracted preference dict contains:
        category, value, preference_type ('hard'|'soft'), confidence, raw_query
        """
        pass

    @abstractmethod
    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        preferences: List[Dict[str, Any]],
        recent_matches: List[Dict[str, Any]],
        user_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate conversational response embodying HeeraMon bird advisor persona.
        Returns dict with:
        - content: str
        - suggested_chips: List[str]
        - clarification_needed: Optional[str]
        """
        pass

    @abstractmethod
    async def evaluate_tradeoffs(
        self,
        job: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluate job against preferences and generate:
        - satisfied: List[str]
        - violated: List[str]
        - unknown: List[str]
        - trade_offs: List[str]
        - explanation: str
        - score: float (0.0 to 100.0)
        """
        pass

    @abstractmethod
    async def draft_application_package(
        self,
        job: Dict[str, Any],
        user_profile: Dict[str, Any],
        preferences: List[Dict[str, Any]]
    ) -> Dict[str, str]:
        """
        Draft tailored cover letter and alignment notes without inventing ungrounded facts.
        """
        pass
