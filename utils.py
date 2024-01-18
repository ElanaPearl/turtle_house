import numpy as np


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

    return roof_base_angle, roof_top_angle, roof_length
