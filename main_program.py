from api_getter import ApiGetter
from api_thermostat_putter import ApiThermostatPutter
import time
import json
from token_generator import TokenHelper

# SETTINGS:
#
# TokenHelper() # Use only for prod or when the token is expired,
# Token Helper will create a token for Nest API calls
#
GET = ApiGetter()
PUT = ApiThermostatPutter()
motion = (json.loads(open('nest_config.json').read()))['motion']
exit_code = 0
buffer = []
sensor_location = str(GET.get_thermostat_only().where)
device_id = str(GET.get_thermostat_only().device_id)

#
# Just faking movement report
#
def bool_convertor(what):
    if what == 'False':
        return False
    elif what == 'True':
        return True
    else:
        print("Wrong string value")

while exit_code == 0:
    if str(GET.get_thermostat_only().where) != 'Living Room':
        if bool_convertor((json.loads(open('nest_config.json').read()))['motion']) is False:
            print("Warning: Currently active room is empty but Nest pointed to it! Action required...")
        else:
            print("No Events")
    time.sleep(5)