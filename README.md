# Face Recognition
This is a Python-based face recognition system that uses OpenCV and Haar Cascades to detect and recognize faces in real-time video streams. The system is designed to be easy to use and can be integrated into a variety of applications, such as security systems, attendance trackers, or personalized content delivery.

## Installation
To use this face recognition system, you need to have Python 3.x installed on your computer along with the OpenCV and NumPy libraries. You can install these libraries using pip by running the following commands:

```
pip install opencv-python
pip install numpy
```
You will also need to download the Haar Cascade classifiers from the OpenCV GitHub repository. You can do this by running the following command:

```
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```
Once you have installed the necessary libraries and downloaded the classifiers, you can run the face recognition system using the following command:

```
python face_recognition.py
```
## Usage
The face recognition system is designed to work with live video streams from a webcam. When you run the program, it will automatically detect and recognize faces in the video stream. If a face is detected, the system will compare it to a pre-trained set of faces and try to match it to a known user.

To add new faces to the system, you can use the `create_user.py` script. This script will prompt you to enter a user name and then capture a series of images of the user's face. The images will be saved to the data/ directory and used to train the face recognition system.

## Contributing
If you want to contribute to this project, feel free to fork the repository and make changes as needed. We welcome contributions of all types, including bug fixes, new features, or documentation improvements.

Before making any changes, please create a new branch and submit a pull request outlining the changes you made. We will review your changes and merge them into the main branch if they meet our guidelines and standards.

## License
This face recognition system is released under the MIT License. See the LICENSE file for more information.
