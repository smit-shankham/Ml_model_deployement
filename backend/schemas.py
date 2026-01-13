from pydantic import BaseModel, Field, validator
from typing import Optional

class HouseFeatures(BaseModel):
    CRIM: Optional[float] = Field(None, ge=0)
    ZN: Optional[float] = Field(None, ge=0)
    INDUS: Optional[float] = Field(None, ge=0)
    CHAS: Optional[int] = Field(None, ge=0, le=1)
    NOX: Optional[float] = Field(None, ge=0, le=1)
    RM: Optional[float] = Field(None, ge=1)
    AGE: Optional[float] = Field(None, ge=0, le=100)
    DIS: Optional[float] = Field(None, gt=0)
    RAD: Optional[int] = Field(None, ge=1)
    TAX: Optional[float] = Field(None, ge=0)
    PTRATIO: Optional[float] = Field(None, ge=0)
    B: Optional[float] = Field(None, ge=0)
    LSTAT: Optional[float] = Field(None, ge=0)

    @validator("*")
    def no_nan_or_inf(cls, v):
        if v is None:
            return v
        if not float("-inf") < float(v) < float("inf"):
            raise ValueError("Invalid numeric value")
        return v
