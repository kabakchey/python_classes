class Person:

   FORMAT_ATTR = "%-7s"
   FORMAT_VALUE = "%20s"
   FORMAT_DELIM = ":"
   FORMAT_ALL = FORMAT_ATTR + FORMAT_VALUE

   total_count = 0

   __i18n_attr_names = ("Name", "Email", "Phone", "Year", "Age")

   __i18n = {
       "EN": ["Name", "Email",      "Phone", "Year", "Age"],
       "UA": ["Им'я", "Е-скринька", "Телефон", "Рiк",  "Вiк"],
       "IT": ["Nome", "Email",      "Telefono", "Anno", "Eta"],
       "FR": ["Nom",  "Email",      "Téléphone", "Annee","Age"],
   }

   def __init__(self, name, email="", phone_number=""):
       self.name = name
       self.email = email
       self.phone_number = phone_number
       Person.total_count += 1
       self.__id = Person.total_count

   @staticmethod
   def __i18n_by_name(attr_name, lang):
       i18n_name = attr_name
       if attr_name in Person.__i18n_attr_names:
          idx = Person.__i18n_attr_names.index(attr_name)
          i18n_name = Person.__i18n[lang][idx]
       return i18n_name

   @staticmethod
   def _format_row(attr_name, attr_value, lang):
       i18_attr_name = Person.__i18n_by_name(attr_name, lang)
       attr_str = Person.FORMAT_ATTR % (i18_attr_name + Person.FORMAT_DELIM)
       return Person.FORMAT_ALL % (attr_str, attr_value)

   def _print_rows(self, lang):
       print(Person._format_row("ID", self.__id, lang))
       print(Person._format_row("Name", self.name, lang))
       print(Person._format_row("Email", self.email, lang))
       print(Person._format_row("Phone", self.phone_number, lang))

   def print_info(self, lang="EN"):
       print()
       print("-----------------------------")
       self._print_rows(lang)
       print("-----------------------------")
