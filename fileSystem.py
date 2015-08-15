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
        self.file = open(path, 'r')
        self.path = hashlib.md5(path.encode('utf-8')).hexdigest() + ".json"
        self.tags = None

    # Stages the tags file for editing and reading
    def stage(self):
        self.tags = json.load(open(self.path,'a+', encoding=('utf-8')))

    # Saves the file with specified content. Overwrites the old content wholly.
    def save(self,slug):
        # build the file content
        t3hslug = {
            'original': self.original,
            'tags': [ slug ]
        }
        # Convert the content to json
        parsedslug = json.dumps(t3hslug)
        # Write to the file
        self.tags.write(parsedslug)

    def tag(self,description,index = []):
        parsedjson = {json.load(self.tags)}
        parsedjson[index] = description
        self.save(parsedjson)