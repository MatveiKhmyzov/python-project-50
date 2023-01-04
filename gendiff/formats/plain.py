from gendiff.utils.constants import ADD, DELETE, UPDATED, NESTED


def get_plain(diff_tree):
    plain_lst = plain(diff_tree)
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
    diff_tree.sort(key=lambda d: d['name'])
    for item in range(len(diff_tree)):
        new_path = path + diff_tree[item]['name']
        sentence = 'Property ' + '\'' + new_path + '\''
        value = '[complex value]' if \
            (diff_tree[item]['type'] == NESTED  # noqa: W503
             or isinstance(diff_tree[item]['value'], dict)) \
            else diff_tree[item]['value']  # noqa: W503
        if diff_tree[item]['type'] == NESTED:
            phrase_lst.append(plain(diff_tree[item]['children'],
                              new_path + '.'))
        if diff_tree[item]['type'] == ADD:
            phrase_lst.append(sentence + ' was added with value: '
                              + format_plain_values(value))  # noqa: W503
        if diff_tree[item]['type'] == DELETE:
            phrase_lst.append(sentence + ' was removed')
        if diff_tree[item]['type'] == UPDATED:
            before_value = format_plain_values(value)
            new_value = '[complex value]' if \
                (diff_tree[item]['type'] == NESTED  # noqa: W503
                 or isinstance(diff_tree[item]['new_value'], dict)) \
                else diff_tree[item]['new_value']  # noqa: W503
            after_value = format_plain_values(new_value)
            complex_str = f'{sentence} was updated.' \
                          f' From {before_value}' \
                          f' to {after_value}'
            phrase_lst.append(complex_str)
    return phrase_lst


def format_plain_values(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    elif value == '[complex value]':
        value = '[complex value]'
    elif isinstance(value, str):
        value = "'{}'".format(value)
    else:
        value = "{}".format(value)
    return value
