def modifyLink(link):
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
	link = "%s: %s %s\n" % (title, link, "#agile")
	return link

g = open ("targetlinks.txt", "w")
with open ("sourcelinks2.txt", "r+") as f:
	links = f.readlines()
	for i in links:
		g.write(modifyLink(i))
