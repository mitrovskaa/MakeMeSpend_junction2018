'''
    Google implementation of taking keywords
    from text. Used for extracting labels 
    from reviews.
'''

import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six
from google.cloud.language import enums
from google.cloud.language import types

def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities


    return entities