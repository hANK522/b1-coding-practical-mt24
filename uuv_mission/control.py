class pid_controller:
    def __init__(self, Kp: float, Ki: float, Kd: float):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    
    def get_action(self, reference: float, measurement: float) -> float:
        error = reference - measurement
        action = self.Kp * error
        return action
