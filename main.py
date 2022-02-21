from copy import copy


def get_signed_permutations(perm_list):
    total_signed_permutations = []
    for perm in perm_list:
        for signed_comb in get_signed_combinations(perm, signed_combinations=[]):
            total_signed_permutations.append(signed_comb)

    return total_signed_permutations


def get_signed_combinations(input_list, start_index=0, signed_combinations=[]):
    signed_combinations.append(input_list)

    for i in range(start_index, len(input_list)):
        combination = copy(input_list)
        combination[i] = -combination[i]

        if i is len(input_list) - 1:
            signed_combinations.append(combination)
        else:
            get_signed_combinations(combination, start_index=i+1, signed_combinations=signed_combinations)

    return signed_combinations


def get_permutations_of_integer(integer):
    ints = []
    for i in range(1, integer+1):
        ints.append(i)

    return get_permutations(ints)


def get_permutations(int_list):
    if len(int_list) == 1:
        return int_list

    perm_list = []
    for i in int_list:
        remaining_elements = [x for x in int_list if x != i]
        remaining_perms = get_permutations(remaining_elements)

        for permutation in remaining_perms:
            perm_list.append([i, permutation] if len(remaining_perms) == 1 else [i] + permutation)

    return perm_list


def output_to_file(results, file_path):
    with open(file_path, 'w') as reader:
        reader.write(str(len(results)) + '\n')
        for permutation in results:
            reader.writelines(' '.join(map(str, permutation)))
            reader.write('\n')


permutations = get_permutations_of_integer(5)
signed_permutations = get_signed_permutations(permutations)
print(signed_permutations)
print(len(signed_permutations))
