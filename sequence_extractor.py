def epitop_checker(sequence: list, row: list, epitop: list, amino_acid_residue: str):
    """

    function for checking the original sequence for epitopes
    and copying it to the list of amino acid residues
    :param sequence: list
    :param row: list[str]
    :param epitop: list
    :param amino_acid_residue: str
    :return:
    """
    if int(row[5]) in epitop:
        sequence.append(amino_acid_residue + ' Epitop')
    else:
        sequence.append(amino_acid_residue)


def sequence_constructor():
    """

    function for creating modified sequence txt-file
    :return: list
    """
    file_name = input("Имя/путь до файла для построения последовательности: ")
    start = int(input("Введите начало последовательности: "))
    end = int(input("Окончить построение последовательности на порядковом номере: "))
    epitop = input("Введите номера аминокислотных остатков рецептора, соприкасающихся с лигандом: ").split(', ')
    sequence_file_name = input("Записать файл последовательности как: ")

    epitop = [int(i) for i in epitop]
    sequence = []

    with open(file_name, 'r') as file:
        for row in file:
            row = row.split()
            if end >= int(row[5]) >= start:
                amino_acid_residue = row[3] + row[5]
                if sequence:
                    if sequence[-1].split()[0] != amino_acid_residue:
                        epitop_checker(sequence, row, epitop, amino_acid_residue)
                else:
                    epitop_checker(sequence, row, epitop, amino_acid_residue)

    with open(sequence_file_name + '.txt', 'w') as sequence_file:
        for data in sequence:
            sequence_file.write(data + '\n')
        sequence_file.write("Длина непрерывной аминокислотной последовательности: {}".format(len(sequence)))

    return sequence


if __name__ == "__main__":
    print(sequence_constructor())
