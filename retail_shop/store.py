class Store(object):

    # ---------------------------------------------------------------
    def __init__(self):
        self.__items_balance = {}

    # ---------------------------------------------------------------
    def add_item(self, item, qty):
        self.__items_balance[item] = self.__items_balance.get(item, 0) + qty
        #
        # if item in self.__items_balance:
        #     self.__items_balance[item] = self.__items_balance[item] + qty
        # else:
        #     self.__items_balance[item] = 0                          + qty

    # ---------------------------------------------------------------
    def withdraw_item(self, item, qty):
        if item in self.__items_balance:
            if self.__items_balance[item] >= qty:
                self.__items_balance[item] -= qty

    # ---------------------------------------------------------------
    def balance(self, item):
        return self.__items_balance.get(item, 0)

    # ---------------------------------------------------------------
    def print_balance(self):
        #TODO: fancy print
        print("\nStore balance:")
        for item in sorted(self.__items_balance, key=lambda item : item.name):
            print ("\t%s: %d" % (item.name, self.__items_balance[item]))