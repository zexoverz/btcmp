import re
def is_username_valid(username):
	username_pattern = re.compile("^([a-z]{8})")
	if username_pattern.match(username):
		print(True)
	else:
		print(False)

def is_password_valid(password):
	password_pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_!@#\$%\^&\*])(?=.{8})")
	if password_pattern.match(password):
		print(True)
	else:
		print(False)

is_username_valid("zeronull")
is_username_valid("useroke")
is_password_valid("qazW_123")
