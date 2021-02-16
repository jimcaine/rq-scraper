import requests
from fake_headers import Headers
from xml.etree import ElementTree

def get_page(uri):
    """
    Reads a webpage given the URI.
    """

    # make request for uri
    HeadersGenerator = Headers(os='mac', headers=False)
    response = requests.get(uri, headers=HeadersGenerator.generate())

    # check status code
    status_code = response.status_code
    if status_code != 200:
        print(status_code)

    # get and return content as bytes
    content = response.content
    return content
