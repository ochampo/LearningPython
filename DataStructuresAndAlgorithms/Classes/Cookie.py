from calendar import c


class Cookie:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color


cookie_1 = Cookie('blue')

print("cookie1",cookie_1.get_color())