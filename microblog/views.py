from django import shortcuts
from cijug.microblog import models

def index(request):
    return shortcuts.render_to_response('index.html', {'blogs':models.Blog.objects.all()})
