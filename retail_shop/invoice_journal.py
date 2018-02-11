import datetime

class InvoiceJournal(object):

    # ----------------------------------------------------------------
    def __init__(self):
        self._invoices = []

    # ----------------------------------------------------------------
    def add_invoice(self, invoice):
        if invoice not in self._invoices:
            self._invoices.append(invoice)

    # ----------------------------------------------------------------
    def remove_invoice(self, invoice):
        if invoice in self._invoices:
            self._invoices.remove(invoice)

    # ----------------------------------------------------------------
    def get_invoices(self, date1=None, date2=None):
        self._invoices.sort(key=lambda inv : inv.date_time)

        lower_limit = date1 if not date1 is None else datetime.datetime.min
        upper_limit = date2 if not date2 is None else datetime.datetime.max

        return [invoice for invoice in self._invoices if
                lower_limit <= invoice.date_time <= upper_limit]
