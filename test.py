__author__ = 'Jani'
import fileSystem

file = fileSystem.File('asd.txt')
file.tag("räpingsingsasfsaffsafsdgf",[5,4])
print(file.get_tags_by_index([5,4]))
