import logging
from registerapp.models import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.template import RequestContext
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
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('registerapp/login.html', {
                'error' : error,
                'form' : form,
        }
        ,context_instance=RequestContext(request))    
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = request.POST['idsid']                        
            if name is not None:            
                # Redirect to a success page.
                try:
                    #participant = Participant.objects.get(client_ip=request.META["REMOTE_ADDR"])
                    participant = Participant.objects.get(name=request.REQUEST["idsid"])
                except ObjectDoesNotExist:
                    logins = Login.objects.filter(participant=None)
                    if (not logins):
                        raise Exception("There are no available logins")
                    login = logins[0]
                    participant = Participant(name=request.REQUEST["idsid"],
                        client_ip=request.META['REMOTE_ADDR']
                        ,login=login)
                    participant.save()
                return render_to_response('registerapp/registered.html',
                    {
                        'login': participant.name
                        ,'host': participant.login.host.name            
                        ,'login': participant.login.name
                    }
                )                                
            else:
                 # Return an 'invalid login' error message.
                error = u'invalid login'
                return errorHandle(error)
        else:
            error = u'form is invalid'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form        
        return render_to_response('registerapp/login.html', {
            'form': form,
        }
        ,context_instance=RequestContext(request))

#def get_login(request):
#    try:
#        participant = Participant.objects.get(client_ip=request.META["REMOTE_ADDR"])
#    except ObjectDoesNotExist:
#        logins = Login.objects.filter(participant=None)
#        if (not logins):
#            raise Exception("There are no available logins")
#        login = logins[0]
#        participant = Participant(client_ip=request.META['REMOTE_ADDR'],login=login)
#        participant.save()
#    return render_to_response('registerapp/registered.html',
#        {
#            'host': participant.login.host.name            
#            ,'login': participant.login.name
#        }
#    )

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
    



