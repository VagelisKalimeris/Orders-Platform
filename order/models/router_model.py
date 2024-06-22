from enum import Enum

from pydantic import BaseModel, Field


class OrderInput(BaseModel):
    stoks: str = Field(
        description="Currency pair symbol (e.g. 'EURUSD'), or any other stuff",
        json_schema_extra={'example': 'EURUSD'}
    )
    quantity: float = Field(
        description='Quantity of the currency pair to be traded',
        json_schema_extra={'example': 55.5}
    )


class Status(Enum):
    pending = 'pending'
    executed = 'executed'
    canceled = 'canceled'


class OrderOutput(BaseModel):
    id: str = Field(
        description='Unique identifier for the order',
        json_schema_extra={'example': '3a051d9d-5932-4b40-8c61-e2ebb673bd31'},
    )
    stoks: str = Field(
        description="Currency pair symbol (e.g. 'EURUSD')",
        json_schema_extra={'example': 'EURUSD'}
    )
    quantity: float = Field(
        description='Quantity of the currency pair to be traded',
        json_schema_extra={'example': 55.5}
    )
    status: Status = Field(
        description='Status of the order',
        json_schema_extra={'example': Status.executed}
    )


class Error(BaseModel):
    code: int = Field(
        description='Error code',
        json_schema_extra={'example': 404}
    )
    message: str = Field(
        description='Error message',
        json_schema_extra={'example': 'Order not found'}
    )
