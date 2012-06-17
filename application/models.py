"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db


class ExampleModel(db.Model):
    """Example Model"""
    example_name = db.StringProperty(required=True)
    example_description = db.TextProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)


class Post(db.Model):
    title = db.StringProperty(required=True)
    author = db.UserProperty(required=True)
    body = db.TextProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)


class Project(db.Model):
    name = db.StringProperty(required=True)
    author = db.UserProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)
