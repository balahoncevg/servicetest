import uuid
import requests
from django.db import models
import time
import asyncio

# Create your models here.

class Mailing(models.Model): #модель рассылки
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    dateofstart = models.DateField(null=False)
    dateofstop = models.DateField(null=False)
    def __str__(self):
        return self.name

class Takingone(models.Model): #модель клиента
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    numberofone = models.IntegerField()
    operatoscode = models.IntegerField()
    sometag = models.CharField(max_length=200)
    timezoneofone = models.IntegerField(help_text='Введите часоваой пояс в формате +/-число')
    def __str__(self):
        return str(self.numberofone)

class Wordsofmail(models.Model): #модель сообщения
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timetogo = models.TimeField(null=True)
    themailing = models.ManyToManyField('Mailing')
    #idofmailing = themailing.id
    #theone = models.ManyToManyField('Takingone')
    #idofone = theone.id
    number = models.ManyToManyField('Takingone')
    #timetosend = theone.timezoneofone
    spam = True
    #async def timewait(self):
    #    if self.timetosend == 0:
    #        pass
    #    elif self.timetosend < 0:
    #        aaa = self.timetosend * 3600
    #        await asyncio.sleep(86400 - aaa)
    #    else:
    #        await asyncio.sleep(self.timetosend * 36000)
    while spam:
        def send_sms(self):
            r = requests.post('https://probe.fbrq.cloud/v1/send/{}'.format(str(id)), data={'phone': number})
            return r
        #time.sleep(86400)

    def __str__(self):
        return self.id