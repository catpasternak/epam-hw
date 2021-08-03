"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""


def yield_from_file(path_to_file):
    """Generates integers from file.
    :param path_to_file: path to file that contains only integers, one per line
    :type path_to_file: str
    :return: yields integers one by one
    :rtype: Genarator
    """
    with open(path_to_file) as file_input:
        for line in file_input:
            yield int(line.rstrip())


def create_list_of_incoming_gens(file_list):
    """Creates list that contains generators that generate integers from given files.
    :param file_list: list of files with integers sorted from min to max
    :type file_list: List[str]
    :return: list of generators created from files from list of files
    :rtype: List[Generator]
    """
    incoming_gens = []
    for file_name in file_list:
        incoming_gen = yield_from_file(file_name)
        incoming_gens.append(incoming_gen)
    return incoming_gens


def find_next_to_yield(incoming_values):
    """Finds minimun value in list. There might be None values in list.
    :param incoming_values: list of next values from list of generators
    :type incoming_values: List[int, None]
    :return: minimum value among values
    :rtype: int
    """
    for value in incoming_values:
        if value is not None:
            next_to_yield = value
            break
    for value in incoming_values:
        if value is not None:
            if value < next_to_yield:
                next_to_yield = value
    return next_to_yield


def merge_sorted_files(file_list):
    """Generates sequence that contains integers from files in ascending order.
    - Creates list of generators, one from each file;
    - Creates list of next values from each generator;
    - Yields minimum value from list, replaces it with next() from respective generator;
    - Performs until no values left.
    :param file_list: list of files with integers sorted from min to max
    :type file_list: List[str]
    :return: iterator from all integers from files in ascending order
    :rtype: Generator
    """
    incoming_gens = create_list_of_incoming_gens(file_list)
    index_list = [num for num in range(len(incoming_gens))]
    incoming_values = [placeholder for placeholder in index_list]

    while True:
        for index in index_list:
            try:
                incoming_values[index] = next(incoming_gens[index])
            except StopIteration:
                incoming_values[index] = None

        if set(incoming_values) == {None}:
            break

        next_to_yield = find_next_to_yield(incoming_values)
        yield next_to_yield
        index_list = [incoming_values.index(next_to_yield)]
