from django.forms.models import ModelForm
from cijug.microblog import models


class BlogForm(ModelForm):
    class Meta:
        model = models.Blog