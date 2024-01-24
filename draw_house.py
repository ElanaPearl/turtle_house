#!/usr/bin/env python

# Load paackages required for drawing
from svg_turtle import SvgTurtle

from utils import filled_circle, filled_rectangle, get_roof_angles


def move_to(t: SvgTurtle, x: int = 1, y: int = 1):
    """Move the turtle to position (x, y) without drawing.

    :param t: the turtle
    :param x: The x coordinate to move to
    :param y: The y coordinate to move to
    """
    t.penup()
    t.setpos(x, y)
    t.pendown()


def draw_house_outline(
    t: SvgTurtle, base_width: int = 250, base_height: int = 150, roof_height: int = 100
):
    """Draws the outline of a 2D rectangular house with a triangular roof.

    :param t: the turtle
    :param base_width: The width of the base of the house
    :param base_height: The height of the base of the house
    :param roof_height: The height of the roof of the house
    """
    # Draw the base
    t.forward(base_width)
    t.left(90)
    t.forward(base_height)
    t.left(90)
    t.forward(base_width)
    t.left(90)
    t.forward(base_height)

    # Return to upper left corner
    t.left(180)
    t.forward(base_height)

    # Draw the roof
    roof_base_angle, roof_top_angle, roof_length = get_roof_angles(
        base_width, base_height, roof_height
    )
    t.right(90 - roof_base_angle)
    t.forward(roof_length)
    t.right(180 - roof_top_angle)
    t.forward(roof_length)


def draw_door(t: SvgTurtle, width: int = 30, height: int = 60, color: str = "white"):
    """
    Draw a standard door.

    :param t: the turtle
    :param width: width of door
    :param height: height of door
    :param color: color of door
    """

    filled_rectangle(t, width, height, color)
    t.penup()
    t.forward(int(0.75 * width))
    t.left(90)
    t.forward(int(0.5 * height))
    t.pendown()
    t.circle(int(0.125 * width))


def draw_garage_door(
    t: SvgTurtle, width: int = 60, height: int = 60, color: str = "white"
):
    """
    Draw a garage door
    :param t: the turtle
    :param width: width of garage door
    :param height: height of garage door
    :param color: color of garage door
    """
    filled_rectangle(t, width, height, color)


def draw_tree(
    t: SvgTurtle,
    trunk_width: int = 10,
    trunk_height: int = 50,
    leaf_radius: int = 20,
    trunk_color: str = "brown",
    leaf_color: str = "green",
):
    """
    Draws outline of tree and colors it.
    Tree is constructed as a circle on top of a rectangle

    :param t: the turtle
    :param trunk_width: width of trunk
    :param trunk_height: height of trunk
    :param trunk_color: color of trunk
    :param leaf_radius: radius of leaf
    :param leaf_color: color of leaf
    """
    # Draw the leafs
    filled_circle(t, leaf_radius, leaf_color)
    t.right(180)

    # Draw the trunk
    filled_rectangle(t, trunk_width, trunk_height, trunk_color)


def draw_window(t: SvgTurtle, width: int = 20, height: int = 40, color: str = "white"):
    """
    Draw a window
    cross lines exactly halfway of width and height

    :param t: the turtle
    :param width: width of garage door
    :param height: height of garage door
    :param color: color of garage door
    """

    filled_rectangle(t, width, height, color)
    t.forward(int(0.5 * width))
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(int(0.5 * width))
    t.right(90)
    t.forward(int(0.5 * height))
    t.right(90)
    t.forward(width)


def draw_cloud(t: SvgTurtle, radius: int = 20, cloud_color: str = "blue"):
    """
    Draws outline of cloud and fills them in.
    Clouds are constructed as a cluster of overlapping circles

    :param t: the turtle
    :param radius: radius of each overlapping circle
    :param cloud_color: color of cloud
    """
    # Draw clowd consisting of 5 circles:
    filled_circle(t, radius, cloud_color)
    t.forward(radius)

    for _ in range(4):
        filled_circle(t, radius, cloud_color)
        t.right(90)


def main(output_file: str = "house.svg"):
    """Draws a house with a door, garage door, windows, trees and clouds

    :param output_file: The name of the output file to save the image to
    """
    canvas_size = (800, 400)
    start = (-200, -100)

    t = SvgTurtle(*canvas_size)

    # Set the base parameters
    base_width = 250
    base_height = 150

    # Move to the starting point
    move_to(t, start[0], start[1])

    # Draw the house
    draw_house_outline(t, base_width=base_width, base_height=base_height)
    move_to(t, start[0] + base_width - 50, start[1])
    t.setheading(0)

    # Draw the door
    draw_door(t)

    move_to(t, start[0] + 20, start[1])
    t.setheading(0)

    # Draw the garage door
    draw_garage_door(t)
    move_to(t, start[0] + 100, start[1])
    t.setheading(0)

    # Draw the other garage door
    draw_garage_door(t)

    move_to(t, start[0] + 20, start[1] + (base_height / 2))
    t.setheading(0)

    # Draw 4 windows in different psitions
    draw_window(t)  # First window
    move_to(t, start[0] + 70, start[1] + (base_height / 2))
    t.setheading(0)
    draw_window(t)  # Second window
    move_to(t, start[0] + 120, start[1] + (base_height / 2))
    t.setheading(0)
    draw_window(t)  # Third window
    move_to(t, start[0] + 170, start[1] + (base_height / 2))
    t.setheading(0)
    draw_window(t)  # Fourth window

    move_to(t, start[0] + base_width + 50, start[1] + 50)
    t.setheading(0)

    # Draw the trees
    draw_tree(t)  # First tree
    move_to(t, start[0] + base_width + 100, start[1] + 50)
    t.setheading(0)
    draw_tree(t)  # Second tree

    move_to(t, 100, 100)
    t.setheading(0)

    # Draw the clouds
    draw_cloud(
        t,
    )  # First cloud
    move_to(t, -300, 100)
    t.setheading(0)
    draw_cloud(t)  # Second cloud

    t.save_as(output_file)


if __name__ == "__main__":
    main()
