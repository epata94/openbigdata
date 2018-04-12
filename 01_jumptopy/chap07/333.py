from xml.etree.ElementTree import parse

tree = parse("note2.xml")
note = tree.getroot()

# childs = note.getchildren()
# for child in note.iter():
#     print(child.attrib)

# for child in note.iter("from"):
#     print(child.attrib)
#
from_tag = note.find("from")
for student in from_tag.iter():
    print(student.attrib)
# childs = note.getiterator("from")
# childs = note.getchildren()
print("end")