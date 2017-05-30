import datetime



class InvoiceJournal(object):

    # ----------------------------------------------------------------
    def __init__(self):
        self.__invoices = []

    # ----------------------------------------------------------------
    def add_invoice(self, invoice):
        if invoice not in self.__invoices:
            self.__invoices.append(invoice)

    # ----------------------------------------------------------------
    def remove_invoice(self, invoice):
        if invoice in self.__invoices:
            self.__invoices.remove(invoice)

    # ----------------------------------------------------------------
    def get_invoices(self, date1=None, date2=None):
        self.__invoices.sort(key=lambda inv : inv.date_time)

        lower_limit = datetime.datetime.min
        if date1 != None:
            lower_limit = date1

        upper_limit = date2 if date2 != None else datetime.datetime.max

        result_lst = [invoice for invoice in self.__invoices if
                            lower_limit <= invoice.date_time <= upper_limit]

        return result_lst