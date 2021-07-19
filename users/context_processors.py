from users.forms import ContactUsForm

def contact_form(request):
    form = ContactUsForm()
    return  {"form": form}
