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

from utils import get_roof_angles


def move_to(x, y):
    """Move the turtle to position (x, y) without drawing."""
    pass


def draw_house_outline(
    base_width: int = 250, base_height: int = 100, roof_height: int = 100
):
    """Draws the outline of a 2D rectangular house with a triangular roof.

    :param base_width: The width of the base of the house
    :param base_height: The height of the base of the house
    :param roof_height: The height of the roof of the house
    """
    # Draw the base
    forward(base_width)
    left(90)
    forward(base_height)
    left(90)
    forward(base_width)
    left(90)
    forward(base_height)

    # Return to upper left corner
    left(180)
    forward(base_height)

    # Draw the roof
    roof_base_angle, roof_top_angle, roof_length = get_roof_angles(
        base_width, base_height, roof_height
    )
    right(90 - roof_base_angle)
    forward(roof_length)
    right(180 - roof_top_angle)
    forward(roof_length)


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
