
def test_delete_first_contact(app):
    app.contact.delete_first()

def test_delete_all_contacts(app):
    app.contact.delete_all()