class Inventory:
    def __init__(self,stock=0):
        self.stock=stock
        print("새 상품이 등록되었습니다.")

    def get_stock(self):
        return self.stock

    def set_stock(self,amount):
        if amount>=0:
            self.amount=amount
        else:
            print('수량이 음수이면 안됨')

    def add_stock(self,amount):
        if amount>=0:
            self.stock+=amount
            print(f'{amount}개가 입고되었습니다.')
        else:
            print('0보다 큰 수량만 입고 가능')

    def remove_stock(self,amount):
        if self.stock>amount:
            self.stock-=amount
            print(f'{amount}개가 출고되었습니다.')
        else:
            print('현재 재고보다 많은 수량은 출고 불가')

item1=Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량",item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())
