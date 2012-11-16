import datetime

from django.conf import settings
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from core.forms import LibraryAccountForm

# TODO: Overwrite account when you submit it more than once.
def index(request):
    bad_login = False

    if request.method == "POST":
        form = LibraryAccountForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)

            if not settings.CONTEXT.TPLService.test_login(new_account):
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

def unsubscribe(request, card_number):
    account = settings.CONTEXT.AccountService.get(card_number)
    if not account:
        raise Http404

    if request.method == "POST":
        settings.CONTEXT.AccountService.unsubscribe(account)
        return redirect(unsubscribe_done)
    else:
        return render_to_response("unsubscribe.html", {
                'account' : account,
            },
            context_instance=RequestContext(request)
        )

def unsubscribe_done(request):
    return render_to_response("unsubscribe_done.html")
