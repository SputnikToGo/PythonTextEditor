# Python Tagging Text Editor
A text editor meant for tagging existing text.

## Getting it to run
### Requirements:
- Python 3

Example on a Mac, using python3 as alias for python version 3.5:
```bash
python3 TextEditor.py
```

### Workflow
By now you should have an empty editor window open with a basic file menu (Embedded in Windows, in the menu bar in Unity or OS X GUI).

Steps:
1.  Open up a flat text file you want to tag.
2.  Select text within the editor.
3.  Press <Mouse 2> or <Mouse 3> to open the tag editor.
4.  Write a tag and submit it.
5.  Voila! Now you should have a highlighted area in the text telling you that the substring has a tag attached to it.

Existing tags are automatically loaded to the editor. The editor uses a JSON file in the "data" subdirectory with a name that's a hashed file path of the original file for this functionality.
