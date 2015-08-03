import webapp2
import jinja2
import os
import random
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    story_input = ndb.TextProperty(required=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # user = users.get_current_user()
        # if user:
        #     greeting = ('Welcome, %s!(<a href="%s">sign out</a>)'%(user.nickname(),users.create_logout_url('/')))
        # else:
        #     greeting = ('<a href ="%s">Sign in or Register</a>.'% users.create_login_url('/'))
        # self.response.out.write('%s'% greeting)
        # Get all of the student data from the datastore
        student_query = Student.query()
        student_query = student_query.order(Student.name)
        # student_query = student_query.filter(Student.name == 'Adam')
        student_data = student_query.fetch()
        # Pass the data to the template
        template_values = {
            'students' : student_data
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    def post(self):
        # Get the student name and university from the form
        name = self.request.get('name')
        story_input = self.request.get('story_input')
        # lunchbox_instance = LunchBox(
        # food = self.request.get('food'),
        # drink = self.request.get('drink'),
        # insulated = True)
        # my_lunchbox_key = lunchbox_instance.put()
        # Create a new Student and put it in the datastore
        student = Student(name=name, story_input=story_input)
        student.put()
        # Redirect to the main handler that will render the template
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
