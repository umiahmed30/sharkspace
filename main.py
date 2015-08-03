import webapp2
import jinja2
import os
import random
from google.appengine.api import users
import jinja2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s!(<a href="%s">sign out</a>)'%(user.nickname(),users.create_logout_url('/')))
        else:
            greeting = ('<a href ="%s">Sign in or Register</a>.'% users.create_login_url('/'))
        template = jinja_environment.get_template('index.html')
        self.response.out.write('%s'% greeting)
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
