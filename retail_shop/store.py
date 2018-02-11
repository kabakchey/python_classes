class Store(object):

    # ---------------------------------------------------------------
    def __init__(self):
        self._items_balance = {}

    # ---------------------------------------------------------------
    def add_item(self, item, qty):
        self._items_balance[item] = self._items_balance.get(item, 0) + qty

    # ---------------------------------------------------------------
    def withdraw_item(self, item, qty):
        if item in self._items_balance:
            if self._items_balance[item] >= qty:
                self._items_balance[item] -= qty

    # ---------------------------------------------------------------
    def balance(self, item):
        return self._items_balance.get(item, 0)

    # ---------------------------------------------------------------
    def print_balance(self):
        #TODO: fancy print
        print("\nStore balance:")
        for item in sorted(self._items_balance, key=lambda item : item.name):
            print ("\t%s: %d" % (item.name, self._items_balance[item]))