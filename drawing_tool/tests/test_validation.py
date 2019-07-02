import unittest
from unittest.mock import patch, mock_open
from validation import (
    canvas_instruction_validator,
    pre_validate_instruction,
    line_validator,
    rectangle_validator,
    flood_fill_validator,
)


class CanvasValidationTest(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='3 2 1'))
    def test_canvas_instruction_validator_react_wrong_1st_parameter(self):
        with self.assertRaises(ValueError):
            canvas_instruction_validator()

    @patch('builtins.open', mock_open(read_data='C r 1'))
    def test_canvas_instruction_validator_react_2nd_parameter_not_digit(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 2 r'))
    def test_canvas_instruction_validator_react_3rd_parameter_not_digit(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 0 1'))
    def test_canvas_instruction_validator_react_2nd_parameter_is_zero(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 7 0'))
    def test_canvas_instruction_validator_react_3rd_parameter_is_zero(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 2'))
    def test_canvas_instruction_validator_react_length_less_than_2(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 2 4 6'))
    def test_canvas_instruction_validator_react_length_greater_than_3(self):
        self.assertRaises(ValueError, canvas_instruction_validator())

    @patch('builtins.open', mock_open(read_data='C 1000 1000'))
    def test_canvas_instruction_validator_returns_correct_value(self):
        self.assertTupleEqual(canvas_instruction_validator(), (1000, 1000))

    @patch('builtins.open', mock_open(read_data=''))
    def test_canvas_instruction_validator_react_to_empty_string(self):
        self.assertRaises(IndexError, canvas_instruction_validator())


class PreValidateInstructionTest(unittest.TestCase):

    def setUp(self):
        self.instruction_1 = ['B', '1', '2', '3']
        self.instruction_2 = ['L', 'x', 'x', 'x', 'x']
        self.instruction_3 = ['R', 't', 'e', 's', 't']

    def test_pre_validate_instruction_returns_tuple(self):
        self.assertIsInstance(pre_validate_instruction(self.instruction_1), tuple)
        self.assertIsInstance(pre_validate_instruction(self.instruction_2), tuple)
        self.assertIsInstance(pre_validate_instruction(self.instruction_3), tuple)

    def test_pre_validate_instruction_returns_correct_value(self):
        self.assertTupleEqual(pre_validate_instruction(self.instruction_1), ('B', ['1', '2', '3']))
        self.assertTupleEqual(pre_validate_instruction(self.instruction_2), ('L', ['x', 'x', 'x', 'x']))
        self.assertTupleEqual(pre_validate_instruction(self.instruction_3), ('R', ['t', 'e', 's', 't']))

    def test_pre_validate_instruction_raises_ValueError(self):
        instruction_1 = ['R', '1', '2', '3', '4', '5']
        instruction_2 = ['L', '1', '2']
        instruction_3 = ['\n']
        instruction_4 = ['4', '4', '4', '4']
        self.assertRaises(ValueError, pre_validate_instruction(instruction_1))
        self.assertRaises(ValueError, pre_validate_instruction(instruction_2))
        self.assertRaises(ValueError, pre_validate_instruction(instruction_3))
        self.assertRaises(ValueError, pre_validate_instruction(instruction_4))


class LineValidatorTest(unittest.TestCase):

    def setUp(self):
        self.cleaned_data = 20, 6
        self.parameters_1 = ['1', '1', '20', '1']
        self.parameters_2 = ['1', '6', '20', '6']
        self.parameters_3 = ['1', '6', '1', '1']
        self.parameters_4 = ['20', '6', '20', '1']

    def test_line_validator_returns_list(self):
        self.assertIsInstance(line_validator(self.cleaned_data, self.parameters_1), list)
        self.assertIsInstance(line_validator(self.cleaned_data, self.parameters_2), list)
        self.assertIsInstance(line_validator(self.cleaned_data, self.parameters_3), list)
        self.assertIsInstance(line_validator(self.cleaned_data, self.parameters_4), list)

    def test_line_validator_returns_correct_value(self):
        self.assertListEqual(line_validator(self.cleaned_data, self.parameters_1), [1, 1, 20, 1])
        self.assertListEqual(line_validator(self.cleaned_data, self.parameters_2), [1, 6, 20, 6])
        self.assertListEqual(line_validator(self.cleaned_data, self.parameters_3), [1, 6, 1, 1])
        self.assertListEqual(line_validator(self.cleaned_data, self.parameters_4), [20, 6, 20, 1])

    def test_line_validator_raises_ValueError_if_length_not_equal_4(self):
        parameters_1 = ['1', '2', '3']
        parameters_2 = ['1', '2', '3', '4', '5']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))

    def test_line_validator_raises_ValueError_if_parameter_not_is_digit(self):
        parameters_1 = ['a', '4', '1', '4']
        parameters_2 = [str(float(2)), '4', '1', '4']
        parameters_3 = [str(complex(2)), '4', '1', '4']
        parameters_4 = [bin(2), '4', '1', '4']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_3))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_4))

    def test_line_validator_raises_ValueError_if_width_parameter_greater_than_canvas_width(self):
        parameters_1 = ['21', '4', '1', '4']
        parameters_2 = ['1', '4', '21', '4']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))

    def test_line_validator_raises_ValueError_if_width_parameter_less_equal_zero(self):
        parameters_1 = ['-1', '4', '1', '4']
        parameters_2 = ['1', '4', '0', '4']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))

    def test_line_validator_raises_ValueError_if_height_parameter_greater_than_canvas_height(self):
        parameters_1 = ['1', '7', '1', '4']
        parameters_2 = ['1', '4', '1', '7']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))

    def test_line_validator_raises_ValueError_if_height_parameter_less_equal_zero(self):
        parameters_1 = ['1', '-1', '1', '4']
        parameters_2 = ['1', '4', '1', '0']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))

    def test_line_validator_raises_ValueError_if_width_or_height_parameters_not_equal(self):
        parameters_1 = ['1', '2', '3' '4']
        parameters_2 = ['1', '1', '3' '3']
        parameters_3 = ['1', '3', '3' '1']
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_2))
        self.assertRaises(ValueError, line_validator(self.cleaned_data, parameters_3))


class RectangleValidator(unittest.TestCase):

    def setUp(self):
        self.cleaned_data = 20, 6
        self.parameters_1 = ['1', '1', '20', '6']
        self.parameters_2 = ['2', '2', '19', '6']

    def test_rectangle_validator_returns_list(self):
        self.assertIsInstance(rectangle_validator(self.cleaned_data, self.parameters_1), list)
        self.assertIsInstance(rectangle_validator(self.cleaned_data, self.parameters_2), list)

    def test_rectangle_validator_returns_correct_output(self):
        self.assertListEqual(rectangle_validator(self.cleaned_data, self.parameters_1), [1, 1, 20, 6])
        self.assertListEqual(rectangle_validator(self.cleaned_data, self.parameters_2), [2, 2, 19, 6])

    def test_rectangle_validator_raises_ValueError_if_length_parameters_not_equal_4(self):
        parameters_1 = ['1', '2', '3']
        parameters_2 = ['1', '2', '3', '4', '5']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))

    def test_rectangle_validator_raises_ValueError_if_parameter_not_is_digit(self):
        parameters_1 = ['a', '2', '1', '4']
        parameters_2 = [str(float(2)), '2', '1', '4']
        parameters_3 = [str(complex(2)), '2', '1', '4']
        parameters_4 = [bin(2), '2', '1', '4']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_3))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_4))

    def test_rectangle_validator_raises_ValueError_if_width_parameter_is_greater_than_canvas_width(self):
        parameters_1 = ['21', '6', '1', '1']
        parameters_2 = ['1', '6', '21', '1']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))

    def test_rectangle_validator_raises_ValueError_if_width_parameter_less_equal_zero(self):
        parameters_1 = ['0', '6', '1', '1']
        parameters_2 = ['3', '6', '-1', '1']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))

    def test_rectangle_validator_raises_ValueError_if_height_parameter_is_greater_than_canvas_height(self):
        parameters_1 = ['1', '7', '3', '2']
        parameters_2 = ['1', '2', '3', '7']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))

    def test_rectangle_validator_raises_ValueError_if_height_parameter_less_equal_zero(self):
        parameters_1 = ['1', '0', '3', '6']
        parameters_2 = ['1', '6', '3', '-1']
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, rectangle_validator(self.cleaned_data, parameters_2))


class FloodFillValidatorTest(unittest.TestCase):

    def setUp(self):
        self.cleaned_data = 20, 6
        self.parameters_1 = ['1', '6', 'd']
        self.parameters_2 = ['20', '1', 'd']

    def test_flood_fill_validator_returns_tuple(self):
        self.assertIsInstance(flood_fill_validator(self.cleaned_data, self.parameters_1), tuple)
        self.assertIsInstance(flood_fill_validator(self.cleaned_data, self.parameters_2), tuple)

    def test_flood_fill_validator_returns_correct_output(self):
        self.assertTupleEqual(flood_fill_validator(self.cleaned_data, self.parameters_1), (1, 6, 'd'))
        self.assertTupleEqual(flood_fill_validator(self.cleaned_data, self.parameters_2), (20, 1, 'd'))

    def test_flood_fill_validator_raises_ValueError_if_length_parameters_not_equal_3(self):
        parameters_1 = ['1', '3', 'd', '7']
        parameters_2 = ['1', '3']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_2))

    def test_flood_fill_validator_raises_ValueError_if_width_or_height_parameters_is_not_digit(self):
        parameters_1 = ['s', '1', 'd']
        parameters_2 = ['1', 's', 'd']
        parameters_3 = [str(float(2)), 's', 'd']
        parameters_4 = ['2', bin(2), 'd']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_2))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_3))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_4))

    def test_fllod_fill_validator_raises_ValueError_if_color_does_not_exist(self):
        parameters_1 = ['2', '3', '']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))

    def test_flood_fill_validator_raises_ValueError_if_width_greater_than_canvas_width(self):
        parameters_1 = ['21', '1', 'c']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))

    def test_flood_fill_validator_raises_ValueError_if_width_less_equal_zero(self):
        parameters_1 = ['0', '1', 'c']
        parameters_2 = ['-1', '1', 'c']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_2))

    def test_flood_fill_validator_raises_ValueError_if_height_greater_than_canvas_height(self):
        parameters_1 = ['1', '7', 'c']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))

    def test_flood_fill_validator_raises_ValueError_if_height_less_equal_zero(self):
        parameters_1 = ['1', '0', 'c']
        parameters_2 = ['1', '-1', 'c']
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_1))
        self.assertRaises(ValueError, flood_fill_validator(self.cleaned_data, parameters_2))


if __name__ == '__main__':
    unittest.main()
