import datetime
from store import Store

###################################################################
class SaleInvoice(object):

    __last_number = 1
    __FORMAT_HEADER   = "%-15s| %8s| %10s| %12s|"
    __FORMAT_ROW      = "%-15s| %8.2f| %10.2f| %12.2f|"

    class Record(object):
        def __init__(self, item, qty=0, price=0):
            self.item = item
            self.qty = qty
            self.price = price
            self.sum = self.qty * self.price

    # ---------------------------------------------------------------
    def __init__(self, store):

        self.number = SaleInvoice.__last_number
        self.date_time = datetime.datetime.now()
        self.store = store
        self.__records = {}

        SaleInvoice.__last_number += 1

    # ---------------------------------------------------------------
    def add_item(self, item, qty):
        record = self.__records.get(item, SaleInvoice.Record(item))
        record.qty += qty
        record.price = item.sale_price
        record.sum   = record.qty * record.price

        self.__records[item] = record

    # ---------------------------------------------------------------
    def remove_item(self, item, qty, sale_price):
        if item in self.__records:
            del self.__records[item]

    # ---------------------------------------------------------------
    def accept(self):
        success = True
        for item in self.__records:
            if self.store.balance(item) < self.__records[item].qty:
                success = False
                break

        self.__accepted = success
        if success:
            for item in self.__records:
                self.store.withdraw_item(item, self.__records[item].qty)
        else:
            self.__accepted = False
            print("Insufficient balance for '%s'. Required: %d, actual: %d" %
                  (item.name, self.__records[item].qty, self.store.balance(item)))

    # ---------------------------------------------------------------
    def cancel(self):
        # TODO: reverts accept logic
        pass

    # ---------------------------------------------------------------
    def __iter__(self):
        return iter(self.__records.values())

    # ---------------------------------------------------------------
    def __str__(self):
        str = "Sale invoice #%d at %s" % (self.number, self.date_time)
        str += "\n"
        str += SaleInvoice.__FORMAT_HEADER % ( "Item", "Qty", "Price", "Sum")
        for item in self.__records:
            str += "\n"
            str += SaleInvoice.__FORMAT_ROW % (item.name, self.__records[item].qty
                                             , self.__records[item].price
                                             , self.__records[item].sum)
        return str
