def create_vertices(center=(0,0,0), size = 1.0):
    """
    Generate 8 vertices for a cube centered at a given point

    Parameters:
        center (tuple): (x, y, z) The cordinates of the cubes center
        size (float): Length of one edge of the cube

    Returns:
        list of tuples: All 8 vertices of the cube
    """

    # Assign centers cordinates
    cx, cy, cz = center

    # Offset ammount (half the size of an edge)
    half = size / 2

    # Empty list to store the vertices
    vertices = []

    # Combine all of the -half & +half offsets around the center
    for x_offset in (-half, half):
        for y_offset in (-half, half):
            for z_offset in (-half, half):
                x = cx + x_offset
                y = cy + y_offset
                z = cz + z_offset

                vertices.append((x,y,z))
    
    return vertices 