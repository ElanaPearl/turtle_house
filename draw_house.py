#!/usr/bin/env python

# Load paackages required for drawing
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
    setheading
)

from utils import filled_circle, filled_rectangle, get_roof_angles


def move_to(x, y):
    """Move the turtle to position (x, y) without drawing."""
    penup()
    setpos(x, y)
    pendown()


def draw_house_outline(
    base_width: int = 250, base_height: int = 150, roof_height: int = 100
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


def draw_door(width: int = 30, height: int = 60, color: str = "white"):
    """
    Draw a standard door.

    :param width: width of door
    :param height: height of door
    :param color: color of door
    """

    filled_rectangle(width, height, color)
    penup()
    forward(int(0.75 * width))
    left(90)
    forward(int(0.5 * height))
    pendown()
    circle(int(0.125 * width))


def draw_garage_door(width: int = 60, height: int = 60, color: str = "white"):
    """
    Draw a garage door
    :param width: width of garage door
    :param height: height of garage door
    :param color: color of garage door
    """
    filled_rectangle(width, height, color)


def draw_tree(
    trunk_width: int = 10,
    trunk_height: int = 50,
    leaf_radius: int = 20,
    trunk_color: str = "brown",
    leaf_color: str = "green",
):
    """
    Draws outline of tree and colors it.
    Tree is constructed as a circle on top of a rectangle

    :param trunk_width: width of trunk
    :param trunk_height: height of trunk
    :param trunk_color: color of trunk
    :param leaf_radius: radius of leaf
    :param leaf_color: color of leaf
    """
    # Draw the leafs
    filled_circle(leaf_radius, leaf_color)
    right(180)

    # Draw the trunk
    filled_rectangle(trunk_width, trunk_height, trunk_color)


def draw_window(width: int = 20, height: int = 40, color: str = "white"):
    """
    Draw a window
    cross lines exactly halfway of width and height

    :param width: width of garage door
    :param height: height of garage door
    :param color: color of garage door
    """
    
    filled_rectangle(width, height, color)
    forward(int(0.5 * width))
    left(90)
    forward(height)
    right(90)
    forward(int(0.5 * width))
    right(90)
    forward(int(0.5 * height))
    right(90)
    forward(width)


def draw_cloud(radius: int = 20, cloud_color: str = "blue"):
    """
    Draws outline of cloud and fills them in.
    Clouds are constructed as a cluster of overlapping circles

    :param radius: radius of each overlapping circle
    :param cloud_color: color of cloud
    """
    # Draw clowd consisting of 5 circles:
    filled_circle(radius, cloud_color)
    forward(radius)

    for _ in range(4):
        filled_circle(radius, cloud_color)
        right(90)
   


def main():

    # Open the screen
    getscreen()

    # Set the starting point
    start = (-200, -100)

    # Set the base parameters
    base_width = 250
    base_height = 150

    # Move to the starting point
    move_to(start[0], start[1])

    # Draw the house
    draw_house_outline(base_width=base_width, base_height=base_height)
    move_to(start[0] + base_width - 50, start[1])
    setheading(0)

    # Draw the door
    draw_door()

    move_to(start[0] + 20, start[1])
    setheading(0)

    # Draw the garage door
    draw_garage_door()
    move_to(start[0] + 100, start[1])
    setheading(0)

    # Draw the other garage door
    draw_garage_door()

    move_to(start[0] + 20, start[1] + (base_height / 2))
    setheading(0)

    # Draw 4 windows in different psitions
    draw_window() # First window
    move_to(start[0] + 70, start[1] + (base_height / 2))
    setheading(0)
    draw_window() # Second window
    move_to(start[0] + 120, start[1] + (base_height / 2))
    setheading(0)
    draw_window() # Third window
    move_to(start[0] + 170, start[1] + (base_height / 2))
    setheading(0)
    draw_window() # Fourth window

    move_to(start[0] + base_width + 50, start[1] + 50)
    setheading(0)

    # Draw the trees
    draw_tree() # First tree
    move_to(start[0] + base_width + 100, start[1] + 50)
    setheading(0)
    draw_tree() # Second tree

    move_to(100, 100)
    setheading(0)

    # Draw the clouds
    draw_cloud() # First cloud
    move_to(-300, 100)
    setheading(0)
    draw_cloud() # Second cloud

    mainloop()


if __name__ == "__main__":
    main()
