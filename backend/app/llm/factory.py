from backend.app.config import settings
from backend.app.llm.base import BaseLLMProvider
from backend.app.llm.mock_provider import MockLLMProvider
from backend.app.llm.gemini_provider import GeminiLLMProvider

def get_llm_provider() -> BaseLLMProvider:
    if settings.LLM_PROVIDER.lower() == "gemini" and settings.GEMINI_API_KEY:
        return GeminiLLMProvider(api_key=settings.GEMINI_API_KEY)
    # Default to robust Mock provider for offline reliability and deterministic testing
    return MockLLMProvider()
