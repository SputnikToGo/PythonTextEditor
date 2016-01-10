__author__ = 'Jani Anttonen'
import json
import hashlib
import tempfile

# File system
# Works with json files as of now
class File:

    """ Specifies the file to be worked with
        Works with both new and old files (creates a new one if nonexistent)
    """
    def __init__(self, path):
        self.original = path
        self.file = open(path, 'r', encoding=('utf-8'))
        self.path = hashlib.md5(path.encode('utf-8')).hexdigest() + ".json"
        self.tags = open(self.path,'a+', encoding=('utf-8'))

    # Saves the file with specified content. Overwrites the old content wholly.
    def save(self,slug):
        # build the file content
        content = {
            'original': self.original,
            'tags': { slug }
        }
        # Write to the file
        json.dump(content, self.tags, indent=2)

    def tag(self,description,index = []):
        with open(self.path) as json_file:
            parsedjson = json.load(json_file)

        # Form the tag
        tag = {'index': index, 'description': description}

        # Write to the file
        json.dump(tag, parsedjson["tags"], indent=2)