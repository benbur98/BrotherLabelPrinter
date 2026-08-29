import time
from dataclasses import dataclass

from servo_motor_control.motor import Motor


@dataclass(frozen=True)
class MotorPowerButtonControl:
    initial_position: int = 50
    final_position: int = 25

    @classmethod
    def get(cls, initial_position: int | None, final_position: int | None) -> "MotorPowerButtonControl | None":
        if initial_position is None or final_position is None:
            return None
        return cls(initial_position, final_position)


def toggle_power_button(motor_control: MotorPowerButtonControl) -> None:
    """Toggles the Power Button of the Printer by moving the Motor to the Pressed Position and then back to the Initial"""
    if not Motor.is_supported():
        return

    motor = Motor()
    motor.set_position_percentage(motor_control.initial_position)
    motor.enable_pwm()
    time.sleep(2)
    motor.set_position_percentage(motor_control.final_position)
    time.sleep(2)
    motor.set_position_percentage(motor_control.initial_position)
    time.sleep(2)
    motor.disable_pwm()
