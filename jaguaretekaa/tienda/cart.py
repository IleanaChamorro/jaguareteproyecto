class Cart:
    def __init(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session["cart"]={}
        self.cart = cart

    def add_product(self, product):
        if (str(product.id) not in self.carro.keys()):
            self.cart[product.id] = {
                "id_product": product.id,
                "name": product.name,
                "price": product.price,
                "amount": product.amount,
            }
