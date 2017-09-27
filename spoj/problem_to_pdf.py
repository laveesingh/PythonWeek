import requests

import pdfkit  # Needs pip install, Depends on wkhtmltopdf

def convert(instance):
    fname = "%s: %s.pdf" % (instance.id, instance.name)
    dirname = "archive"
    pdfkit.from_url(instance.link, dirname + '/' + fname)

