# For more information visit:
# https://developers.nest.com/reference/api-thermostat

from api_putter import ApiPutter


class ApiThermostatPutter(ApiPutter):

    # fan_timer_active
    #
    # Indicates if the fan timer is engaged; used with fan_timer_duration
    # to turn on the fan for a (user-specified) preset duration.
    # Values: true, false
    #
    def update_fan_timer_active(self, device_id, value):
        payload = "{\"fan_timer_active\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # temperature_scale
    #
    # Fahrenheit or Celsius; used with temperature display.
    # Values: "F", "C"
    #
    def update_temperature_scale(self, device_id, value):
        payload = "{\"temperature_scale\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_f
    #
    # Desired temperature, in full degrees Fahrenheit (1 F). Used when hvac_mode = heat or cool.
    # Range: 50-90
    #
    def update_target_temperature_f(self, device_id, value):
        payload = "{\"target_temperature_f\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_c
    #
    # Desired temperature, in half degrees Celsius (0.5 C). Used when hvac_mode = heat or cool.
    # Range: 9-32
    #
    def update_target_temperature_c(self, device_id, value):
        payload = "{\"target_temperature_c\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_high_f
    #
    # Maximum target temperature, displayed in whole degrees Fahrenheit (1 F).
    # Used when hvac_mode = heat-cool (Heat Cool mode).
    #
    def update_target_temperature_high_f(self, device_id, value):
        payload = "{\"target_temperature_high_f\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_high_c
    #
    # Maximum target temperature, displayed in half degrees Celsius (0.5C).
    # Used when hvac_mode = heat-cool (Heat Cool mode).
    #
    def update_target_temperature_high_c(self, device_id, value):
        payload = "{\"target_temperature_high_c\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_low_f
    #
    # Minimum target temperature, displayed in whole degrees Fahrenheit (1 F).
    # Used when hvac_mode = heat-cool (Heat Cool mode).
    #
    def update_target_temperature_low_f(self, device_id, value):
        payload = "{\"target_temperature_low_f\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # target_temperature_low_c
    #
    # Minimum target temperature, displayed in half degrees Celsius (0.5C).
    # Used when hvac_mode = heat-cool (Heat Cool mode).
    #
    def update_target_temperature_low_c(self, device_id, value):
        payload = "{\"target_temperature_low_c\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # hvac_mode
    #
    # Indicates HVAC system heating/cooling modes, like Heat, Cool
    # for systems with heating and cooling capacity, or Eco Temperatures for energy savings.
    #
    # hvac_mode can be changed if the Thermostat is locked
    # target_temperature_f and target_temperature_c cannot be changed if hvac_mode = off or eco
    # Values: "heat", "cool", "heat-cool", "eco", "off"
    #
    def update_hvac_mode(self, device_id, value):
        payload = "{\"hvac_mode\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # label
    #
    # Thermostat custom label. Appears in parentheses, after the where name.
    # Examples: "Upstairs", "Guest room", "Playroom"
    #
    def update_label(self, device_id, value):
        payload = "{\"label\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)

    # fan_timer_duration
    #
    # Specifies the length of time (in minutes) that the fan is set to run.
    #
    # The fan_timer_active setting turns on the fan.
    # The fan_timer_timeout value indicates the timestamp when fan_timer_duration is set to end.
    # Values: 15, 30, 45, 60, 120, 240, 480, 720
    #
    def update_fan_timer_duration(self, device_id, value):
        payload = "{\"fan_timer_duration\": \"%s\"}" % value
        self.poster('thermostats', device_id, payload)