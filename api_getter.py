import nest
from token_generator import TokenHelper


class ApiGetter:

    def __init__(self):
        access_token_cache_file = 'token.json'
        self.nest_api = nest.Nest(client_id=TokenHelper(bypass_aoth = 1).CLIENT_ID, client_secret=TokenHelper.CLIENT_SECRET, access_token_cache_file=access_token_cache_file)
        #
        #     Basic Usage::
        #       >>> import requests
        #       >>> s = requests.Session()
        #       >>> s.get('https://httpbin.org/get')
        #       <Response [200]>
        #
        self.session = self.nest_api._session
        print("Token ready and saved in token.json")

    def get_all_structure(self):
        for structure in self.nest_api.structures:
            print ('\nStructure name: %s' % structure.name)
            print ('    Away: %s' % structure.away)
            print ('    Security State: %s' % structure.security_state)
            print ('    Devices:')
            for device in structure.thermostats:
                print ('        Device: %s' % device.name)
                print ('        Temp: %0.1f' % device.temperature)
        return self.nest_api.structures

    def get_all_thermostat(self):
        for structure in self.nest_api.structures:
            print ('\nStructure name: %s' % structure.name)
            for device in structure.thermostats:
                print ('        Device: %s' % device.name_long)
                print ('        Device ID: %s' % device.device_id)
                print ('        Temp: %0.1f' % device.temperature)
                print ('        Online: %s' % device.online)
                print ('        Serial number: %s' % device.serial)
                print ('        Max Temp: %0.1f' % device.max_temperature)
                print ('        Min Temp: %0.1f' % device.min_temperature)
                print ('        Can Cool: %s' % device.can_cool)
                print ('        Can Heat: %s' % device.can_heat)
                print ('        Has Fan: %s' % device.has_fan)
                print ('        Fan: %s' % device.fan)
                print ('        Fan Timer: %s' % device.fan_timer)
                print ('        Humidity: %i' % device.humidity)
                print ('        Mode: %s' % device.mode)
                print ('        Temperature Scale: %s' % device.temperature_scale)
                print ('        Where Name: %s' % device.where)
        return self.nest_api.structures

    def get_thermostat_only(self):
        # needs to be updated in case of several structures or thermostats
        return self.nest_api.structures[0].thermostats[0]

# ApiGetter().get_all_thermostat()
