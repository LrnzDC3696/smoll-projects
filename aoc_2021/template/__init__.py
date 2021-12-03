def read_n_format_txt_file(file_name = 'input.txt'):
    with open(file_name, 'r') as file:
        string_of_files = file.read()
    return string_of_files.split('\n')

def part_1(input_list):
    pass

def part_2(input_list):
    pass

def main():
    input_from_file = [x for x in read_n_format_txt_file() if bool(x)]
    print(part_1(input_from_file))
    print(part_2(input_from_file))

if __name__ == '__main__':
    main()

