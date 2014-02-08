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

"""
Particular Webpage Classes Go below here:
"""

class IntroductionPage(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
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
        self.response.write(template.render(template_values))
class AliasSelectionPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('AliasSelection.html')
        self.response.write(template.render())

    def post(self):
        pass

class AmmazonTemplateEditingPage(webapp2.RequestHandler):
    def get(self):

        defaultTemplate = "We regret to inform you that your current order is has been significantly delayed. \n In order to compensate you for your inconvience we are applying a $50 credit to your account. To confirm this addition click the following link"

        template_values = {
        'defaultTemplate' : defaultTemplate
        }


        template = JINJA_ENVIRONMENT.get_template('AmmazonTemplateEditingPage.html', template_values)
        self.response.write(template.render(template_values))

class BanOfAmericaTemplateEditingPage(webapp2.RequestHandler):
    def get(self):

        defaultTemplate = "There has been suspicious activity on your checking account. \n In order to verify your recent transaction history please click on the link below"
        
        template_values = {
        'defaultTemplate' : defaultTemplate
        }

        template = JINJA_ENVIRONMENT.get_template('BanOfAmericaTemplateEditingPage.html', template_values)
        self.response.write(template.render(template_values))


class LeaderboardPage(webapp2.RequestHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('Leaderboard.html')
        self.response.write(template.render())

    def post(self):
        finalEmail = self.request.get("finalTemplate")
        recipients = self.request.get("recipents")
        alias      = self.request.get("alias")

    def ammazon():
        subject = "Delayed Package"
        sender_address = "Ammazon.User.Help@gmail.com"
        emailInfo = [sender_address,subject]
        return emailInfo

    def BanOfAmerica():
        subject = "suspicious Account Activity"
        sender_address = "BanOfAmerica.User.Help@gmail.com"
        emailInfo = [sender_address,subject]
        return emailInfo

        options = {"ammazon" : ammazon,
                   "banOfAmerica" : banOfAmerica}

        emailInfo = options[alias]()



        for recipent in recipients:
            mail.send_mail(emailInfo[1], recipent, emailInfo[2], finalEmail)


application = webapp2.WSGIApplication([
    ('/', IntroductionPage),
    ('/AliasSelection', AliasSelectionPage),
    ('/TemplateEditing/Ammazon', AmmazonTemplateEditingPage),
    ('/TemplateEditing/BanOfAmerica', BanOfAmericaTemplateEditingPage),
    ('/Leaderboard', LeaderboardPage)
], debug=True)
