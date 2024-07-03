from typing import Union
from pydantic import BaseModel

from typing import Generic, List, TypeVar, Optional
from pydantic import BaseModel, Field
        
################# APIS ###################
## Common
class BaseRequest(BaseModel):
    sessionId: str
    userId: Optional[str] = ''

class BaseResponse(BaseModel):
    result_cd: int
    result_msg: str

class QueryRequest(BaseRequest):
    corpCd: str
    locale: str
    platform: str
    query: str
