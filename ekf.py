import numpy as np

class ExtendedKalmanFilter:
    def __init__(self, dt, state_dim, measurement_dim, process_noise_cov, measurement_noise_cov):
        self.dt = dt
        self.x = np.zeros((state_dim, 1))
        self.P = np.eye(state_dim)
        self.Q = process_noise_cov
        self.R = measurement_noise_cov

    def state_transition(self, x):
        F = np.array([[1, 0, self.dt, 0],
                      [0, 1, 0, self.dt],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
        return np.dot(F, x)

    def measurement_function(self, x):
        H = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0]])
        return np.dot(H, x)

    def predict(self):
        self.x = self.state_transition(self.x)
        F = np.array([[1, 0, self.dt, 0],
                      [0, 1, 0, self.dt],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
        self.P = np.dot(np.dot(F, self.P), F.T) + self.Q

    def update(self, z):
        H = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0]])
        y = z - self.measurement_function(self.x)
        S = np.dot(np.dot(H, self.P), H.T) + self.R
        K = np.dot(np.dot(self.P, H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(np.dot(K, H), self.P)

    def get_state(self):
        return self.x
