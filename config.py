import os


class Config(object):
	SECRET_KEY = os.environ.get('s') or b'\x93\xb9\xa5\x0f(\xdc\xca\x0f\xa4^\nH\xf7s\\\xb3'

	MONGODB_SETTINGS = { 'db':'UTA_Enrollment'}


