# motioneye 2.0

## **Description:**

MotionEye 2.0 is an advanced project designed to determine the speed of a vehicle using a downward-facing camera. This version employs the Extended Kalman Filter (EKF) and other advanced techniques to improve the accuracy and stability of speed estimation. The project processes video frames to track ground features and calculate vehicle speed.

## **Tech Stack:**
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy
- **Algorithms:** Optical Flow (Lucas-Kanade), Extended Kalman Filter
- **Tools:** Video frame extraction, Advanced feature detection

## **Techniques Used:**

1. **Video Frame Extraction:**
   - Extract frames from a video of a downward-facing camera using OpenCV.
   - Convert frames to grayscale for consistent feature detection and optical flow analysis.

2. **Feature Detection:**
   - Use Good Features to Track (Shi-Tomasi corner detector) or advanced methods like ORB/SIFT to identify distinct points of interest in the initial frame.

3. **Optical Flow Calculation:**
   - Apply the Lucas-Kanade method to track the movement of detected features between consecutive frames.
   - Calculate the displacement of features to estimate motion.

4. **Extended Kalman Filter:**
   - Implement an EKF to handle non-linear state transitions and measurements.
   - Use the EKF to predict and update the state of the vehicle's motion.
   - Smooth the speed estimates to reduce the impact of noise and variability.

5. **Speed Estimation:**
   - Compute the speed of the vehicle based on the displacement of tracked features and the frame rate.
   - Apply a moving average to smooth the speed estimates and provide more stable results.

