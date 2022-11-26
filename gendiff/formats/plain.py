from gendiff.formats.validators import get_format_values


def get_plain(file):
    return plain(file)


def plain(diff_tree, path=None):  # noqa: C901
    if not path:
        path = ''
    phrase = ''
    for item in diff_tree:
        new_path = path + item['name']
        if item['type'] == 'internal node':
            phrase += plain(item['children'], new_path + '.')
        sentence = 'Property ' + '\'' + new_path + '\''
        value = '[complex value]' if item['type'] == 'internal node' \
            else item['value']
        if item['action'] == 'add':
            phrase += sentence + ' was added with value: '\
                + get_format_values(value) + '\n'
        if item['action'] == 'delete':
            phrase += sentence + ' was removed' + '\n'
        if item['action'] == 'to update':
            before_value = value
            phrase += sentence + ' was updated. From '\
                + get_format_values(before_value) + ' to '
        if item['action'] == 'updated':
            after_value = value
            phrase += get_format_values(after_value) + '\n'

    return phrase
