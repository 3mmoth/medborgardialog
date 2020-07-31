from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

from .models import Fraga, Val

# Hämta frågor och visa
def index(request):
    latest_fraga_list = Fraga.objects.order_by('-id')[:5]
    context = {'latest_fraga_list': latest_fraga_list}
    return render(request, 'polls/index.html', context)

# Visa specifika frågor och val
def detail(request, fraga_id):
    try:
        fraga = Fraga.objects.get(pk=fraga_id)
    except Fraga.DoesNotExist:
        raise Http404("Frågan existerar inte")
    return render(request, 'polls/detail.html', {'fraga': fraga})

#Hämta fråga och visa resultat
def results(request, fraga_id):
    fraga = get_object_or_404(Fraga, pk=fraga_id)
    return render(request, 'polls/results.html', {'fraga': fraga})

# Rösta på ett av alternativen
def rosta(request, fraga_id):
    # print(request.POST['choice'])
    fraga = get_object_or_404(Fraga, pk=fraga_id)
    try:
        selected_val = fraga.val_set.get(pk=request.POST['val'])
    except (KeyError, Val.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'fraga': fraga,
            'error_message': "Du gjorde inte ett val.",
        })
    else:
        selected_val.roster += 1
        selected_val.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(fraga.id,)))

def resultsData(request, obj):
  rostdata = []

  fraga = Fraga.objects.get(id=obj)
  roster = fraga.val_set.all()

  for i in roster:
    rostdata.append({i.val_text: i.roster})

  return JsonResponse(rostdata, safe = False)