import item
from sale_invoice import SaleInvoice
from invoice_journal import InvoiceJournal
from store import Store
from report import Report


if __name__ == "__main__":

    ### items
    item1 = item.Item("iPhone12", 1000, 1200)
    item2 = item.Item("iPhone13", 1200, 1400)
    item3 = item.Food("Sugar", 10, 12)

    ### store
    store = Store()
    store.add_item(item1, 10)
    store.add_item(item2, 20)
    store.add_item(item3, 30)

    ### invoice
    invoice1 = SaleInvoice(store)
    invoice1.add_item(item1, 10)
    invoice1.add_item(item2, 10)
    invoice1.add_item(item2, 5)
    invoice1.add_item(item3, 10)

    invoice2 = SaleInvoice(store)
    invoice2.add_item(item2, 5)
    invoice2.accept()

    print(invoice1)

    store.print_balance()
    invoice1.accept()
    store.print_balance()

    ### journal
    journal = InvoiceJournal()
    journal.add_invoice(invoice1)
    journal.add_invoice(invoice1)
    journal.add_invoice(invoice1)
    journal.add_invoice(invoice2)
    invcs = journal.get_invoices()
    ###print(invcs)

    ### report
    report = Report(journal, store)
    report.print_profit_by_item()
