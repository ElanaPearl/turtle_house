#!/usr/bin/env python

import numpy as np

from turtle import (
    begin_fill,
    circle,
    end_fill,
    color,
    fillcolor,
    forward,
    left
)


def get_roof_angles(
    base_width: int, base_height: int, roof_height: int
) -> tuple[int, int, int]:
    """Returns the angles and length of the roof using the pythagorean theorem

    :param base_width: The width of the base of the house
    :param base_height: The height of the base of the house
    :param roof_height: The height of the roof of the house
    :return roof_base_angle: The angle between the roof and the base
    :return roof_top_angle: The angle between the two roof sides
    :return roof_length: The length of each side of the roof
    """

    # Calculate the length of the roof using a^2 + b^2 = c^2
    roof_length = np.sqrt(roof_height**2 + (base_width / 2) ** 2)

    # Calculate the angles between the roof and the base
    roof_base_angle = np.degrees(np.arcsin(roof_height / roof_length))

    # Calculate the angle between the two roof sides
    roof_top_angle = 2 * (90 - roof_base_angle)

    # Return the roof base angle, roof top angle and roof length
    return roof_base_angle, roof_top_angle, roof_length


def filled_circle(radius: int, circle_color: str):
    '''
    Creates a circle that is filled in with a color
    
    :param radius: the radius of the circle
    :param circle_color: fill color
    '''
    color(circle_color,circle_color)
    begin_fill()
    circle(radius)
    end_fill()


def filled_rectangle(width: int, height: int, color: str):
    '''
    Creates a rectangle that is filled in with a color
    
    :param height: the width of the rectangle
    :param width: the height of the rectangle
    :param color: fill color
    '''
    
    # Fill the color
    fillcolor(color) 
    begin_fill() 

    # Now draw the form
    forward(width) 
    left(90) 
    forward(height) 
    left(90) 
    forward(width) 
    left(90) 
    forward(height) 
    left(90) 

    # Complete
    end_fill()

