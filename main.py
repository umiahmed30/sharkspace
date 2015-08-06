import webapp2
import jinja2
import os
import random
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import logging
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

code = []
name = []

class Student(ndb.Model):
    name = ndb.StringProperty(required=False)
    bio = ndb.StringProperty(required=False)
    password = ndb.StringProperty(required=False)
    github = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    activity = ndb.StringProperty(required=False)
    school = ndb.StringProperty(required=False)
    schoolyear = ndb.StringProperty(required=False)
    skill1 = ndb.TextProperty(required=False)
    skill2 = ndb.TextProperty(required=False)
    skill3 = ndb.TextProperty(required=False)
    skill4 = ndb.TextProperty(required=False)
    java = ndb.StringProperty(required=False)
    Python = ndb.StringProperty(required=False)
    HTML = ndb.StringProperty(required=False)
    Javascript = ndb.StringProperty(required=False)
    CSS = ndb.StringProperty(required=False)
    Cplus = ndb.StringProperty(required=False)
    Objective_C = ndb.StringProperty(required=False)
    ruby = ndb.StringProperty(required=False)
    otherlang = ndb.StringProperty(required=False)
    ID = ndb.StringProperty(required=True)
    pic = ndb.TextProperty(required=False)

    user = ndb.UserProperty(required=True)


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
        template = jinja_environment.get_template('templates/form.html')

        self.response.out.write(template.render())


    def post(self):
        # profilepic = self.request.get('profilepic')
        pic = self.request.get('pic')
        name = self.request.get('name')
        bio = self.request.get('bio')
        github = self.request.get('github')
        email = self.request.get('email')
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
        otherlang = self.request.get('otherlang')
        activity = self.request.get('activity')
        user = users.get_current_user()

        student=Student(name=name, password=password, github=github, email=email, activity=activity, bio=bio, school=school, schoolyear=schoolyear, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, java=java, Python=Python, HTML=HTML, Javascript=Javascript, CSS=CSS, Cplus=Cplus, Objective_C=Objective_C, pic=pic, otherlang=otherlang, ruby=ruby, ID=users.get_current_user().user_id(), user =users.get_current_user(),);
        student.put()

        self.redirect('/submit')

class MainHandler(webapp2.RequestHandler):
    globvar = []
    Stuff = [i.split() for i in globvar]
    newvar =  Stuff

    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('<p style="color:goldenrod;"><strong>Welcome, %s! (<a href="%s"style="color:goldenrod;">sign out</a>)</strong></p>' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
        else:
            greeting = ('<p style="color:goldenrod;"><strong><a href="%s">Sign in or register</a>.</strong></p>' %
                        users.create_login_url('/'))
        # template = jinja_environment.get_template('index.html')
        self.response.out.write("<html><body>%s</body></html>" % greeting)



        student_query = Student.query()
        student_query = student_query.order(Student.name)
        student_query = student_query.filter(Student.user == user )
        student_data = student_query.fetch()
        logging.info(student_data)

        # Pass the data to the template
        template_values = {
            'student' : student_data[0]
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))
        # self.response.write(globvar)

    def post(self):
        avatar = self.request.get('pic')
        student.avatar= avatar
        name = self.request.get('name')
        story_input = self.request.get('story_input')


        # self.response.out.write('%s'% greeting)
        # template_vars = {'newvar': newvar}
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
        # template = jinja_environment.get_template('index.html')
        self.response.out.write("<html><body>%s</body></html>" % greeting)

        print 'umi {}'.format(user.user_id())
        student_query = Student.query()
        student_query = student_query.order(Student.name)
        student_query = student_query.filter(Student.user == user )
        student_data = student_query.fetch()
        logging.info(student_data)

        # Pass the data to the template
        template_values = {
            'students' : student_data
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class UserPrefs(ndb.Model):
    userid = ndb.StringProperty()

class SignInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()


        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
            if userprefs:
                self.redirect('/profile')
            else:
                self.redirect('/signup')
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
    #
        self.response.out.write("<html><body>%s</body></html>" % greeting)
    # template = jinja_environment.get_template('redirect.html')
    # self.response.out.write('%s'% greeting)
    # self.response.out.write(template.render())

class WelcomepageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            print "logged in"
            greeting = ('<p style="color:goldenrod;"><strong>Welcome, %s!(<a href="%s"style= "color:goldenrod;">sign out</a>)</strong></p>'%(user.nickname(),users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
            if userprefs:
                print 'userprefs'
                self.redirect('/profile')
            else:
                print 'no userprefs'
                self.redirect('/signup')
        else:
            print "not logged in"
            greeting = ('<a href="%s" style="color:goldenrod;">Sign in or Register</a>.'% users.create_login_url('/redirect'))


        template = jinja_environment.get_template('templates/welcomepage.html')
        self.response.out.write('%s'% greeting)
        self.response.out.write(template.render())

class ReferenceHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('<p style="color:goldenrod;"><strong>Welcome, %s! (<a href="%s"style="color:goldenrod;">sign out</a>)</strong></p>' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
        else:
            greeting = ('<p style="color:goldenrod;"><strong><a href="%s">Sign in or register</a>.</strong></p>' %
                        users.create_login_url('/'))
        # template = jinja_environment.get_template('index.html')
        self.response.out.write("<html><body>%s</body></html>" % greeting)
        template = jinja_environment.get_template('templates/references.html')
        self.response.out.write(template.render())

class DevTeamHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('<p style="color:goldenrod;"><strong>Welcome, %s! (<a href="%s"style="color:goldenrod;">sign out</a>)</strong></p>' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
        else:
            greeting = ('<p style="color:goldenrod;"><strong><a href="%s">Sign in or register</a>.</strong></p>' %
                        users.create_login_url('/'))
        # template = jinja_environment.get_template('index.html')
        self.response.out.write("<html><body>%s</body></html>" % greeting)
        template = jinja_environment.get_template('templates/devteam.html')
        self.response.out.write(template.render())
class SubmitHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/submit.html')
        self.response.out.write(template.render())
class ContactsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('<p style="color:goldenrod;"><strong>Welcome, %s! (<a href="%s"style="color:goldenrod;">sign out</a>)</strong></p>' %
                        (user.nickname(), users.create_logout_url('/')))
            q = ndb.gql("SELECT * FROM Student WHERE ID = :1", user.user_id())
            userprefs = q.get()
        else:
            greeting = ('<p style="color:goldenrod;"><strong><a href="%s">Sign in or register</a>.</strong></p>' %
                        users.create_login_url('/'))
        # template = jinja_environment.get_template('index.html')
        self.response.out.write("<html><body>%s</body></html>" % greeting)



        student_query = Student.query()
        student_query = student_query.order(Student.name)
        # student_query = student_query.filter(Student.user == user )
        student_data = student_query.fetch()
        logging.info(student_data)

            # Pass the data to the template
        template_values = {
            'student' : student_data
        }


        template = jinja_environment.get_template('templates/contacts.html')
        self.response.out.write(template.render(template_values))






app = webapp2.WSGIApplication([
    ('/', WelcomepageHandler),
    ('/signup', FormHandler),
    ('/profile', MainHandler),
    ('/redirect', SignInHandler),
    ('/references', ReferenceHandler),
    ('/devteam', DevTeamHandler),
    ('/submit', SubmitHandler),
    ('/contacts', ContactsHandler)
], debug=True)
