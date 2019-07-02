from validation import (
    canvas_instruction_validator,
    pre_validate_instruction,
    line_validator,
    rectangle_validator,
    flood_fill_validator,
)
from functions import (
    initialize_canvas,
    draw_into_output,
    get_instructions,
    add_line,
    get_coordinates_to_draw_rect_with_addline_function,
    add_rectangle,
    to_flood_fill,
)


def main():
    if canvas_instruction_validator():
        cleaned_data = canvas_instruction_validator()
        canvas = initialize_canvas(cleaned_data)
        draw_into_output(canvas)

        all_instructions = get_instructions()
        if all_instructions:

            for instruction in all_instructions:
                instruction = instruction.split()
                if pre_validate_instruction(instruction):
                    command, parameters = pre_validate_instruction(instruction)

                    if command == 'L' and line_validator(cleaned_data, parameters):
                        clean_parameters = line_validator(cleaned_data, parameters)
                        add_line(canvas, clean_parameters)
                        draw_into_output(canvas)

                    elif command == 'R' and rectangle_validator(cleaned_data, parameters):
                        clean_parameters = rectangle_validator(cleaned_data, parameters)
                        coordinates = get_coordinates_to_draw_rect_with_addline_function(clean_parameters)
                        add_rectangle(canvas, coordinates)
                        draw_into_output(canvas)

                    elif command == 'B' and flood_fill_validator(cleaned_data, parameters):
                        pos_x, pos_y, color = flood_fill_validator(cleaned_data, parameters)
                        to_flood_fill(canvas, pos_x, pos_y, color)
                        draw_into_output(canvas)


if __name__ == '__main__':
    main()
