from typing import Any, Dict, List

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    Summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.Summary, "facts": self.facts}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
