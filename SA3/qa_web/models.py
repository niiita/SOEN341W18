from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
       User will be able to insert his or her personal information,
       this will then be uploaded and saver the appropriate database.
       Furthermore, these fields are added to the pre-existing fields provided
       by Django such as first name, last name, email.

     """

    Age = models.IntegerField(null =True)
    Birthday = models.DateField(null = True)
    Motherland=models.TextField(max_length=100, null =True)
    School = models.TextField(max_length=100, null =True)
    Major = models.CharField(max_length=50, null =True)
    City = models.TextField(max_length=100, null=True)

    """
      The below code has a purpose that a user profile will be created when
      a user is created

     """

    def create_profile(self):
        pass






class Post(models.Model):
    """
    Parent meta class that describes a post as a publication on the website with certain content
    created by a certain owner
    This will be used for inheritance
    """
    content = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null= True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    class Meta:
        abstract = True

    @property
    def score(self):
        return self.upvotes - self.downvotes

class Questions(Post):
    """
    The question (or thread) initiates the interaction between users' answers,
    comments, and voting
    """
    title = models.CharField(max_length=300, null=True)
    visits = models.IntegerField(default=0)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='q_voters', through='Vote')

    def __str__(self):
        return self.title
    
class Answers(Post):
    """
    The answer is a proposed solution to a certain question
    There can be many answers to a question and there is only one correct answer per question
    """
    question = models.ForeignKey(Questions, null=True, on_delete=models.CASCADE)
    correct_answer = models.BooleanField(default = False)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='a_voters', through='Vote')

class Comments(Post):
    """
    A comment can be posted for an entire question or an answer
    There can be many comments to questions and answers
    """
    question = models.ForeignKey(Questions, null=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, null=True, on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='c_voters', through='Vote')

class Tags(models.Model):
    """
    One or multiple tags can be assigned to a question, in order to classify the question
    There can be many tags to a question
    """
    question = models.ForeignKey(Questions, null= True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, null=True)

class Vote(models.Model):
    """
    Defines the relationship between a user voting and the post
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    positive = models.BooleanField()