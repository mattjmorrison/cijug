from django import shortcuts
from java.util import Date

def index(request):
    return shortcuts.render_to_response('news/templates/index.html', {'date': Date()})
