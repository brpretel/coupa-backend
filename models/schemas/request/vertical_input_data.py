from pydantic import BaseModel


class VerticalCreateRequest(BaseModel):
    vertical_name: str
