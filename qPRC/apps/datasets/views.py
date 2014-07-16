from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from .forms import DatasetForm
from .models import Dataset

def home(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = Dataset(file=request.FILES['file'])
            new_file.save()
            return HttpResponseRedirect(reverse('datasets:home'))
    else:
        form = DatasetForm
    data = {
        'form': form,
        'datasets': Dataset.objects.all()
    }
    return render_to_response('datasets/index.html', data,
                              context_instance=RequestContext(request))

def detail(request, dataset_id):
    # TODO: verify that we can get contents from S3
    return HttpResponse('details of dataset {}'.format(dataset_id))

# API

from django.core import serializers

def index(request):
    datasets = Dataset.objects.all()
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    return HttpResponse(json_serializer.serialize(datasets))
