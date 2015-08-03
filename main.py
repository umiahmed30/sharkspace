import webapp2
import jinja2
import os
import random
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s!(<a href="%s">sign out</a>)'%(user.nickname(),users.create_logout_url('/')))
        else:
            greeting = ('<a href ="%s">Sign in or Register</a>.'% users.create_login_url('/'))
        self.response.out.write('%s'% greeting)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
