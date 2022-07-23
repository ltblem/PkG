#!/bin/python3

# PkG - A LetThereBeLemons creation
# It's basically just a yay alias
# Liscensed under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)

import sys, os, autopull, colours, killer
from sys import argv as args

manpage = """PkG - LetThereBeLemons' Package Manager
Usage:
	pkg [command] [options]
Options:
	help | h : print this help page
	update | u : update package lists and upgrade packages
	install | i : install a package
	remove | r : remove a package
	query | q: list all packages on the system
	diskusage | du: unmount the external drive, open ncdu, then remount it
	cleardiskcache | cd: clears /home/jamsii/.cache
	clearmemcache | cm: clears cahced memory
	gitpull | gp: runs a git pull on all fiddly/ repositories
	main | m: does a load of useful stuff (update, cleardiskcache, clearmemcache, gitpull)
	kill | k: kills a process
"""


try:


	if args[1] == "help" or args[1] == "h":
		print(manpage)

	elif args[1] == "install" or args[1] == "i":
		os.system("yay -S " + args[2])

	elif args[1] == "update" or args[1] == "u":
		os.system("yay -Syyu --noconfirm")

	elif args[1] == "remove" or args[1] == "r":
		os.system("yay -R " + args[2])

	elif args[1] == "query" or args[1] == "q":
		os.system("yay -Q")

	elif args[1] == "diskusage" or args[1] == "du":
		os.system("sudo umount /dev/sdb1 && sudo ncdu / ; sudo mount /dev/sdb1 /home/jamsii/data")

	elif args[1] == "cleardiskcache" or args[1] == "cd":
		os.system("rm -rf /home/jamsii/.cache && mkdir /home/jamsii/.cache && echo 'Success.'")

	elif args[1] == "clearmemcache" or args[1] == "cm":
		os.system("sudo sh -c 'echo 3 >  /proc/sys/vm/drop_caches'")

	elif args[1] == "gitpull" or args[1] == "gp":
		autopull.pull(autopull.getDirs())

	elif args[1] == "main" or args[1] == "m":
		# Update packages
		print(colours.get_fg("blue") + colours.get_style("bold") + colours.get_style("underline") + "Updating packages... (1/4)" + colours.get_style("reset"))
		os.system("yay -Syyu --noconfirm")
		# Clear disk cache
		print(colours.get_fg("blue") + colours.get_style("bold") + colours.get_style("underline") + "Clearing disk cache... (2/4)" + colours.get_style("reset"))
		os.system("rm -rf /home/jamsii/.cache && mkdir /home/jamsii/.cache && echo 'Success.'")
		# Clear memory cache
		print(colours.get_fg("blue") + colours.get_style("bold") + colours.get_style("underline") + "Clearing memory cache... (3/4)" + colours.get_style("reset"))
		os.system("sudo sh -c 'echo 3 >  /proc/sys/vm/drop_caches'")
		# Pull all fiddly repositories
		print(colours.get_fg("blue") + colours.get_style("bold") + colours.get_style("underline") + "Pulling all fiddly repositories... (4/4)" + colours.get_style("reset"))
		autopull.pull(autopull.getDirs())
		# Print success message
		print(colours.get_fg("blue") + colours.get_style("bold") + colours.get_style("underline") + "Finished." + colours.get_style("reset"))
  
	elif args[1] == "kill" or args[1] == "k":
		killer.kill(args[2])
		print("Killed " + args[2])

	else:
		print("Invalid arguments given.\nUse `pkg help` for help.")
		sys.exit(1)


except IndexError:
	print("Invalid arguments given.\nUse `pkg help` for help.")
	sys.exit(0)