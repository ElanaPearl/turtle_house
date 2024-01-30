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


def move_relative_to_start(
    t: SvgTurtle, start: tuple[int, int], offset_from_start: tuple[int, int] = (0, 0)
):
    """Move the turtle to a position relative to the start position without drawing.

    :param t: the turtle
    :param start: The start position
    :param offset_from_start: The offset from the start position
    """
    move_to(t, x=start[0] + offset_from_start[0], y=start[1] + offset_from_start[1])
    t.setheading(0)


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


def main(
    output_file: str = "house.svg",
    canvas_size: tuple[int, int] = (800, 400),
    start: tuple[int, int] = (-200, -100),
    base_width: int = 250,
    base_height: int = 150,
    door_offset: tuple[int, int] = (-50, 0),
    garage_door_1_offset: tuple[int, int] = (20, 0),
    garage_door_2_offset: tuple[int, int] = (100, 0),
    window_1_offset: tuple[int, int] = (20, 0),
    window_2_offset: tuple[int, int] = (70, 0),
    window_3_offset: tuple[int, int] = (120, 0),
    window_4_offset: tuple[int, int] = (170, 0),
    tree_1_offset: tuple[int, int] = (50, 50),
    tree_2_offset: tuple[int, int] = (100, 50),
    cloud_1_offset: tuple[int, int] = (100, 100),
    cloud_2_offset: tuple[int, int] = (-300, 100),
):
    """Draws a house with a door, garage door, windows, trees and clouds

    :param output_file: The name of the output file to save the image to
    :param canvas_size: The size of the canvas to draw the house on
    :param start: The starting position of the house
    :param base_width: The width of the base of the house
    :param base_height: The height of the base of the house
    :param door_offset: The offset of the door from the start position
    :param garage_door_1_offset: The offset of the first garage door from the start position
    :param garage_door_2_offset: The offset of the second garage door from the start position
    :param window_1_offset: The offset of the first window from the start position
    :param window_2_offset: The offset of the second window from the start position
    :param window_3_offset: The offset of the third window from the start position
    :param window_4_offset: The offset of the fourth window from the start position
    :param tree_1_offset: The offset of the first tree from the start position
    :param tree_2_offset: The offset of the second tree from the start position
    :param cloud_1_offset: The offset of the first cloud from the start position
    :param cloud_2_offset: The offset of the second cloud from the start position
    """

    t = SvgTurtle(*canvas_size)

    # Move to the starting point
    move_to(t, start[0], start[1])

    # Draw the house
    draw_house_outline(t, base_width=base_width, base_height=base_height)

    # Draw the door
    move_relative_to_start(t, (start[0] + base_width, start[1]), door_offset)
    draw_door(t)

    # Draw the garage door
    move_relative_to_start(t, start, garage_door_1_offset)
    draw_garage_door(t)

    # Draw the other garage door
    move_relative_to_start(t, start, garage_door_2_offset)
    draw_garage_door(t)

    # Draw 4 windows in different positions
    start_of_second_floor = (start[0], start[1] + base_height / 2)
    for window_offset in [
        window_1_offset,
        window_2_offset,
        window_3_offset,
        window_4_offset,
    ]:
        move_relative_to_start(t, start_of_second_floor, window_offset)
        draw_window(t)

    # Draw the trees
    start_of_trees = (start[0] + base_width, start[1])
    for tree_offset in [tree_1_offset, tree_2_offset]:
        move_relative_to_start(t, start_of_trees, tree_offset)
        draw_tree(t)

    # Draw the clouds
    for cloud_offset in [cloud_1_offset, cloud_2_offset]:
        move_relative_to_start(t, [0, 0], cloud_offset)
        draw_cloud(t)

    t.save_as(output_file)


if __name__ == "__main__":
    main()
