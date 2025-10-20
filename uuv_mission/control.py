class pid_controller:
    def __init__(self, Kp: float, Ki: float, Kd: float):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    
    def get_action(self, current_error, errors_sum, previous_error) -> float:
        action = (self.Kp * current_error +
                  self.Ki * errors_sum +
                  self.Kd * (current_error - previous_error))
        return action
