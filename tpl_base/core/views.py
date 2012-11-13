import datetime
from django.utils.timezone import utc

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from core.forms import LibraryAccountForm
from core.models import LibraryAccount

# TODO: Remove all spaces from library account number
# TODO: Overwrite account when you submit it more than once.

def index(request):
    if request.method == "POST":
        form = LibraryAccountForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.last_check = datetime.datetime.utcnow().replace(tzinfo=utc)
            new_account.save()
            return redirect(thanks)
    else:
        form = LibraryAccountForm()

    return render_to_response("index.html", {
            'form' : form,
        },
        context_instance=RequestContext(request)
    )

def thanks(request):
    return render_to_response("thanks.html")
