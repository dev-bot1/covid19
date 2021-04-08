from django.shortcuts import render

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "134565b106mshe206809cc510420p1ad375jsn7647af74f94c",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()




def helloworldview(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    mylist=sorted(mylist)
    context= {'mylist': mylist}
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total= response['response'][x]['cases']['total']
                deaths= int(total)-int(active)-int(recovered)
        context ={'selectedcountry':selectedcountry,'mylist': mylist,'new': new,'active': active,'critical': critical,'recovered': recovered,'total': total,'deaths': deaths}
        return render(request, 'helloworld.html', context)
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    mylist=sorted(mylist)
    context= {'mylist': mylist}
    return render(request, 'helloworld.html', context)
