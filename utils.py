import numpy as np


def get_roof_angles(base_width, base_height, roof_height):
    """Returns the angles and length of the roof using the pythagorean theorem"""

    # Calculate the length of the roof using a^2 + b^2 = c^2
    roof_length = np.sqrt(roof_height**2 + (base_width / 2) ** 2)

    # Calculate the angles between the roof and the base
    roof_base_angle = np.degrees(np.arcsin(roof_height / roof_length))

    # Calculate the angle between the two roof sides
    roof_top_angle = 2 * (90 - roof_base_angle)

    return roof_base_angle, roof_top_angle, roof_length
