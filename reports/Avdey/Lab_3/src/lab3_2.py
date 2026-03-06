from abc import ABC, abstractmethod


class DigitalClock(ABC):
    @abstractmethod
    def get_time(self) -> str:
        pass


class AnalogClock:
    def __init__(self, hour_angle: float, minute_angle: float):
        self._hour_angle = hour_angle % 720
        self._minute_angle = minute_angle % 360

    @property
    def hour_angle(self) -> float:
        return self._hour_angle

    @property
    def minute_angle(self) -> float:
        return self._minute_angle


class ClockAdapter(DigitalClock):
    def __init__(self, analog_clock: AnalogClock):
        self.analog_clock = analog_clock

    def get_time(self) -> str:
        ha = self.analog_clock.hour_angle
        ma = self.analog_clock.minute_angle

        minutes = int(ma / 6)
        hours = int(ha / 30)

        hours = hours % 24
        minutes = min(minutes, 59)

        return f"{hours:02d}:{minutes:02d}"


if __name__ == "__main__":
    input_hour_angle = float(input("Введите угол часовой стрелки: "))
    input_minute_angle = float(input("Введите угол минутной стрелки: "))

    analog = AnalogClock(input_hour_angle, input_minute_angle)
    digital_clock = ClockAdapter(analog)

    print("Текущее время:", digital_clock.get_time())
