from enum import Enum


class Language(Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    RUBY = "ruby"
    UNKNOWN = "unknown"


class EmbeddingsModel(Enum):
    INSTRUCTOR_LARGE = "Instructor-Large"


class LlmHost(Enum):
    LLAMACPP = "Llamacpp"
    OLLAMA = "Ollama"