from gendiff.formats.validators import get_format_values


def get_plain(file):
    plain_lst = plain(file)
    result = []

    def walk(subtree):
        for item in subtree:

            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(plain_lst)

    return "\n".join(result)


def plain(diff_tree, path=None):  # noqa: C901
    if not path:
        path = ''
    phrase_lst = []
    for item in range(len(diff_tree)):
        new_path = path + diff_tree[item]['name']
        if 'children' in diff_tree[item]:
            phrase_lst.append(plain(diff_tree[item]['children'],
                              new_path + '.'))
        sentence = 'Property ' + '\'' + new_path + '\''
        value = '[complex value]' if \
            ('children' in diff_tree[item]  # noqa: W503
             or isinstance(diff_tree[item]['value'], list))\
            else diff_tree[item]['value']  # noqa: W503
        if diff_tree[item]['type'] == 'add':
            phrase_lst.append(sentence + ' was added with value: '
                              + get_format_values(value))  # noqa: W503
        if diff_tree[item]['type'] == 'delete':
            phrase_lst.append(sentence + ' was removed')
        if diff_tree[item]['type'] == 'updated':
            before_value = get_format_values(value)
            after_value = get_format_values(diff_tree[item]['new_value'])
            complex_str = f'{sentence} was updated.' \
                          f' From {before_value}' \
                          f' to {after_value}'
            phrase_lst.append(complex_str)
    return phrase_lst
