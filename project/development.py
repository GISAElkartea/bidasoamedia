from project.settings import *

DEBUG=True
TEMPLATE_DEBUG=DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(DIR, 'db.sqlite'),                      
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': '',                      
        'PORT': '',                      
    }
}
