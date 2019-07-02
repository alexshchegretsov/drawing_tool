from typing import Optional


def canvas_instruction_validator() -> Optional[tuple]:
    try:
        with open('input.txt', 'r') as file:
            line = file.readline().split()
            if line[0] == 'C' and len(line) == 3:
                if line[1].isdigit() and line[2].isdigit() and int(line[1]) and int(line[2]):
                    return int(line[1]), int(line[2])
                else:
                    raise ValueError
            else:
                raise ValueError
    except IndexError:
        print('ERROR! Canvas instruction does not exist.')
    except FileNotFoundError:
        print('ERROR! No such file or directory: "input.txt"')
    except ValueError:
        print('ERROR! Invalid Canvas instruction')
    except:
        print('ERROR!')


def pre_validate_instruction(instruction: list) -> Optional[tuple]:
    try:
        if instruction[0] in ('B', 'L', 'R') and 3 < len(instruction) < 6:
            return instruction[0], instruction[1:]
        else:
            raise ValueError

    except ValueError:
        print(f'ERROR! Wrong Command "{" ".join(instruction)}".')
    except IndexError:
        print('ERROR! Empty instruction.')


def line_validator(cleaned_data: tuple, parameters: list) -> Optional[list]:
    try:
        width, height = cleaned_data
        if len(parameters) == 4:
            if parameters[0].isdigit() and parameters[1].isdigit() and \
                    parameters[2].isdigit() and parameters[3].isdigit():
                if 0 < int(parameters[0]) <= width and 0 < int(parameters[1]) <= height and \
                        0 < int(parameters[2]) <= width and 0 < int(parameters[3]) <= height:
                    if parameters[0] == parameters[2] or parameters[1] == parameters[3]:
                        return [int(parameter) for parameter in parameters]
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
    except:
        print(f'ERROR! Wrong Line instruction "L {" ".join(parameters)}".')


def rectangle_validator(cleaned_data: tuple, parameters: list) -> Optional[list]:
    try:
        width, height = cleaned_data
        if len(parameters) == 4:
            if parameters[0].isdigit() and parameters[1].isdigit() and \
                    parameters[2].isdigit() and parameters[3].isdigit():
                if 0 < int(parameters[0]) <= width and 0 < int(parameters[1]) <= height and \
                        0 < int(parameters[2]) <= width and 0 < int(parameters[3]) <= height:
                    return [int(parameter) for parameter in parameters]
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print(f'ERROR! Wrong Rectangle instruction "R {" ".join(parameters)}".')


def flood_fill_validator(cleaned_data: tuple, parameters: list) -> Optional[tuple]:
    try:
        width, height = cleaned_data
        if len(parameters) == 3:
            if parameters[0].isdigit() and parameters[1].isdigit() and \
                    0 < int(parameters[0]) <= width and 0 < int(parameters[1]) <= height and parameters[2]:
                return int(parameters[0]), int(parameters[1]), parameters[2]
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print(f'ERROR! Wrong Bucket instruction B {" ".join(parameters)}.')
