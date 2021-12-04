def read_n_format_txt_file(file_name = 'input.txt'):
    with open(file_name, 'r') as file:
        string_of_files = file.read()
    return string_of_files.split('\n')

def part_1(input_list):
    length = len(input_list[0])
    one_count = [0 for _ in range(length)]
    zero_count = [0 for _ in range(length)]
    for string in input_list:
        for x, char in enumerate(string):
            if char == '0':
                zero_count[x] += 1
            elif char == '1':
                one_count[x] += 1
            else:
                raise
    gamma = ''
    epsilon = ''
    for x, y in zip(one_count, zero_count):
        gamma += '1' if x > y else '0'
        epsilon += '0' if x > y else '1'

    return int(gamma, base=2) * int(epsilon, base=2)

def part_2(input_list):
    pass

def main():
    input_from_file = [x for x in read_n_format_txt_file() if bool(x)]
    print(part_1(input_from_file))
    print(part_2(input_from_file))

if __name__ == '__main__':
    main()

