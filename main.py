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

class TemplateEditingPage(webapp2.RequestHandler):
    def get(self):

        def aamazon():
            ammazonTemplate = "We regret to inform you that your current order is has been significantly delayed. \n In order to compensate you for your inconvience we are applying a $50 credit to your account. To confirm this addition click the following link"
            return ammazonTemplate

        def banOA():
            banOATemplate = "There has been suspicious activity on your checking account. \n In order to verify your recent transaction history please click on the link below"
            return banOATemplate

        options = {"Ammazon.User.Help" : aamazon,
                 "BanOfAmerica.User.Help" : banOA
        }

        alias = self.request.get('alias')


        defaultTemplate = options[alias]()

        template_values = {
        'alias' : alias,
        'defaultTemplate' : defaultTemplate
        }

        template = JINJA_ENVIRONMENT.get_template('TemplateEditingPage.html', template_values)
        self.response.write(template.render(template_values))

    # def post(self):
        
    #     finalTemplate = self.request.get("editedTemplateEmail")

    #     template_values = {
    #     'finalTemplate' : finalTemplate
    #     }

class LeaderboardPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Leaderboard.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', IntroductionPage),
    ('/AliasSelection', AliasSelectionPage),
    ('/TemplateEditing', TemplateEditingPage),
    ('/LeaderboardPage', LeaderboardPage)
], debug=True)
