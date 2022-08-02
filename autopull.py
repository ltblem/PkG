import os, colours

green = colours.get_fg("green")
greenbold = colours.get_fg("green") + colours.get_style("bold")
creset = colours.get_style("reset")
red = colours.get_fg("red")

def getDirs():

	dirs = os.listdir("/home/jamsii/fiddly/")

	doit = 1

	while doit == 1:
		doit = 0
		try:
			for item in range(0, len(dirs)):
				if os.path.isfile("/home/jamsii/fiddly/" + dirs[item]):
					dirs.pop(item)
		except IndexError:
			doit = 1

	return dirs

def pull(dirs):

	count = 0
	for proj in dirs:
		count += 1
		print(greenbold + str(count) + ":", proj + creset)
		if os.path.isdir("/home/jamsii/fiddly/" + proj + "/.git"):
			os.system("cd /home/jamsii/fiddly/" + proj + " && git pull")
			print(green + proj, "updated, moving on" + creset)
		else:
			print(red + proj, "is not a repo, skipping" + creset)