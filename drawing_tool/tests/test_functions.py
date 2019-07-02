import unittest
from unittest.mock import patch, mock_open
from random import randint as rd
from functions import (
    initialize_canvas,
    get_instructions,
    get_coordinates_to_draw_rect_with_addline_function,
    to_flood_fill,
    add_line,
    add_rectangle,
    draw_into_output,
)


class InitializeCanvasTest(unittest.TestCase):

    def setUp(self):
        self.cleaned_data = rd(1, 100), rd(1, 100)

    def test_initialize_canvas_returns_list(self):
        self.assertIsInstance(initialize_canvas(self.cleaned_data), list)

    def test_initialize_canvas_returns_correct_output(self):
        width, height = self.cleaned_data
        dashes = ['-' * (width + 2)]
        body = [(['|'] + [' ' for _ in range(width)] + ['|']) for _ in range(height)]
        canvas = dashes + body + dashes
        self.assertListEqual(initialize_canvas(self.cleaned_data), canvas)


class GetInstructionsTest(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='C 20 6\nR 10 4 5 4'))
    def test_get_instructions_returns_list(self):
        self.assertIsInstance(get_instructions(), list)

    @patch('builtins.open', mock_open(read_data='C 20 6\nR 10 4 5 4'))
    def test_get_instructions_returns_correct_output(self):
        self.assertListEqual(get_instructions(), ['R 10 4 5 4'])


class GetCoordinatesTest(unittest.TestCase):

    def setUp(self):
        self.cleaned_data = [1, 3, 20, 6]

    def test_get_coordinates_returns_correct_output(self):
        self.assertTupleEqual(get_coordinates_to_draw_rect_with_addline_function(self.cleaned_data),
                              (
                                  (1, 3, 20, 3),
                                  (1, 6, 20, 6),
                                  (1, 3, 1, 6),
                                  (20, 3, 20, 6)
                              )
                              )

    def test_get_coordinates_returns_tuple(self):
        self.assertIsInstance(get_coordinates_to_draw_rect_with_addline_function(self.cleaned_data), tuple)


class WithoutReturnFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.width, self.height = rd(10, 100), rd(10, 100)
        self.dashes = ['-' * (self.width + 2)]
        self.body = [(['|'] + [' ' for _ in range(self.width)] + ['|']) for _ in range(self.height)]
        self.canvas = self.dashes + self.body + self.dashes
        self.control_body = [(['|'] + [' ' for _ in range(self.width)] + ['|']) for _ in range(self.height)]
        self.control_canvas = self.dashes + self.control_body + self.dashes

    def test_to_flood_fill_add_correct_values_to_canvas(self):
        control_body = [(['|'] + ['o' for _ in range(self.width)] + ['|']) for _ in range(self.height)]
        control_canvas = self.dashes + control_body + self.dashes
        to_flood_fill(self.canvas, 1, 1, 'o')
        self.assertListEqual(self.canvas, control_canvas)

    def test_addline_add_horizontal_line_correct_to_canvas(self):
        for cell in range(1, 11):
            self.control_canvas[1][cell] = 'x'
        add_line(self.canvas, (1, 1, 10, 1))
        self.assertListEqual(self.canvas, self.control_canvas)

    def test_addline_add_vertical_line_correct_to_canvas(self):
        for row in range(1, 11):
            self.control_canvas[row][5] = 'x'
        add_line(self.canvas, (5, 1, 5, 10))
        self.assertListEqual(self.canvas, self.control_canvas)

    def test_add_rectangle_add_correct_values_to_canvas(self):
        for cell in range(2, 8):
            self.control_canvas[2][cell] = 'x'
            self.control_canvas[5][cell] = 'x'
        for row in range(3, 5):
            self.control_canvas[row][2] = 'x'
            self.control_canvas[row][7] = 'x'
        add_rectangle(self.canvas, ((2, 2, 7, 2), (2, 5, 7, 5), (2, 2, 2, 5), (7, 2, 7, 5)))
        self.assertListEqual(self.canvas, self.control_canvas)

    def test_draw_into_output_write_into_correct_file(self):
        m = mock_open()
        with patch('builtins.open', m):
            draw_into_output(self.canvas)
        m.assert_called_once_with('output.txt', 'a')




if __name__ == '__main__':
    unittest.main()
