__author__ = 'Jani'
import fileSystem

file = fileSystem.File('asd.txt')
file.tag("räpingsingsings",[0,4])
print(file.get_tags_by_index([0,4]))
