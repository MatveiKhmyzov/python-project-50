def get_plain(file):
    return plain(file)


def get_format_values(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if value == "[complex value]":
        return "[complex value]"
    else:
        return "'{}'".format(value)


def plain(diff_tree, path=None):  # noqa: C901
    if not path:
        path = ""
    phrase = ""
    for item in diff_tree:
        new_path = path + item["name"]
        if type(item["children"]) is list:
            phrase += plain(item["children"], new_path + ".")
        if item["action"] == 'add':
            value = "[complex value]" if type(item["children"]) is list\
                else item["children"]
            phrase += "Property " + "'" + new_path + "'" +\
                      " was added with value: "\
                      + get_format_values(value) + "\n"
        if item["action"] == 'delete':
            phrase += "Property " + "'" + new_path + "'" + " was removed" + "\n"
        if item["action"] == "to update":
            before_value = "[complex value]" \
                if type(item["children"]) is list else item["children"]
            phrase += "Property " + "'" + new_path + "'" +\
                      " was updated. From "\
                      + get_format_values(before_value) + " to "
        if item["action"] == "updated":
            after_value = "[complex value]" \
                if type(item["children"]) is list else item["children"]
            phrase += get_format_values(after_value) + "\n"

    return phrase
