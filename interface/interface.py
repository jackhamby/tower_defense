

class Interface():

    def __init__(self, map_, x, y, width, height, icon):
        self.map = map_
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.icon = icon

    def render(self):
        pass

    def handle_mouse_down(self, x, y):
        pass

    def handle_mouse_up(self, x, y):
        pass

    def handle_mouse_motion(self, x, y):
        pass

