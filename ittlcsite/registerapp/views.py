import logging
from registerapp.models import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

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

def getlogin(request):
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
