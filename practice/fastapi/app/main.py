from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from datetime import datetime

app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "World"}


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    # UUID : Universally Unique Identifier
    name: str
    price: float


class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    products: List[Product] = Field(default_factory=list)  # 최초에 빈 list를 만들어서 저장한다.
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @property
    def bill(self):
        return sum([product.price for product in self.products])


orders = []

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

# TODO: 주문 구현, 상품 구현, 결제 구현
# TODO: 주문(Order) = Rquest
# TODO: 상품(Product)  = 마스크 분류모델 결과
# TODO: 결제 = Order.bill
# 2개의 컴포넌트
# TODO: Order, Product Class 구현
# TODO: Order의 products 필드로 Product의 LIST(하나의 주문에 여러 제품이 있을 수 있음)

# TODO: get_orders(GET) : get all Orders
# TODO: get_order(GET) : get an Order using order_id
# TODO: get_order_by_id : function to use in get_order()
# TODO: make_order(POST) : predict after load model, config => get into Order products, then return
# TODO: update_order(PATCH): order_id를 사용해 order를 가져온 후, update
# TODO: update_order_by_id : update_order에서 사용할 함수.
# TODO: get_bill(GET) : order_id를 사용해 order를 가져온 후, order.bill return
