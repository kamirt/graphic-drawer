from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from rest_framework import viewsets

from . forms import UploadFileForm
from . models import Upload
from . serializers import UploadSerializer

import os.path
import xlrd



BASE = os.path.dirname(os.path.abspath(__file__))




def handle_uploaded_file(f):
    destination = open(os.path.join(BASE + '/files/' + "file.xls"), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    rb = xlrd.open_workbook(BASE + '/files/file.xls')
    sheet = rb.sheet_by_index(0)
    xlist = []
    ylist = []
    for x in range(sheet.nrows):
        xvalue = (sheet.cell(x,0).value)
        yvalue = (sheet.cell(x,1).value)
        xlist.append(str(xvalue))
        ylist.append(str(yvalue))

    newUp = Upload(x = ",".join(xlist), y = ",".join(ylist))
    newUp.save()



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/xlsloader')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def readfile(request):
    return HttpResponseRedirect('/xlsloader')





class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
