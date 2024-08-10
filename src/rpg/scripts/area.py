def polygon_area(coords):
    n = len(coords)
    area = 0.0
    for i in range(n - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        area += x1 * y2 - y1 * x2
    area += coords[-1][0] * coords[0][1] - coords[-1][1] * coords[0][0]
    return abs(area) / 2.0

# Define the coordinates of the polygon
coords = [
    (95, 620),
    (470, 310),
    (946, 17),
    (1082, 139),
    (1169, 368),
    (1008, 513),
    (824, 727),
    (616, 1114),
    (95, 620)  # Closing the polygon
]

# Calculate the area
area = polygon_area(coords)
print(f'The area of the polygon is: {area} square units')