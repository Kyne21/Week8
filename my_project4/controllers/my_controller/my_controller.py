from controller import Robot

def control_robot(bot):
    time_interval = 64  # Time step lebih besar untuk memperlambat
    max_velocity = 3.14  # Kecepatan maksimum lebih rendah untuk gerakan lebih lambat

    # Motors
    left_wheel = bot.getMotor('left wheel motor')
    right_wheel = bot.getMotor('right wheel motor')
    left_wheel.setPosition(float('inf'))
    right_wheel.setPosition(float('inf'))
    left_wheel.setVelocity(0.0)
    right_wheel.setVelocity(0.0)

    # Enable IR sensors
    left_sensor = bot.getDistanceSensor('ir0')
    left_sensor.enable(time_interval)
    right_sensor = bot.getDistanceSensor('ir1')
    right_sensor.enable(time_interval)

    # Step simulation
    while bot.step(time_interval) != -1:
        # Read IR sensors
        left_sensor_value = left_sensor.getValue()
        right_sensor_value = right_sensor.getValue()

        print("Left sensor: {} Right sensor: {}".format(left_sensor_value, right_sensor_value))

        left_velocity = max_velocity
        right_velocity = max_velocity

        # Adjust speeds based on sensor readings
        if (left_sensor_value > right_sensor_value) and (6 < left_sensor_value < 15):
            print("Turn left")
            left_velocity = -max_velocity
        elif (right_sensor_value > left_sensor_value) and (6 < right_sensor_value < 15):
            print("Turn right")
            right_velocity = -max_velocity

        left_wheel.setVelocity(left_velocity)
        right_wheel.setVelocity(right_velocity)

if __name__ == "__main__":
    my_bot = Robot()
    control_robot(my_bot)
