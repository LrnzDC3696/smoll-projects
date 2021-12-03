def read_n_format_txt_file(file_name = 'input.txt'):
    with open(file_name, 'r') as file:
        string_of_files = file.read()
    return string_of_files.split('\n')

def part_1(list_of_input):
    horizontal_value = 0
    depth = 0
    for string in list_of_input:
        direction, n = string.split(' ')
        n = int(n)
        if direction == 'forward':
            horizontal_value += n
        elif direction == 'down':
            depth += n
        elif direction == 'up':
            depth -= n
        else:
            raise
    return horizontal_value * depth

def part_2(list_of_input):
    aim = 0
    horizontal_value = 0
    depth = 0
    for string in list_of_input:
        direction, n = string.split(' ')
        n = int(n)
        if direction == 'forward':
            horizontal_value += n
            depth += n * aim
        elif direction == 'down':
            aim += n
        elif direction == 'up':
            aim -= n
        else:
            raise
    return horizontal_value * depth

def main():
    input_from_file = [x for x in read_n_format_txt_file() if bool(x)]
    print(part_1(input_from_file))
    print(part_2(input_from_file))

if __name__ == '__main__':
    main()

