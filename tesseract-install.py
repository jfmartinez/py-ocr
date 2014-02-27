
"For Mac OSX, easiest installation path is using Mac Ports"

from subprocess import call
install_tess_error = call(["sudo", "port", "install", "tesseract"])
if install_tess_error == 1:
	print "Try it"

lang_code = raw_input('Enter the language code for the installation. (Ex: eng - English): ')
install_lang = call(["sudo", "port", "install", 'tesseract-' + lang_code])