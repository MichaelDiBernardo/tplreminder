tplreminder: Don't forget your books are due 
============================================


What is this?
-------------
The Toronto Public Library (http://www.torontopubliclibrary.ca/) allows you to
renew books online, which is great. However, they only email you after your
books are _overdue_. They are apparently [working on it](http://torontopubliclibrary.typepad.com/webteam/2012/02/improvements-to-holds-and-overdue-notification.html),
but until then, you can use this instead. It lives at
http://tplreminder.mikedebo.ca, or you can install it yourself.


How does it work?
-----------------
`tplreminder` is a Python/Django app, although the core fetching and parsing
stuff is just pure python. 

If you want to run this locally instead of using the public service (which
keeps your library card numbers and PINs in your own datasphere), life will be
easier if you use `virtualenv`. Create and activate a virtualenv for
tplreminder, clone the project, change to the project root, and do this:

    pip install -r requirements.py
    cp tplreminder/settings_local.py.default tplreminder/settings_local.py
    vi (or whatever) tplreminder/settings_local.py (set things up as needed)
    ./manage.py syncdb
    ./manage.py migrate

Now set up a cron job to run `./manage.py run_batch` every 24 hours, and you
should be set. 


Why did you do this?
--------------------
Two reasons:

* I thought people mightfind it useful.
* It bothers me that TPL can't already do this.

Not that I blame them. It at first seemed ridiculous to me that a public service
capable of emailing me _after_ my books were due shouldn't be equally capable
of doing the same ahead of time, but I was being hasty. I have no idea what
monolithic, proprietary system they may be locked into, but I've worked with
enough of those to know how painful the simplest changes can be.

Then again, maybe it was just a money grab. Again, I don't blame them. In fact,
if you find this service useful, [consider donating to the TPL](http://tplfoundation.ca/become_a_donor). 


