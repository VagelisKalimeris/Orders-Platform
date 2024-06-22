from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import exc

from order.models.router_model import Error
from order.models.sqlalchemy_models import Order
from order.repositories.db_repository.depends import get_db


class DBAccess:
    def get_all_db_orders(self, db: Session = Depends(get_db)):
        return

    def get_specific_db_order(self, db: Session = Depends(get_db)):
        pass

    async def add_db_order(self, stoks, quantity, db: Session = Depends(get_db)):
        try:
            new_order = Order(stoks=stoks, quantity=quantity)
            db.add(new_order)
            return await db.commit()
        except exc.SQLAlchemyError as e:
            db.rollback()
            return Error(message=e.args[0], code=500)

    def remove_db_order(self, db: Session = Depends(get_db)):
        pass
