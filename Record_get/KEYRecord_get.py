import httplib
import json

BASE_URL = 'api2.dynect.net'
api = '/REST/KEYRecord'

def KEYRecord_get(zone, fqdn, rec_id, token):
    conn = httplib.HTTPSConnection(BASE_URL)
    conn.request('GET', api + '/' + zone + '/' + fqdn + '/' + str(rec_id), '', headers = {'Content-type': 'application/json', 'Auth-Token': token})

    res = conn.getresponse()
    result = json.loads(res.read())

    if result['status'] == 'success':
        if rec_id == '':
	    return result['data']
	#Print the record's info for user
	print fqdn, '-', result['data']['record_type'], '-', result['data']['rdata']['algorithm'], result['data']['rdata']['flags'], result['data']['rdata']['protocol'], result['data']['rdata']['public_key']
	return result['data']['record_type'], result['data']['record_id']
    else:
        return 0
