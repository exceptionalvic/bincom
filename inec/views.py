from django.shortcuts import render, redirect,HttpResponseRedirect, HttpResponse
from .forms import PUSearchForm
from .models import Ward, LGA, Polling_Unit, Announced_PU_Results
from django.core import serializers
import json
from django.contrib import messages
import datetime

# Create your views here.
def pu_results(request):
    # get all wards
    get_wards = Ward.objects.all()
    
    # get input ward
    ward = request.GET.get('ward')
    # filter polling ubit by input ward
    get_pu = (Polling_Unit.objects.filter(ward_id=ward) or None)
    get_pu_uniqueid = request.GET.get('pu')
    pu_results_context = (Announced_PU_Results.objects.filter(polling_unit_uniqueid=get_pu_uniqueid) or None)
    context = {
        'ward_context': get_wards,
        'pu_context':get_pu,
        'pu_results_context':pu_results_context
        }
    # use HTMX to do partial filter and manipulate DOM
    if request.META.get("HTTP_HX_REQUEST") == 'true':
        if ward:
            return render(request, 'filter/partial_pu.html', context)
        else:
            return render(request, 'filter/partial_pu_result.html', context)
    return render(request, 'pu_results.html', context)





def lga_pu_results(request):
    all_lga = LGA.objects.all()
    # get the lga_id input in the select form
    get_lga_id = request.GET.get('lga_id')
    # assign zero to all party polling numbers in LGA
    pdp = 0
    dpp=0
    acn=0
    ppa=0
    cdc=0
    jp=0
    cpp=0
    anpp=0
    labo=0
    # run a forloop to sum all polling unit results in the selected LGA
    sum_pu_results = 0
    # Count the polling units in the selected LGA. set to 0
    count_all_pu =  None
    if get_lga_id:
        '''use if statement to make view load without queries unless an input is called'''
        # get all polling units in an LGA using the lga_id
        get_all_pu = Polling_Unit.objects.filter(lga_id=get_lga_id)
        
        count_all_pu = Polling_Unit.objects.filter(lga_id=get_lga_id).count()
        # run forloop to filter out announced polling unit result of selected LGA
        all_uniqueid = []
        for pu in get_all_pu:
            all_uniqueid.append(pu.uniqueid)
        
        # filter out announced pu results from the list of aggregated pu uniqueids of all polling unit in the selected LGA
        get_all_announced_pu_in_lga = Announced_PU_Results.objects.filter(polling_unit_uniqueid__in=all_uniqueid)
        
        # get total sum of pu results per party in selected LGA
        
        for i in get_all_announced_pu_in_lga:
            # add up total polls accross all units in selected LGA
            sum_pu_results += int(i.party_score)
            # add up each party total score in selected LGA
            pdp += (i.party_score if 'PDP' in i.party_abbreviation else 0)
            dpp += (i.party_score if 'DPP' in i.party_abbreviation else 0)
            acn += (i.party_score if 'ACN' in i.party_abbreviation else 0)
            ppa += (i.party_score if 'PPA' in i.party_abbreviation else 0)
            cdc += (i.party_score if 'CDC' in i.party_abbreviation else 0)
            jp += (i.party_score if 'JP' in i.party_abbreviation else 0)
            cpp += (i.party_score if 'CPP' in i.party_abbreviation else 0)
            anpp += (i.party_score if 'ANPP' in i.party_abbreviation else 0)
            labo += (i.party_score if 'LABO' in i.party_abbreviation else 0)
        
    context ={
        'all_lga':all_lga,
        'count_all_pu':count_all_pu,
        'sum_pu_result':sum_pu_results,
        # 'data':None,
        'PDP':pdp,
        'DPP':dpp,
        'ACN':acn,
        'PPA':ppa,
        'CDC':cdc,
        'JP':jp,
        'CPP':cpp,
        'ANPP':anpp,
        'LABO':labo,
    }
    # print(pdp)
    if request.META.get("HTTP_HX_REQUEST") == 'true':
        return render(request, 'filter/partial_pu_result_by_lga.html',context)
    
    return render(request, 'pu_result_by_lga.html',context)


def add_new_pu_result(request):
    all_pu = Polling_Unit.objects.all()
    # for p in all_pu:
    #     print(p.uniqueid)
    if request.method == 'POST':
        party_abbreviation = request.POST.get('party_abbreviation')
        party_score = request.POST.get('party_score')
        polling_unit_uniqueid = request.POST.get('polling_unit_uniqueid')
        entered_by_user = request.POST.get('entered_by_user')
        date_entered = datetime.datetime.now()
        
        new_poll_data = Announced_PU_Results(party_abbreviation=party_abbreviation,
                                             party_score=party_score,
                                             polling_unit_uniqueid=polling_unit_uniqueid,
                                             entered_by_user=entered_by_user,
                                             date_entered=date_entered
                                             )
        try:
            new_poll_data.save()
            messages.success(request,'New Poll Result Added Successfully')
            return redirect('add_new_poll')
        except Exception as e:
            messages.error(request,'Error occured. {}'.format(str(e)))
            return redirect('add_new_poll')
    context = {
        'all_pu':all_pu
        }
    return render(request, 'add_new_poll.html',context)