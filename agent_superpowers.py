# Zenith Agent Superpowers
# Authored by Sarvesh Zenith (Sarvesh Khandelwal / Dayal Infotech Services)

import abc
from typing import Any, Dict, List, Optional

class AgentTool(abc.ABC):
    """Abstract Base Class for Zenith Agent Tools."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abc.abstractmethod
    def execute(self, **kwargs: Any) -> Any:
        """Execute the tool action."""
        pass

class MemoryExtension(abc.ABC):
    """Abstract Base Class for Zenith Memory Extensions."""
    def __init__(self, memory_id: str):
        self.memory_id = memory_id

    @abc.abstractmethod
    def store(self, key: str, value: Any) -> None:
        """Store data into persistent memory."""
        pass

    @abc.abstractmethod
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve data from memory."""
        pass
