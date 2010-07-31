from django import shortcuts

def index(request):
    return shortcuts.render_to_response('index.html')
