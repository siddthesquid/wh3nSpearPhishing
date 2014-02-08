#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import mail

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

"""
Helper Classes Go Below Here:
"""

TEMPLATE_EDITING_PAGE_HTML = """\
<html>
  <body>
    <form action="/TemplateEmail" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""

class ConfirmUserSignup(webapp2.RequestHandler):
    def post(self):
        recepient_address = self.request.get("recepient_address")

        if not mail.is_email_value(recepient_address):
            # prompt user to enter a valid address

        else:
            confirmation_url = createNewUserConfirmation(self.request)
            sender_address = "Example.com Support <support@example.com>"
            subject = "Confirm your registration"
            body = """
                    Thank you for creating an account! Please confirm your email address by
                    clicking on the link below:

                    %s
                    """ % confirmation_url

            mail.send_mail(sender_address, user_address, subject, body)



"""
Particular Webpage Classes Go below here:
"""

class IntroductionPage(webapp2.RequestHandler):
    def get(self):
    	pass
        """if users.get_current_user():
            logUrl = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            logUrl = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

		template_values = {
            'logUrl': logUrl,
            'url_linktext': url_linktext,
            }
    	template = JINJA_ENVIRONMENT.get_template('Introduction.html')
    	"""self.response.write(template.render(template_values))

class AliasSelectionPage(webapp2.RequestHandler):
	def get(self):
		pass

class TemplateEditingPage(webapp2.RequestHandler):
	def get(self):
        pass

    def post(self):
        
        template_body
        sender_address = self.request.get('sender_address')

        if  # check if user still logged in
            pass
        
        else: # render the page



        template_values = {
            'template_body': template_body,
            'recepient': recepient,
        }

        template = JINJA_ENVIRONMENT.get_template('TemplateEmail.html')
        self.response.write(template.render(template_values))

class TemplateEmail(webapp2.RequestHandler):
    def post(self):
        recepient_address = self.request.get("recepient_address")

        if mail.is_email_value(recepient_address):
            # prompt user to enter a valid address


		template = JINJA_ENVIRONMENT.get_template('TemplateEditingPage.html')
		self.response.write(template.render(template_values))
	def post(self):
		finalTemplateBody = self.request.get("editedTemplateBody")

		template_values = {
		'finalTemplateBody' = finalTemplateBody
		}
		self.response.write(template.render(template_values))

		#self.redirect('/?' + urllib.urlencode(query_params))

class LeaderboardPage(webapp2.RequestHandler):
	def get(self):
		pass

app = webapp2.WSGIApplication([
    ('/', IntroductionPage),
    ('/AliasSelection', AliasSelectionPage),
    ('/TemplateEditing', TemplateEditingPage),
    ('/TemplateEmail', )
    ('/LeaderboardPage', LeaderboardPage)
], debug=True)
