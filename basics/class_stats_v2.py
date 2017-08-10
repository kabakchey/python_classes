
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
def reset():
    response = requests.put(URL + '/reset/')

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def demo():
    '''
    Demonstrates fetching, updating and adding new student.
    Resets remote DB afterwards
    :return: None
    '''

    # available urls
    # http://54.201.47.219:8080/api/v1/students/
    # http://54.201.47.219:8080/api/v1/students/1025
    # http://54.201.47.219:8080/api/v1/hw_results/
    # http://54.201.47.219:8080/api/v1/hw_results/1025
    # http://54.201.47.219:8080/api/v1/test1_results/
    # http://54.201.47.219:8080/api/v1/test1_results/1025
    # http://54.201.47.219:8080/api/v1/test1_weights/

    pprint(get_students())
    pprint(get_student(1024))

    update_student(1024, {'rank': 42})
    pprint(get_student(1024))

    add_student({"id":1234, "fullname":"AAAA", "email":"x@y.z", "github":"", "rank":0})
    pprint(get_student(1234))

    reset()

#------------------------------------------------------------------------------
def update_students_results():
    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    pass


#------------------------------------------------------------------------------
def print_students_info(sort_by_key="fullname"):
    '''
    Prints students info sorted according to the passed key in dictionary). By default, sort by students names.
    Student info should be presented as a card that includes the following information:
        - id,
        - name,
        - email,
        - github account (only name, not URL path)
        - rank
    Example (format is not strictly required):
        -----------------------------------------
        : ID:                               1025:
        :.......................................:
        : Full name:                Юношев Павел:
        : Email:          p.n.yunoshev@gmail.com:
        : Github:                               :
        : Rank:                               42:
        -----------------------------------------
    :return: None
    '''
    pass


#------------------------------------------------------------------------------
if __name__ == "__main__":
    #demo()

    update_students_results()
    print_students_info()
