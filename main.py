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
<<<<<<< HEAD
class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    school=ndb.StringProperty(required=True)
    schoolyear=ndb.StringProperty(required=False)
    skill1=ndb.TextProperty(required=True)
    skill2=ndb.TextProperty(required=True)
    skill3=ndb.TextProperty(required=True)
    skill4=ndb.TextProperty(required=True)

    # language= ndb.StringProperty(required=True)

=======
name = []
school = []
schoolyear = []

# class Student(ndb.Model):
#     name = ndb.StringProperty(required=True)
#     story_input = ndb.TextProperty(required=True)
>>>>>>> 11352a1fd4a9843edddf79620127a55fef2085f3


jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class FormHandler(webapp2.RequestHandler):
    def get(self):

        # schoolyear = self.request.get("schoolyear"," ")

        new_student = Student(name=name, content=story_input)
        student_key = new_student.put()
        schoolyear = self.request.get("schoolyear"," ")

        # name = self.request.get("name"," ")
        # school = self.request.get("school"," ")


        response_string = ' '

        template = jinja_environment.get_template('form.html')

        template_vars = {'name':name, 'schoolyear': schoolyear, 'response': response_string}
        self.response.out.write(template.render(template_vars))

    def post(self):

<<<<<<< HEAD
        name = self.request.get('name')
        school = self.request.get('school')
        schoolyear = self.request.get('schoolyear')
        skill1 = self.request.get('skill1')
        skill2 = self.request.get('skill2')
        skill3 = self.request.get('skill3')
        skill4 = self.request.get('skill4')
=======
        name.append(self.request.get('name'))
        self.response.out.write(name)
        # print name
        school.append(self.request.get('school'))
        self.response.out.write(school)
        schoolyear.append(self.request.get('schoolyear'))
        self.response.out.write(schoolyear)
>>>>>>> 11352a1fd4a9843edddf79620127a55fef2085f3
        # skill = self.request.get('skill')
        # activity = self.request.get('activity')

        student=Student(name=name, school=school, schoolyear=schoolyear, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4)
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
<<<<<<< HEAD
    globvar = []
    Stuff = [i.split() for i in globvar]
    newvar =  Stuff
    def get(self):
        user = users.get_current_user()
        newvar = code
=======
    #globvar = []



    def get(self):
        user = users.get_current_user()
        numero = ""

        if len(name) > 0:
            numero = name[0]
        else:
            numero = ""
        globvar = code

        schoolname = ""
        if len(school) > 0:
            schoolname = school[0]
        else:
            schoolname = ""
        year = ""
        if len(schoolyear) > 0:
            year = schoolyear[0]
        else:
            year = ""





>>>>>>> 11352a1fd4a9843edddf79620127a55fef2085f3
        if user:
            greeting = ('Welcome, %s!(<a href="%s">sign out</a>)'%(user.nickname(),users.create_logout_url('/')))
        else:
            greeting = ('<a href ="%s">Sign in or Register</a>.'% users.create_login_url('/'))
        template = jinja_environment.get_template('index.html')
        self.response.out.write('%s'% greeting)
<<<<<<< HEAD
        template_vars = {'newvar': newvar}
=======
        template_vars = {'numero': numero, 'globvar': globvar, 'schoolname': schoolname, 'year': year}
>>>>>>> 11352a1fd4a9843edddf79620127a55fef2085f3
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

        # name = self.request.get('name')
        # story_input = self.request.get('story_input')
        #
        name = self.request.get('name')
<<<<<<< HEAD
        story_input = self.request.get('story_input')
=======
        # story_input = self.request.get('story_input')
        # student_keys = ndb.KeyProperty(kind='Student', repeated=True)

>>>>>>> 11352a1fd4a9843edddf79620127a55fef2085f3
        # lunchbox_instance = LunchBox(
        # food = self.request.get('food'),
        # drink = self.request.get('drink'),
        # insulated = True)
        # my_lunchbox_key = lunchbox_instance.put()
        # Create a new Student and put it in the datastore
        # student = Student(name=name, story_input=story_input)
        # student.put()
        # Redirect to the main handler that will render the template
        self.redirect('/')




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler)
], debug=True)
