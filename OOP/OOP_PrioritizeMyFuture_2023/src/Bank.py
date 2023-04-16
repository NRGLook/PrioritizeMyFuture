class Bank:
    def __init__(self):
        self.volume = 0
        self.styles = []
        self.name = ""
        self.y_o = 0

    def set_volume(self, volume):
        self.volume = volume

    def set_styles(self, styles):
        self.styles = styles

    def change_styles(self, styles):
        self.styles += styles

    def set_name(self, name):
        self.name = name

    def set_y_o(self, y_o):
        self.y_o = y_o

    def change_y_o(self, y_o):
        self.y_o += y_o

    def get_y_o(self):
        return self.y_o