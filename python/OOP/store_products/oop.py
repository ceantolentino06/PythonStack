class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        print("Product Name:",self.products[id].name,"Price:",self.products[id].price, "Category:", self.products[id].category)
        self.products.pop(id)

    def printAllProducts(self):
        for val in self.products:
            print("Product Name:",val.name,"Price:",val.price, "Category:", val.category)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change

# phone = Product("apple", 400, "mobile")
# phone.update_price(0.20, True)
# print(phone.price)

bestbuy = Store("Phone store")
bestbuy.add_product(Product("Apple", 400, "Mobile"))
bestbuy.add_product(Product("Samsung", 300, "Mobile"))
bestbuy.add_product(Product("Sony", 800, "TV"))
bestbuy.products[0].update_price(0.20, True)
print(bestbuy.products[0].price)
bestbuy.printAllProducts()
# print(len(bestbuy.products))

