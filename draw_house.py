from turtle import (
    circle,
    forward,
    getscreen,
    left,
    mainloop,
    pendown,
    penup,
    right,
    setpos,
)


def move_to(x, y):
    """Move the turtle to position (x, y) without drawing."""
    pass


def draw_house_outline():
    """Draw the outline of a house."""
    pass


def draw_door():
    """Draw a standard door."""
    pass


def draw_garage_door():
    """Draw a garage door."""
    pass


def draw_tree():
    """Draw a tree."""
    pass


def draw_window():
    """Draw a window."""
    pass


def draw_cloud():
    """Draw a cloud."""
    pass


def main():
    getscreen()

    draw_house_outline()

    draw_door()

    draw_garage_door()
    draw_garage_door()

    draw_window()
    draw_window()
    draw_window()
    draw_window()

    draw_tree()
    draw_tree()

    draw_cloud()
    draw_cloud()

    mainloop()


if __name__ == "__main__":
    main()
