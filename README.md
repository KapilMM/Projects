## Remote Live CCTV: Raspberry Pi Surveillance System

### Project Overview

The **Remote Live CCTV Surveillance System** enables real-time video monitoring using a Raspberry Pi with a USB camera. Users can remotely access live camera feeds via a web interface. The system also includes motion detection, triggering email notifications with images when motion is detected.

### Hardware Requirements

To set up the system, you'll need the following hardware components:

1. **Raspberry Pi**: Choose a compatible model (e.g., Raspberry Pi 3 or 4).
2. **USB Camera**: Select a USB camera with suitable resolution and features.
3. **Memory Card**: Use a reliable and adequately sized memory card (e.g., 32GB or higher).
4. **Stable Network Connection**: Ensure the Raspberry Pi connects to a stable network with internet access.

### Installation Steps

1. **Installing the Operating System on Raspberry Pi**:
    - Download the latest version of Raspberry Pi OS from the official website.
    - Flash the OS image onto the memory card using tools like Etcher.
    - Insert the memory card into the Raspberry Pi and power it on.

2. **Configuring Raspberry Pi Access**:
    - Enable SSH: Run `sudo raspi-config`, navigate to "Interfacing Options," and enable SSH.
    - Enable VNC Server: Follow the instructions to enable VNC server in the Raspberry Pi configuration.
    - Install XRDP Server: Run `sudo apt install xrdp` to install XRDP server for remote desktop access.

3. **Creating a Flask Server with Python for Live Video Streaming**:
    - Install Flask: Run `sudo apt install python3-flask` to install Flask.
    - Write a Python file (e.g., `camera.py`) that sets up a Flask server to stream live video from the USB camera.
    - Use OpenCV to capture frames from the camera and serve them via the Flask app.
    - Create an HTML template file (e.g., `camera.html`) for the web interface to display the live feed.

4. **Motion Detection Configuration**:
    - Implement motion detection using OpenCV:
        - Capture consecutive frames from the camera.
        - Compare frames to detect changes (motion).
        - Adjust sensitivity settings to minimize false positives.
    - Upon detecting motion, trigger an event (e.g., save images, send notifications).

5. **Integration with remote.it**:
    - Install remote.it: Follow the instructions to install remote.it on the Raspberry Pi.
    - Set up port forwarding rules in the remote.it app for TCP access, HTTP access, and SSH access.
    - Use the proxy address provided by remote.it for remote access via the app.

### Troubleshooting and Support

If you encounter any issues during the setup, consider the following steps:

- **Check Connections**: Ensure all hardware components (Raspberry Pi, camera, memory card) are properly connected.
- **Debugging**: Review logs, error messages, and Python code for any issues.
- **Community Forums**: Visit Raspberry Pi forums or online communities for assistance.
- **Contact Me**: If you need further help, feel free to reach out. I'm here to assist!


Acknowledgments: Special thanks to all the contributors and community members for their inspiration and assistance in building this system.
📷🔍👀 Feel free to customize the project details further, and don't hesitate to ask if you need additional guidance! 
😊 Happy coding! 


`MIT`

This project is licensed under the MIT License - see the LICENSE file for details.

`Apache`

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

`GNU`

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

