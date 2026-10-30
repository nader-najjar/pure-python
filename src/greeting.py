from pydantic import BaseModel, ConfigDict, Field


class Greeting(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", str_strip_whitespace=True)

    name: str = Field(min_length=1)

    def message(self) -> str:
        return f"Hello, {self.name}!"
