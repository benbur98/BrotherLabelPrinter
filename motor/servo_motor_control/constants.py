from enum import Enum

PWM_PATH = "/sys/class/pwm/pwmchip0"


PWM_PERIOD = 20000000  # 20ms = 50 Hz


class MotorPosition(Enum):
    LEFT = 1000000  # 1ms Pulse
    CENTER = 1500000  # 1.5ms Pulse
    RIGHT = 2000000  # 2ms Pulse

    @staticmethod
    def percentage(percentage: int) -> int:
        """Get the Fractional Value of the Position Between Full Left to Full Right"""
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")
        fraction = percentage / 100

        duty_cycle_range = MotorPosition.RIGHT.value - MotorPosition.LEFT.value
        position_value = MotorPosition.LEFT.value + (duty_cycle_range * fraction)
        return int(position_value)
