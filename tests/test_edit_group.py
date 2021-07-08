from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first(Group(name="Edit group name"))
    app.session.logout()


def test_edit_group_header(app):
    app.group.edit_first(Group(header="Edit header name"))
    app.session.logout()


def test_edit_group_footer(app):
    app.group.edit_first(Group(footer="Edit footer name"))
    app.session.logout()
