from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(name="Edit group name"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="123"))
    app.group.edit_first(Group(header="Edit header name"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", footer="456"))
    app.group.edit_first(Group(footer="Edit footer name"))
