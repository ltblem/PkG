# ColoursAPY - A LetThereBeLemons Python API
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
Colours_APY_Version = 2

foreground = {
	"reset" : "\x1b[0m",
	"default" : "\x1b[39m",
	"black" : "\x1b[30m",
	"red" : "\x1b[31m",
	"green" : "\x1b[32m",
	"yellow" : "\x1b[33m",
	"blue" : "\x1b[34m",
	"magenta" : "\x1b[35m",
	"cyan" : "\x1b[36m",
	"white" : "\x1b[37m",
	"bright_black" : "\x1b[90m",
	"bright_red" : "\x1b[91m",
	"bright_green" : "\x1b[92m",
	"bright_yellow" : "\x1b[93m",
	"bright_blue" : "\x1b[94m",
	"bright_magenta" : "\x1b[95m",
	"bright_cyan" : "\x1b[96m",
	"bright_white" : "\x1b[97m"
}

background = {
	"reset" : "\x1b[0m",
	"default" : "\x1b[49m",
	"black" : "\x1b[40m",
	"red" : "\x1b[41m",
	"green" : "\x1b[42m",
	"yellow" : "\x1b[43m",
	"blue" : "\x1b[44m",
	"magenta" : "\x1b[45m",
	"cyan" : "\x1b[46m",
	"white" : "\x1b[47m",
	"bright_black" : "\x1b[100m",
	"bright_red" : "\x1b[101m",
	"bright_green" : "\x1b[102m",
	"bright_yellow" : "\x1b[103m",
	"bright_blue" : "\x1b[104m",
	"bright_magenta" : "\x1b[105m",
	"bright_cyan" : "\x1b[106m",
	"bright_white" : "\x1b[107m"
}

styles = {
	"reset" : "\x1b[0m",
	"bold" : "\x1b[1m",
	"dim" : "\x1b[2m",
	"italic" : "\x1b[3m",
	"underline" : "\x1b[4m",
	"blink" : "\x1b[5m",
	"reverse" : "\x1b[7m",
	"hidden" : "\x1b[8m",
	"strikethrough" : "\x1b[9m"
}



def get_fg(colour):
	return foreground[colour]

def get_bg(colour):
	return background[colour]

def get_style(style):
	return styles[style]




if __name__ == "__main__":
	print("These python files are for importing into your own applications using the `import` command.")
	raise Exception ("This file is not meant to be run directly.")