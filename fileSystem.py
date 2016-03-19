import os

__author__ = 'Jani Anttonen'
import json
import hashlib

# File system
class File:

    """ Specifies the file to be worked with
        Works with both new and old files (creates a new one if nonexistent)
    """
    def __init__(self, path):

        # Original file (flat text)
        self.original = path
        self.file = open(path, 'r', encoding=('utf-8'))

        # Initialize tag file (JSON)
        self.path = "data/" + hashlib.md5(path.encode('utf-8')).hexdigest() + ".json"
        if not os.path.isfile(self.path):
            # Write to the file
            with open(self.path, 'w') as f:
                json.dump([], f, ensure_ascii=False, indent=2)

        # Open tag file
        self.tags = open(self.path,'r', encoding=('utf-8'))

    """ Tagging functionality.
        Gets the tag and its indeces,
        and then appends them to the tag file.
    """
    def tag(self,description,index):
        # Form the tag
        tag = {'index':index,'tag':description}

        # Load existing tags
        with open(self.path) as tagsjson:
            filecontent = json.load(tagsjson)

        # Add the new tag to the end of tags
        filecontent.append(tag)

        # Save to file
        with open(self.path, 'w') as f:
            json.dump(filecontent, f, ensure_ascii=False, indent=2, sort_keys=True)