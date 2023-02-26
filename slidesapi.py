from google.oauth2 import service_account
from googleapiclient.discovery import build

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import uuid

from slidesoauth import doOauthSlides 

SCOPES = ['https://www.googleapis.com/auth/presentations']

#PRESENTATION_ID = '1EW8JearggoLRPXN6qiPvHPujHsrVANaHTgPBlgf2cmE'


# service = doOauthSlides()

def execute_response(body,service,presentation_id):
    response = service.presentations() \
        .batchUpdate(presentationId=presentation_id, body=body).execute()
    print(response)

  

def create_TitleBody_slide(title,bodycontent,service,presentation_id):
    slideobjectid=str(uuid.uuid4())
    titleobjectid = str(uuid.uuid4())
    bodyobjectid = str(uuid.uuid4())




    requests = [
    {
        "createSlide": {
        "objectId": slideobjectid ,
        "slideLayoutReference": {
            "predefinedLayout": "TITLE_AND_BODY"
        },
        "placeholderIdMappings": [
            {
            "layoutPlaceholder": {
                "type": "TITLE",
                "index": 0
            },
            "objectId": titleobjectid ,
            },
            {
            "layoutPlaceholder": {
                "type": "BODY",
                "index": 0
            },
            "objectId": bodyobjectid,
            }
        ],
        }
    },
    {
        "insertText": {
        "objectId": titleobjectid,
        "text": f"{title}",
        }
    },
    {
        "insertText": {
        "objectId": bodyobjectid,
        "text": f"{bodycontent}",
        }
    }
    ]
    body = {
        'requests': requests
    }
    execute_response(body,service,presentation_id)

def create_image_slide(title,bodycontent,url,service,presentation_id):
    slideobjectid=str(uuid.uuid4())
    titleobjectid = str(uuid.uuid4())
    bodyobjectid = str(uuid.uuid4())
    bodyobjectid2 = str(uuid.uuid4())
    print(bodyobjectid)
    print(bodyobjectid2)




    requests = [
    {
        "createSlide": {
        "objectId": slideobjectid ,
        "slideLayoutReference": {
            "predefinedLayout": "TITLE_AND_TWO_COLUMNS"
        },
        "placeholderIdMappings": [
            {
            "layoutPlaceholder": {
                "type": "TITLE",
                "index": 0
            },
            "objectId": titleobjectid ,
            },
            {
            "layoutPlaceholder": {
                "type": "BODY",
                "index": 0
            },
            "objectId": bodyobjectid,
            },
            {
            "layoutPlaceholder": {
                "type": "BODY",
                "index": 1
            },
            "objectId": bodyobjectid2,
            },
        ],
        }
    },
    {
        "insertText": {
        "objectId": titleobjectid,
        "text": f"{title}",
        }
    },
    {
        "insertText": {
        "objectId": bodyobjectid,
        "text": f"{bodycontent}",
        }
    },
    {
      "createImage": {
        "url": f"{url}",
        "elementProperties": {
          "pageObjectId": slideobjectid,

          "size": {
            "width": {
              "magnitude": 5000,
              "unit": "EMU"
            },
            "height": {
              "magnitude": 7500
              ,
              "unit": "EMU"
            }
          },
          "transform": {'scaleX': 608.905, 'scaleY': 423.22, 'translateX': 5254575.9675, 'translateY': 1506450, 'unit': 'EMU'}
        }
      }
    }
    ]
    body = {
        'requests': requests
    }
    execute_response(body,service,presentation_id)