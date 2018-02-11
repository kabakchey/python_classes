####################################################################
class Item(object):

    _total_count = 0

    # ---------------------------------------------------------------
    def __init__(self, name, purchase_price=0, sale_price=0):

        Item._total_count += 1
        self.id = Item._total_count
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price

    # ---------------------------------------------------------------
    def __str__(self):
        return "Item (ID: %d, Name: %s, Sale price: %d)" % (self.id, self.name, self.sale_price)


##################################################################
class Food(Item):

    # ---------------------------------------------------------------
    def __init__(self, name, purchase_price=0, sale_price=0, expire_date=None):
        super().__init__(name, purchase_price, sale_price)
        self.expire_date = expire_date

    # ---------------------------------------------------------------
    def __str__(self):
        return "%s, Exp. date: %s" % (super().__str__(), self.expire_date)
