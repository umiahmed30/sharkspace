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

code = []

class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    password= ndb.StringProperty(required=True)
    school=ndb.StringProperty(required=True)
    schoolyear=ndb.StringProperty(required=False)
    skill1=ndb.TextProperty(required=True)
    skill2=ndb.TextProperty(required=True)
    skill3=ndb.TextProperty(required=True)
    skill4=ndb.TextProperty(required=True)
    java=ndb.StringProperty(required=False)
    Python=ndb.StringProperty(required=False)
    HTML=ndb.StringProperty(required=False)
    Javascript=ndb.StringProperty(required=False)
    CSS=ndb.StringProperty(required=False)
    Cplus=ndb.StringProperty(required=False)
    Objective_C=ndb.StringProperty(required=False)
    ruby =ndb.StringProperty(required=False)

    # language= ndb.StringProperty(required=True)



jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class FormHandler(webapp2.RequestHandler):
    def get(self):
        schoolyear = self.request.get("schoolyear"," ")
        name = self.request.get("name"," ")
        school = self.request.get("school"," ")


        response_string = ' '

        template = jinja_environment.get_template('form.html')

        template_vars = {'name':name, 'schoolyear': schoolyear, 'response': response_string}
        self.response.out.write(template.render(template_vars))

    def post(self):

        name = self.request.get('name')
        password = self.request.get('password')
        school = self.request.get('school')
        schoolyear = self.request.get('schoolyear')
        skill1 = self.request.get('skill1')
        skill2 = self.request.get('skill2')
        skill3 = self.request.get('skill3')
        skill4 = self.request.get('skill4')
        java=self.request.get('java')
        Python=self.request.get('Python')
        HTML=self.request.get('HTML')
        Javascript=self.request.get('Javascript')
        CSS=self.request.get('CSS')
        Cplus=self.request.get('Cplus')
        Objective_C=self.request.get('Objective_C')
        ruby = self.request.get('ruby')
        # skill = self.request.get('skill')
        # activity = self.request.get('activity')

        student=Student(name=name, password=password, school=school, schoolyear=schoolyear, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, java=java, Python=Python, HTML=HTML, Javascript=Javascript, CSS=CSS, Cplus=Cplus, Objective_C=Objective_C, ruby=ruby)
        student.put()

        java = self.request.get('java')
        Python = self.request.get('Python')
        HTML = self.request.get('HTML')
        Javascript = self.request.get('Javascript')


        # response_string = "Hi " + name + "You are a " + schoolyear + "." + " You can code " +  java + " "+ python + " "+ HTML+ " "+ Javascript + " "+CSS + " "+Cplus + " "+Objective_C + " "+ruby
        #
        # response_string = "Hi " + name

        CSS = self.request.get('CSS')
        Cplus = self.request.get('Cplus')
        Objective_C = self.request.get('Objective_C')
        ruby = self.request.get('ruby')
        languages = []
        languages.extend([java, Python, HTML, Javascript, CSS, Cplus, Objective_C, ruby])

        for language in languages:
            if language != "":
                code.append(language)


        # response_string = "Hi " + name + "You are a " + schoolyear + "." + " You can code " +  java + " "+ python + " "+ HTML+ " "+ Javascript + " "+CSS + " "+Cplus + " "+Objective_C + " "+ruby




        template = jinja_environment.get_template('form.html')

        template_vars = {'name':name, 'schoolyear': schoolyear}
        self.response.out.write(template.render(template_vars))

class MainHandler(webapp2.RequestHandler):
    globvar = []
    Stuff = [i.split() for i in globvar]
    newvar =  Stuff
    def get(self):
        user = users.get_current_user()
        newvar = code
        if user:
            greeting = ('Welcome, %s!(<a href="%s">sign out</a>)'%(user.nickname(),users.create_logout_url('/')))
        else:
            greeting = ('<a href ="%s">Sign in or Register</a>.'% users.create_login_url('/'))
        template = jinja_environment.get_template('index.html')
        self.response.out.write('%s'% greeting)
        template_vars = {'newvar': newvar}
        self.response.out.write(template.render(template_vars))



        # self.response.write(globvar)

        # # Get all of the student data from the datastore
        # student_query = Student.query()
        # student_query = student_query.order(Student.name)
        # # student_query = student_query.filter(Student.name == 'Adam')
        # student_data = student_query.fetch()
        # # Pass the data to the template
        # template_values = {
        #     'students' : student_data
        # }
        # template = JINJA_ENVIRONMENT.get_template('index.html')
        # self.response.write(template.render(template_values))
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

        # Redirect to the main handler that will render the template
        self.redirect('/')




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler)
], debug=True)
