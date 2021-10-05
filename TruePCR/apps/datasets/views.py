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

def overview(request, dataset_id):
    dataset = Dataset.objects.get(pk=dataset_id)
    dna = dataset.data()
    well, dye = dna.columns[0]
    wells, dyes = dna.columns.levels
    url = "/{}/well/{}/dye/{}".format(dataset_id, well, dye)
    # TODO: what was this url for?
    data = {'dna': dna, 'wells': wells, 'dyes': dyes}
    return render_to_response('datasets/overview.html', data,
                              context_instance=RequestContext(request))

def detail(request, dataset_id):
    # TODO: some way to open http://localhost:8000/1/well/15/dye/ROX
    dataset = Dataset.objects.get(pk=dataset_id)
    dna = dataset.data()
    return HttpResponse('<h1>Dataset {}</h1>{}'.format(dataset_id,
                                                       dna.to_html()))

# API

from django.core import serializers

def index(request):
    datasets = Dataset.objects.all()
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    return HttpResponse(json_serializer.serialize(datasets))

def well(request, dataset_id, well, dye):
    """well number, dye as parameters"""
    dataset = Dataset.objects.get(pk=dataset_id)
    dna = dataset.data()
    #print(dataset.fit(31, 'SYBR'))
    # TODO: API endpoint to get fitted vals
    well_json = dna.loc[:, (int(well), dye)].to_json()
    return HttpResponse(well_json)

def concentrations_model(request, dataset_id, well, dye):
    """time series of modelled contenctrations for well, dye"""
    dataset = Dataset.objects.get(pk=dataset_id)
    concentrations = dataset.fitted_values(well, dye)
    concentrations_json = concentrations.to_json()
    return HttpResponse(concentrations_json)
