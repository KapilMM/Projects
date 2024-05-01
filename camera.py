import cv2
import smtplib
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, render_template, Response

video = cv2.VideoCapture(0)
app = Flask('__name__')

# Email configuration
email_sender = 'kapilmeshram484@gmail.com'  # Replace with your email
email_receiver = 'mkapil45@yahoo.com'  # Replace with the receiver's email
email_password = 'jlsy vaxt gjxo pzvw'  # Replace with your email password

# Video Sending Interval and Length
video_send_interval = 60  # seconds
video_length = 30  # seconds

def video_stream():
    start_time = time.time()
    while True:
        # Capture video frame
        ret, frame = video.read()
        if not ret:
            break

        # Resize frame to lower resolution
        frame = cv2.resize(frame, (320, 240))  # Adjust size for lower resolution

        # Encode frame to JPEG
        ret, buffer = cv2.imencode('.jpeg', frame)
        frame_bytes = buffer.tobytes()

        # Check if it's time to send the video
        if time.time() - start_time >= video_send_interval:
            # Start timer for next video
            start_time = time.time()

            # Capture and send video
            send_video_email(frame)
            yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


def send_video_email(frame):
    # Write the frame to a temporary video file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec for MP4
    out = cv2.VideoWriter('output.mp4', fourcc, 10.0, (320, 240))  # Adjust resolution and fps as needed for lower resolution
    start_time = time.time()
    while time.time() - start_time < video_length:
        out.write(frame)
    out.release()

    # Send the video via email
    send_video_email_with_attachment('output.mp4')

    # Remove the temporary video file
    os.remove('output.mp4')


def send_video_email_with_attachment(video_path):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = 'Subject of the email'

    # Attach the video to the email
    with open(video_path, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(video_path))
    msg.attach(attachment)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

    print("Video file created successfully.")
    print("Email sent successfully.")


@app.route('/camera')
def camera():
    return render_template('camera.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
