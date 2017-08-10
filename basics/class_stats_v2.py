import requests
import json
from pprint import pprint

#------------------------------------------------------------------------------
BASE_URL = "http://54.201.47.219:8080/api"
VERSION  = "v1"
URL = "%s/%s" % (BASE_URL, VERSION)


#------------------------------------------------------------------------------
def log_error(msg):
    print("ERROR: ", msg)

#------------------------------------------------------------------------------
def get_students():
    response = requests.get(URL + '/students')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['students']
    else:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
def get_student(id):
    response = requests.get(URL + '/students/' + str(id))
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result  = json_object['student']
    else:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def update_student(id, upd_fields):
    response = requests.put(URL + '/students/' + str(id),
                            json=json.dumps(upd_fields))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def add_student(student):
    response = requests.post(URL + '/students/',
                            json=json.dumps(student))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


#------------------------------------------------------------------------------
if __name__ == "__main__":
    pprint(get_students())
    pprint(get_student(1024))

    update_student(1024, {'rank': 43})
    pprint(get_student(1024))

    add_student({"id":1234, "fullname":"AAA", "email":"", "github":"", "rank":0})
    pprint(get_student(1234))


	# available urls
	# http://54.201.47.219:8080/api/v1/students/
	# http://54.201.47.219:8080/api/v1/students/1025
	# http://54.201.47.219:8080/api/v1/hw_results/
	# http://54.201.47.219:8080/api/v1/hw_results/1025
	# http://54.201.47.219:8080/api/v1/test1_results/
	# http://54.201.47.219:8080/api/v1/test1_results/1025
	# http://54.201.47.219:8080/api/v1/test1_weights/
