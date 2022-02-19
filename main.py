from copy import copy


def get_signed_permutations(perm_list):
    total_signed_permutations = []
    for perm in perm_list:
        total_signed_permutations.append(perm)
        for i in range(len(perm)):
            partial_signed_perm = perm[:]
            current_signed_perm = partial_signed_perm[:]
            for j in range(i, len(perm)):
                current_signed_perm[j] = -perm[j]
                total_signed_permutations.append(copy(current_signed_perm))

    return total_signed_permutations


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


def output_to_file(signed_permutations, file_path):
    with open(file_path, 'w') as reader:
        reader.write(str(len(signed_permutations)) + '\n')
        for permutation in signed_permutations:
            reader.writelines(' '.join(map(str, permutation)))
            reader.write('\n')


permutations = get_permutations_of_integer(3)
print(permutations)
signed_permutations = get_signed_permutations(permutations)
print(signed_permutations)
print(len(signed_permutations))

#output_to_file(signed_permutations,
#               'C:\\Users\\masterofdoom\\code projects\\PycharmProjects\\signed-permutations\\results.text')
