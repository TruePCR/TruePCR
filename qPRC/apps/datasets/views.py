from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .forms import DatasetForm
from .models import Dataset

def home(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = Dataset(file=request.FILES['file'])
            new_file.save()
            return HttpResponseRedirect('datasets:home')
    else:
        form = DatasetForm
    data = {'form': form}
    return render_to_response('dashboard.html', data,
                              context_instance=RequestContext(request))
