import cv2
import boto3
import os
from datetime import datetime
# Step 1: Change this to your actual S3 bucket name
BUCKET_NAME = 'smile-detection-lab-zehra'
REGION = 'us-east-1'  # Change this if you're using a different region
# Step 2: Create an S3 client
s3 = boto3.client('s3', region_name=REGION)
# Step 3: Set image filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"webcam_{timestamp}.jpg"
# Step 4: Open the webcam
cap = cv2.VideoCapture(0)
print("Webcam opened. Press SPACE to capture the photo.")
while True:
    ret, frame = cap.read()
    cv2.imshow('Press SPACE to Capture', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        # Save image
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
        break
cap.release()
cv2.destroyAllWindows()
# Step 5: Upload image to S3
print("Uploading image to S3...")
s3.upload_file(Filename=filename, Bucket=BUCKET_NAME, Key=filename)
print(f"Uploaded to: s3://{BUCKET_NAME}/{filename}")

