class Bank:
    def __int__(self, volume, name, date_of_create):
        self.volume = volume
        self.name = name
        self.date_of_create = date_of_create

    def set_volume(self):
        pass

    def set_styles(self):
        pass

    def change_styles(self):
        pass

    def set_name(self):
        pass

    def set_y_o(self):
        pass

    def change_y_o(self):
        pass

    def get_y_o(self):
        pass


class BankToday(Bank):
    def __int__(self):
        pass


class BankFuture(Bank):
    def __int__(self):
        pass
