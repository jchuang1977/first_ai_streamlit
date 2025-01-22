from langchain_core.pydantic_v1 import BaseModel, Field
#from pydantic import BaseModel,Field
from typing import List

class Xiaohongshu(BaseModel):
    titles: List[str] = Field(description="影片的5個標題", min_items=5, max_items=5)
    content: str = Field(description="影片的正文內容")