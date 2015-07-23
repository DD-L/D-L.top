#### <function> ######
import re
import base64
def parse_url(path_info):
	try:
		if re.match(r"^/svencryptapi/token/.+", path_info):
			is_encrypt = True
		else:
			is_encrypt = False

		regex = r"^/sv(encrypt)?api/token(/[^/]+)/url(/[^/]+)"
		args = re.findall(regex, path_info)
		token = args[0][1].lstrip('/')
		b64url = args[0][2].lstrip('/')
		
		return_code = True
		if token == '' or token == None:
			return_code = False
		if b64url == '' or b64url == None:
			return_code = False

		return is_encrypt, token, b64url, return_code
	except Exception as e:
		return False, '', '', False

def decode_base64url(base64url):
	try:
		url = base64url.replace('-', '+').replace('_', '/')
		url = base64.b64decode(url).decode()
		url = url.replace(":##", "://")
		return_code = True
	except Exception as e:
		url = ''
		return_code = False
	return url, return_code

#def get_api(url, cdata = True):
#	from yg_api import toxml
#	return toxml(url, cdata)

def api_respone_encrypt(xml):
	return base64.b64encode(xml.encode()).decode()

#### </function> ######
