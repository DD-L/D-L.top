import base64
def base64url(url, flag = 'encode'):
	if flag == 'encode':
		url = url.replace("://", ":##")
		url = base64.b64encode(url.encode()).decode()
		url = url.replace('+', '-').replace('/', '_')

	elif flag == 'decode':
		url = url.replace('-', '+').replace('_', '/')
		url = base64.b64decode(url.encode()).decode()
		url = url.replace(':##', '://')
		
	return url