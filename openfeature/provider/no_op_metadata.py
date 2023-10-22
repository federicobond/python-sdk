from dataclasses import dataclass

from openfeature.provider import Metadata


@dataclass
class NoOpMetadata(Metadata):
    name: str = "No-op Provider"
    is_default_provider: bool = True
