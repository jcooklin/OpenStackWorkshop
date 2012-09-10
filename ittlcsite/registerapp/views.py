import logging
from registerapp.models import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import json

logger = logging.getLogger(__name__)

def register(request,server,login):
    try:
        host = Host.objects.get(name=server)
    except ObjectDoesNotExist:
        host = Host(name=server)
        host.save()
    login = Login(name=login, host=host)
    login.save()
    logger.info("registration received for {0}@{1}".format(server,login))
    return HttpResponse("registration received for {0}@{1}".format(server,login))

def get_login(request):
    try:
        participant = Participant.objects.get(client_ip=request.META["REMOTE_ADDR"])
    except ObjectDoesNotExist:
        logins = Login.objects.filter(participant=None)
        if (not logins):
            raise Exception("There are no available logins")
        login = logins[0]
        participant = Participant(client_ip=request.META['REMOTE_ADDR'],login=login)
        participant.save()
    return render_to_response('registerapp/registered.html',
        {
            'host': participant.login.host.name            
            ,'login': participant.login.name
        }
    )
def get_available_count(request):
    logins = Login.objects.filter(participant=None)
    return HttpResponse(json.dumps({"success": True, "result": len(logins)}),status=200, content_type="application/json");    

def get_used_count(request):
    logins = Login.objects.filter(~Q(participant=None))
    return HttpResponse(json.dumps({"success": True, "result": len(logins)}),status=200, content_type="application/json");        

def list_logins(request):
    logins = Login.objects.all()
    #results = [{"login_name":i.name,"host":i.host.name,"participant":i.participant.client_ip if i.participant else None} for i in logins]
    #results = [{"login_name":i.name,"host":i.host.name} for i in logins]
    results=[]
    for i in logins:        
        try: 
            results.append( {"login_name":i.name,"host":i.host.name,"participant":i.participant.client_ip} )
        except ObjectDoesNotExist:
            results.append( {"login_name":i.name,"host":i.host.name,"participant":None} )
    return HttpResponse(json.dumps({"success": True, "results": results}),status=200, content_type="application/json");
    



