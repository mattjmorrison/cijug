from django import shortcuts, http
from cijug.microblog import models, forms
from django.core.urlresolvers import reverse

def index(request):
    return shortcuts.render_to_response('microblog/templates/index.html', {'blogs':models.Blog.objects.all()})

def add(request):
    return shortcuts.render_to_response('microblog/templates/add.html', {'blog_form':forms.BlogForm()})

def save_add(request):
    form = forms.BlogForm(request.POST)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse('microblog:index'))
    else:
        return shortcuts.render_to_response('microblog/templates/add.html', {'blog_form':form})

def edit(request, id):
    instance = models.Blog.objects.get(id=id)
    return shortcuts.render_to_response('microblog/templates/edit.html', {'blog_form':forms.BlogForm(instance=instance), 'blog':instance})

def save_edit(request, id):
    instance = models.Blog.objects.get(id=id)
    form = forms.BlogForm(request.POST, instance=instance)
    if form.is_valid():
        form.save()
        return http.HttpResponseRedirect(reverse('microblog:index'))
    else:
        return shortcuts.render_to_response('microblog/templates/edit.html', {'blog_form':form, 'blog':instance})

def delete(request, id):
    models.Blog.objects.get(id=id).delete()
    return http.HttpResponseRedirect(reverse('microblog:index'))
