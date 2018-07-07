try:
    #from django.conf.urls import patterns, url, include
    from django.urls import path, include, re_path
except ImportError: # django 1.3
    from django.conf.urls.defaults import patterns, url, include
