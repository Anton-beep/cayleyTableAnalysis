def transformTableToDict(table):
    out = dict()

    key1 = list()
    for el in example[1:]:
        key1.append(el[0])

    key2 = table[0]

    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            ind1 = key1[j - 1]
            ind2 = key2[i - 1]
            if ind1 not in out:
                out[ind1] = dict()
                out[ind1][ind2] = table[j][i]
                continue

            out[ind1][ind2] = table[j][i]

    return key1, key2, out


def custom_permutations(iterable, r=None):
    n = len(iterable)
    r = n if r is None else r

    def generate_permutations(arr, start=0):
        if start == r:
            return [tuple(arr[:r])]
        permutations = []
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]
            permutations.extend(generate_permutations(arr, start + 1))
            arr[start], arr[i] = arr[i], arr[start]
        return permutations

    return generate_permutations(list(iterable))


def analyseCayley(table):
    key1, key2, table = transformTableToDict(table)

    is_associative = True
    for option in custom_permutations(key1, 3):
        if table[option[0]][table[option[1]][option[2]]] != table[table[option[0]][option[1]]][option[2]]:
            is_associative = False
            print("ass. err: " + str(option))
            break

    print("associative: " + str(is_associative))

    is_commutative = True
    for option in custom_permutations(key1, 2):
        if table[option[0]][option[1]] != table[option[1]][option[0]]:
            is_commutative = False
            break

    print("commutative: " + str(is_commutative))

    regular_element = None
    for arg1 in key1:
        is_regular_arg1 = False
        for arg2 in key2:
            if table[arg2][arg1] == table[arg1][arg2] == arg2:
                is_regular_arg1 = True
            else:
                is_regular_arg1 = False
                break
        if is_regular_arg1:
            regular_element = arg1
            break

    print("regular el: " + str(regular_element))

    if regular_element is not None:
        all_have_symmetric = True
        for arg1 in key1:
            symm_for_arg1 = False
            for arg2 in key2:
                if table[arg1][arg2] == table[arg2][arg1] == regular_element:
                    symm_for_arg1 = True
                    break

            if not symm_for_arg1:
                all_have_symmetric = False
                break

        print("all have symmetric: " + str(all_have_symmetric))
    else:
        all_have_symmetric = False
        print("no symmetric el for all els")

    if is_associative and (regular_element is not None) and all_have_symmetric and is_commutative:
        print("it is Abelian group")
    elif is_associative and (regular_element is not None) and all_have_symmetric:
        print("it is group")
    elif is_associative and (regular_element is not None):
        print("it is monoid")
    elif is_associative:
        print("it is semigroup")
    else:
        print("it is none")


example = [
    [0, 1, 2, 3],
    [0, 3, 1, 2, 0],
    [1, 1, 3, 0, 1],
    [2, 2, 0, 3, 2],
    [3, 0, 1, 2, 3],
]

# example = [
#     ["s", "t", "u", "v"],
#     ["s", "s", "t", "u", "v"],
#     ["t", "t", "s", "v", "u"],
#     ["u", "u", "v", "s", "t"],
#     ["v", "v", "u", "t", "s"],
# ]

analyseCayley(example)
