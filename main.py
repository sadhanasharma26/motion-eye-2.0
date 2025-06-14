import os
import cv2
import numpy as np
from ekf import ExtendedKalmanFilter
#from utils import load_images

frame_rate = 30
scale_factor = 0.1
process_noise_cov = np.eye(4) * 0.1
measurement_noise_cov = np.eye(2) * 0.1

ekf = ExtendedKalmanFilter(dt=1.0 / frame_rate,
                           state_dim=4,
                           measurement_dim=2,
                           process_noise_cov=process_noise_cov,
                           measurement_noise_cov=measurement_noise_cov)

image_folder = 'images'
image_files = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith('.jpg')])

gray_images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_files]


previous_points = None
speed_estimates = []

for i in range(1, len(gray_images)):
    frame = gray_images[i]
    if previous_points is None:
        previous_points = cv2.goodFeaturesToTrack(gray_images[i-1], maxCorners=100, qualityLevel=0.01, minDistance=10)
    else:
        next_points, status, _ = cv2.calcOpticalFlowPyrLK(gray_images[i-1], frame, previous_points, None)
        if next_points is not None and status is not None:
            good_new = next_points[status == 1]
            good_old = previous_points[status == 1]
            if len(good_new) > 0 and len(good_old) > 0:
                displacement = np.mean(good_new - good_old, axis=0)
                measurement = np.array([[displacement[0]], [displacement[1]]])
                ekf.predict()
                ekf.update(measurement)
                state = ekf.get_state()
                vx = state[2, 0]
                vy = state[3, 0]
                speed = np.sqrt(vx**2 + vy**2) * scale_factor
                speed_estimates.append(speed)
                if len(speed_estimates) > 5:
                    speed_estimates.pop(0)
                smoothed_speed = np.mean(speed_estimates)
                print(f'estimated speed at frame {i}: {smoothed_speed:.2f} m/s')
                previous_points = good_new.reshape(-1, 1, 2)
            else:
                previous_points = None
        else:
            previous_points = None
