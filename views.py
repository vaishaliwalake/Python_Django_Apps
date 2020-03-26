#import image
from email.mime import image
import mimetypes
from wsgiref.util import FileWrapper

from django.shortcuts import render,redirect
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse

from PIL import Image
from io import BytesIO

import requests


def http_response_plain_text(request):
    return HttpResponse("Plain Text Response", content_type="text/plain")

def http_response_xml_text(request):
    response = """<?xml version="1.0" encoding="UTF-8"?>
                  <data>
                      <topic>Python Django</topic>
                      <heading>Response Types</heading>
                  </data>"""

    return HttpResponse(response, content_type="text/xml")

def http_response_html(request):

    html_text = """<h1>HTML Response </h1>
                <p style="background-color:red; color:white;">HTML Response Output</p>"""

    return HttpResponse(html_text)

def json_response(request):
    return JsonResponse({'data':'tinitiate'})


def file_response(request,):
    response = HttpResponse (request, content_type='image/png')
    url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'
    r = requests.get(url)
    img = Image.open(BytesIO (r.content))
   # response = FileResponse(img)
    #response['Content-Disposition'] = "attachment; filename=%s" % img.svg
   # response.items(r)
    #r.save(response)

    return HttpResponse (r, content_type='image/png')



######################################################################
## STREAMING EXAMPLE
## This will download a file with 1 to 100 each number on a new line
######################################################################
def generator():
    for x in range(100):
        yield str(x) + "\n"

def streaming_http_response(queryset):
    response = StreamingHttpResponse( streaming_content=generator(),content_type='text/plain')

    response['Content-Disposition'] = 'attachment;filename=data.txt'
    return response