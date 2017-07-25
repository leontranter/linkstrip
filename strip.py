import argparse

def modifyLink(link, mainTag):
	# ignore the utm and/or trailing slash
	location = link.find("?utm")
	if link[location-1] == "/":
		location -=1
	# find the actual url
	link = link[:location]
	# find the last slash in the url - the article title is the resource i.e. what comes after that
	newireversed = link[::-1]
	titleLocation = len(link) - newireversed.find("/")
	# strip hyphens and underscores
	title = link[titleLocation:].replace("-", " ").replace("_", " ")
	title = title[0].upper() + title[1:]
	if title == "":
		nextloc = len(link) - newireversed[titleLocation:].find("/")
		title = link[nextloc:].replace("-", " ")
	# construct and return the whole thing
	link = "%s: %s %s\n" % (title, link, mainTag)
	return link

def getTag():
	parser = argparse.ArgumentParser(description="specify some options such as hashtag")
	parser.add_argument("--hashtag", help="pass in a hashtag", default="agile")
	args = parser.parse_args()
	return "#" + args.hashtag

def main():
	mainTag = getTag()
	with open ("sourcelinks.txt", "r+") as f, ("targetlinks.txt", "w") as g:
		links = f.readlines()
		for i in links:
			g.write(modifyLink(i, mainTag))

if __name__ == "__main__":
	main()