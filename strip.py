import sys

def modifyLink(link):
	if sys.argv[1] != "":
		mainTag = "#" + sys.argv[1]
	else:
		mainTag = "#agile"
	location = link.find("?utm")
	if link[location-1] == "/":
		location -=1
	link = link[:location]
	newireversed = link[::-1]
	strloc = len(link) - newireversed.find("/")
	title = link[strloc:].replace("-", " ")
	title = title[0].upper() + title[1:]
	if title == "":
		nextloc = len(link) - newireversed[strloc:].find("/")
		title = link[nextloc:].replace("-", " ")
	link = "%s: %s %s\n" % (title, link, mainTag)
	return link

g = open ("targetlinks.txt", "w")
with open ("sourcelinks.txt", "r+") as f:
	links = f.readlines()
	for i in links:
		g.write(modifyLink(i))