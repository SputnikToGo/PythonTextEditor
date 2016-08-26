__author__ = 'Jani'
import fileSystem

file = fileSystem.File('ebinsings.txt')
file.tag("raps",[5,4])
file.tag("rapsings",[5,4])
file.remove_tag("raps",[5,4])
print(file.get_tags_by_index([5,4]))
