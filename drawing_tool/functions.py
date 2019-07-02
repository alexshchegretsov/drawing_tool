from typing import Union


def initialize_canvas(cleaned_data: tuple) -> list:
    """Initializes and returns canvas."""
    width, height = cleaned_data
    canvas = []
    canvas.extend(['-' * (width + 2)])
    body = [(['|'] + [' ' for _ in range(width)] + ['|']) for _ in range(height)]
    canvas.extend(body)
    canvas.extend(['-' * (width + 2)])
    return canvas


def draw_into_output(canvas: list) -> None:
    """Writes data into specified file."""
    with open('output.txt', 'a') as file:
        for line in canvas:
            file.write(''.join(line) + '\n')


def get_instructions() -> list:
    """Reads data and returns list except first line."""
    with open('input.txt', 'r') as file:
        return file.readlines()[1:]


def get_coordinates_to_draw_rect_with_addline_function(cleaned_data: list) -> tuple:
    """Decomposes the data to the desired values ​​for the add_rectangle function."""
    value_1, value_2, value_3, value_4 = cleaned_data
    first_horiz_coords = value_1, value_2, value_3, value_2
    second_horiz_coords = value_1, value_4, value_3, value_4
    first_vertical_coords = value_1, value_2, value_1, value_4
    second_vertical_coords = value_3, value_2, value_3, value_4
    return first_horiz_coords, second_horiz_coords, first_vertical_coords, second_vertical_coords


def add_rectangle(canvas: list, coordinates: tuple) -> None:
    """Adds values ​​to the canvas that will be visible as a rectangle."""
    for coordinate in coordinates:
        add_line(canvas, coordinate)


def add_line(canvas: list, instructions: Union[list, tuple]) -> None:
    """Adds values ​​to the canvas that will be visible as a line."""
    cell_1, row_1, cell_2, row_2 = instructions
    if row_1 == row_2:
        for cell_id in range(min(cell_1, cell_2), max(cell_1, cell_2) + 1):
            canvas[row_1][cell_id] = 'x'

    elif cell_1 == cell_2:
        for row_id in range(min(row_1, row_2), max(row_1, row_2) + 1):
            canvas[row_id][cell_1] = 'x'


def to_flood_fill(canvas: list, cell_id: int, row_id: int, color: str) -> None:
    """Should fill the entire area connected to (x,y) with "colour"."""
    width, height = len(canvas[0]), len(canvas)
    to_replace = canvas[row_id][cell_id]
    stack = set()
    stack.add((cell_id, row_id))
    while stack:
        cell_id, row_id = stack.pop()
        if not (0 < cell_id < width and 0 < row_id < height):
            continue
        cell = canvas[row_id][cell_id]
        if cell != to_replace:
            continue
        canvas[row_id][cell_id] = color
        stack.add((cell_id - 1, row_id))
        stack.add((cell_id + 1, row_id))
        stack.add((cell_id, row_id - 1))
        stack.add((cell_id, row_id + 1))
        stack.add((cell_id - 1, row_id - 1))
        stack.add((cell_id + 1, row_id - 1))
        stack.add((cell_id - 1, row_id + 1))
        stack.add((cell_id + 1, row_id + 1))
