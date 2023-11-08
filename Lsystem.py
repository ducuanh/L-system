import turtle


class TreeDrawer:

    def __init__(self, screen_width, screen_height, turtle_color='green', bg_color='black', pen_size=3):
        # screen settings
        self.width, self.height = screen_width, screen_height
        self.screen = turtle.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.screensize(3 * self.width, 3 * self.height)
        self.screen.bgcolor(bg_color)
        self.screen.delay(0)

        # turtle settings
        self.drawer = turtle.Turtle()
        self.drawer.pensize(pen_size)
        self.drawer.speed(0)
        self.drawer.setpos(0, -self.height // 2)
        self.drawer.color(turtle_color)

        # l-system settings
        self.axiom = 'XY'
        self.step = 7
        self.angle = 25
        self.stack = []
        self.thickness = 3
        self.drawer.left(90)
        self.drawer.pensize(self.thickness)

    def apply_rules(self, axiom):
        chr_1, rule_1 = 'F', 'FF'
        chr_2, rule_2 = 'X', 'F+[[X]-X]-F[-FX]+X'
        return ''.join([rule_1 if chr == chr_1 else
                        rule_2 if chr == chr_2 else chr for chr in axiom])

    def get_result(self, gens):
        for gen in range(gens):
            self.axiom = self.apply_rules(self.axiom)
        return self.axiom

    def draw(self, generations):
        self.axiom = self.get_result(generations)
        for chr in self.axiom:
            if chr == 'F':
                self.drawer.forward(self.step)
            elif chr == '+':
                self.drawer.right(self.angle)
            elif chr == '-':
                self.drawer.left(self.angle)
            elif chr == '[':
                angle_, pos_ = self.drawer.heading(), self.drawer.pos()
                self.stack.append((angle_, pos_))
            elif chr == ']':
                angle_, pos_ = self.stack.pop()
                self.drawer.setheading(angle_)
                self.drawer.penup()
                self.drawer.goto(pos_)
                self.drawer.pendown()


if __name__ == "__main__":
    tree = TreeDrawer(1600, 900)
    tree.draw(6)
    turtle.Screen().exitonclick()
