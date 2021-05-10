from pydantic import BaseModel


class TestInfo(BaseModel):
    input: str
