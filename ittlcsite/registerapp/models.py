from django.db import models
from django.contrib import admin

class Host(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True,unique=True)
    def __unicode__(self):
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=120,unique=True)
    host = models.ForeignKey(Host)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name

class Participant(models.Model):
    client_ip = models.CharField(max_length=60, unique=True)
    login = models.OneToOneField(Login)
    created = models.DateTimeField(auto_now_add=True)    

    class Meta:
        unique_together = ('login','client_ip')

class HostAdmin(admin.ModelAdmin):
    search_fields=["name"]
    list_display = ["name"]
admin.site.register(Host,HostAdmin)

class LoginAdmin(admin.ModelAdmin):
    search_fields=["name"]
    list_display = ["name","host"]
admin.site.register(Login,LoginAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["client_ip","login"]
    search_fields=["client_ip"]
admin.site.register(Participant,ParticipantAdmin)

