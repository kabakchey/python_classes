from invoice_journal import InvoiceJournal
from sale_invoice import SaleInvoice


class Report(object):

    #----------------------------------------------------------------
    def __init__(self, journal, store):
        self.journal = journal
        self.store = store

    #----------------------------------------------------------------
    def print_profit_by_item(self, date1=None, date2=None):

        items_profit = {}
        for invoice in self.journal.get_invoices(date1, date2):
            for record in invoice.records():
                profit = record.qty*(record.item.sale_price-record.item.purchase_price)
                items_profit[record.item] = items_profit.get(record.item, 0) + profit

        #TODO: fance print
        print("\nProfit by item:")
        for item in sorted(items_profit, key=items_profit.get):
            print ("\t%s: %d" % (item.name, items_profit[item]))

    # ----------------------------------------------------------------
    def print_profit_by_date(self, date1=None, date2=None):
        pass

    # ----------------------------------------------------------------
    def print_gross_by_item(self, date1=None, date2=None):
        pass

    # ----------------------------------------------------------------
    def print_gross_by_date(self, date1=None, date2=None):
        pass

    # ----------------------------------------------------------------
    def print_balance(self, date1=None):
        pass
