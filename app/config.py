from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ollama_base_url: str = "http://localhost:11434"
    primary_model: str = "qwen2.5:7b"
    fallback_model: str = "qwen2.5:7b"

    langchain_tracking:bool = True
    langchain_api_key:str = ""
    langchain_project: str = "production-api"

    app_env:str="development"
    log_level:str="INFO"
    rate_limit:bool = "20/minute"
    cache_ttl_seconds:int = 300
    max_retries:int = 3

    model_config = {"env_file":".env","extra":"ignore"}
    @property
    def is_production(self):
        return self.app_env == "production"

@lru_cache
def get_settings()->Settings:
    return Settings()