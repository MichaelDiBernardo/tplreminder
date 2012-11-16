import datetime

from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from core.forms import LibraryAccountForm

# TODO: Remove all spaces from library account number
# TODO: Overwrite account when you submit it more than once.
def index(request):
    bad_login = False

    if request.method == "POST":
        form = LibraryAccountForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)

            if settings.CONTEXT.TPLService.test_login(new_account):
                settings.CONTEXT.AccountService.register_new(new_account)
                return redirect(thanks)
            else:
                bad_login = True

    else:
        form = LibraryAccountForm()

    return render_to_response("index.html", {
            'form' : form,
            'bad_login' : bad_login,
        },
        context_instance=RequestContext(request)
    )

def thanks(request):
    return render_to_response("thanks.html")
