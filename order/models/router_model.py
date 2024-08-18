from enum import Enum

from pydantic import BaseModel, Field


class OrderInput(BaseModel):
    item: str = Field(
        description='Order item name',
        json_schema_extra={'example': 'bananas'}
    )
    quantity: int = Field(
        description='Quantity of the item to be ordered',
        json_schema_extra={'example': 55}
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
    item: str = Field(
        description='Order item name',
        json_schema_extra={'example': 'bananas'}
    )
    quantity: int = Field(
        description='Quantity of the item to be ordered',
        json_schema_extra={'example': 55}
    )
    status: Status = Field(
        description='Status of the order',
        json_schema_extra={'example': Status.executed}
    )
