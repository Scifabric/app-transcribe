'''Usage: python upload.py {your-api-key}
'''
import csv
import urllib
import json
import urllib2

api_key = None
pybossa_url = 'http://pybossa.com'
app_id = 75
url = 'https://docs.google.com/spreadsheet/pub?key=0Al6mO9_3Hr2PdGt4b0FzT2VGVGpzREFuMjdqVDlTcmc&output=csv'
fo = urllib.urlopen(url)

def main():
    reader = csv.DictReader(fo)
    for row in reader:
        create_task(row)

def create_task(info):
    print('Processing: %s' % info)
    print api_key
    data = dict(app_id=app_id, info=info, state=0, calibration=0, priority_0=0)
    data = json.dumps(data)
    # Setting the POST action
    request = urllib2.Request(pybossa_url + '/api/task' + '?api_key=' + api_key)
    request.add_data(data)
    request.add_header('Content-type', 'application/json')

    # Create the task
    output = json.loads(urllib2.urlopen(request).read())
    if (output['id'] != None):
        print 'Success'
        return True
    else:
        print 'Error'

if __name__ == '__main__':
    import sys
    api_key = sys.argv[1]
    main()

