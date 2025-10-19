class pid_controller:
    def __init__(self, Kp: float, Ki: float, Kd: float):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    
    def get_action(self, reference: float, measurement: float, previous_e) -> float:
        error = reference - measurement
        action = self.Kp * error + self.Kd * (error - previous_e)
        return action, error
