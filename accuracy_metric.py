import cv2
import numpy as np

def average_saturation(image):
    
    # Convert to HSV color space
    hsv_image = cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_YUV2RGB),cv2.COLOR_RGB2HSV)
    
    # Extract the Saturation channel
    saturation = hsv_image[:, :, 1].astype(np.float32)  # Convert to float for precision
    
    # Compute average saturation
    S_avg = np.mean(saturation)
    
    return S_avg

def saturation_difference(original, prediction):
    S_avg_original = average_saturation(original)
    S_avg_prediction = average_saturation(prediction)
    
    # Compute percent deviation in average saturation
    percent_deviation = (abs(S_avg_prediction - S_avg_original) / S_avg_original) * 100 if S_avg_original > 0 else 0
    
    return percent_deviation

def auc_color_accuracy(predicted_image, ground_truth_image, thresholds=np.arange(0, 151)):
    # Load images
    pred = cv2.imread(predicted_image)
    gt = cv2.imread(ground_truth_image)
    
    if pred is None or gt is None:
        raise ValueError("Error: Unable to load one or both images.")
    
    # Convert to LAB color space
    pred_lab = cv2.cvtColor(cv2.cvtColor(pred,cv2.COLOR_YUV2RGB), cv2.COLOR_RGB2Lab)
    gt_lab = cv2.cvtColor(cv2.cvtColor(gt, cv2.COLOR_YUV2RGB), cv2.COLOR_RGB2Lab)
    
    # Extract 'ab' channels
    pred_ab = pred_lab[:, :, 1:].astype(np.float32)
    gt_ab = gt_lab[:, :, 1:].astype(np.float32)
    
    # Compute L2 distance per pixel in 'ab' space
    dist = np.linalg.norm(pred_ab - gt_ab, axis=2)
    
    # Compute cumulative mass function (CMF)
    cmf = np.array([np.mean(dist <= t) for t in thresholds])
    
    # Compute area under the curve (AUC) and normalize
    auc = np.trapz(cmf, thresholds) / (thresholds[-1] - thresholds[0])
    
    return auc