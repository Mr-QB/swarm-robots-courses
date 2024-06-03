from controller import Robot
import numpy as np

class RunRobot:
    def __init__(self, robot):
        self.robot = robot
        self.TIMESTEP = 32
        self.MAX_SPEED = 6.28
        self.setup_motors()
        self.base_velocity = [(5, 5)]
        self.scale_matrix = [[-0.2, 0.2], [-0.1, 0.1], [-0.05, 0.05], [-0.05, 0.05], [0.05, -0.05], [0.05, -0.05], [0.1, -0.1], [0.2, -0.2]]
        self.setup_sensors()

    def setup_motors(self):
        self.left_motor = self.robot.getDevice('left wheel motor')
        self.right_motor = self.robot.getDevice('right wheel motor')
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))

    def setup_sensors(self):
        self.ir_list = [self.robot.getDevice('ps' + str(i)) for i in range(8)]
        for ir_sensor in self.ir_list:
            ir_sensor.enable(self.TIMESTEP)

    def run(self):
        while self.robot.step(self.TIMESTEP) != -1:
            sensor_values = np.array([ir_sensor.getValue() for ir_sensor in self.ir_list]).reshape(1, -1)
            sensor_values = np.clip(sensor_values, None, 140)
            motor_velocities = np.dot(sensor_values, self.scale_matrix) + self.base_velocity
            motor_velocities = np.clip(motor_velocities, -self.MAX_SPEED, self.MAX_SPEED)
            self.left_motor.setVelocity(motor_velocities[0, 0])
            self.right_motor.setVelocity(motor_velocities[0, 1])

if __name__ == "__main__":
    robot = Robot()
    run_robot = RunRobot(robot)
    run_robot.run()
