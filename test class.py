for i in range (1,4):
        add_entities([PowerSensorAuto(i)])

class PowerSensorAuto():
    def __init__(self,value):
        self._attr_name = f"Power Sensor {value}"

    def update(self) -> None:
        self._attr_native_value = get_on_off()


