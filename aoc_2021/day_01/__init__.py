def read_n_format_txt_file(file_name = 'input.txt'):
    with open(file_name, 'r') as file:
        string_of_files = file.read()
    return string_of_files.split('\n')

def part_1(input_list):
    count = 0
    prev = input_list[0]
    for curr in input_list[1:]:
        if curr > prev:
            count += 1
        prev = curr
    return count

def part_2(input_list):
    count = 0
    index = 0

    while True:
        prev = sum(input_list[index:index+3])
        index += 1
        curr = input_list[index:index+3]

        if len(curr) != 3:
            break
        curr = sum(curr)

        if curr > prev:
            count += 1

        prev = curr

    return count

def main():
    input_from_file = [int(x) for x in read_n_format_txt_file() if bool(x)]
    print(part_1(input_from_file))
    print(part_2(input_from_file))

if __name__ == '__main__':
    main()

