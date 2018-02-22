__author__ = 'jet'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        error_messages={'required': 'please input username'},

    )
    password = forms.CharField(
        required=True,
        label='password',
        error_messages={'required': u'please input password'},
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("username and password are required")
        else:
            cleaned_data = super(LoginForm, self).clean()


class QuestionsForm(forms.Form):
    title = forms.CharField(
        required=True,
        label='title',
        error_messages={'required': 'please input question title'},
    )

    content = forms.Textarea()


class AnswersForm(forms.Form):
    content = forms.Textarea()

class UserProfile(forms.Form):

    age = forms.IntegerField(
        required=True,
        label='age',
        error_messages={'required': 'Please insert an age.'},

    )

    birthday= forms.DateField(
        required=True,
        label='age',
        error_messages={'required': 'Please insert birthday in the format of (mm/dd/yy)'},
    )


    motherland = models.TextField(
        required=True)
        label="motherland",
        error_messages={'required': 'Please insert the country of your native land'},
    )

    school = models.TextField(
        required=True)
        label = "school",
        error_messages = {'required': 'Please insert the country of your native land'},
    )

   major = models.CharField(
        required=True)
        label = "major",
        error_messages = {'required': 'Please insert your main subject of studies. Ex: Software Engineering'},
    )

    city = models.TextField(
        required=True)
        label = "city",
        error_messages = {'required': 'Please insert the name of your current city'},
    )

