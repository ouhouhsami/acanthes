from django.shortcuts import render_to_response
from django.template import RequestContext
from filtersets import AudioFilterSet
from archives.models import Audio
from django.contrib.auth.decorators import login_required


def home(request):
    filterset = AudioFilterSet(request.GET or None, queryset=Audio.objects.all().order_by('subtitle'))
    home = False
    if len(request.GET) == 0:
        home = True
    return render_to_response('archives/index.html',
                           {'filterset': filterset, 'home':home},
                          context_instance=RequestContext(request))

@login_required
def detail(request, pk):
    audio = Audio.objects.get(id=pk)
    return render_to_response('archives/detail.html', {'audio':audio}, 
                           context_instance=RequestContext(request))
    