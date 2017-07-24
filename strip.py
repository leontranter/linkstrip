import argparse

def modifyLink(link, mainTag):
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

parser = argparse.ArgumentParser(description="specify some options such as hashtag")
parser.add_argument("--hashtag", help="pass in a hashtag", default="agile")
args = parser.parse_args()
mainTag = "#" + args.hashtag

g
with open ("sourcelinks.txt", "r+") as f, ("targetlinks.txt", "w") as g:
	links = f.readlines()
	for i in links:
		g.write(modifyLink(i, mainTag))
