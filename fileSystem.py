__author__ = 'Jani Anttonen'
import json
import hashlib

# File system
# Works with json files as of now
class File:

    """ Specifies the file to be worked with
        Works with both new and old files (creates a new one if nonexistent)
    """
    def __init__(self, path):
        self.original = path
        self.file = open(path, 'r')
        self.path = hashlib.md5(open(path,'rb').read()).hexdigest() + ".json"
        self.tags = None

    # Stages the file for editing and reading
    def stage(self):
        self.tags = open(self.path,'a+')

    # Saves the file with specified content. Overwrites the old content wholly.
    def save(self,slug):
        self.tags.write(slug)

    def tag(self,description,index = []):
        taggable = self.file[index[0]:index[1]]
