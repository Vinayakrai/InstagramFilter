# InstagramFilter

**InstagramFilter** is a Python-based application that applies a fun filter to live webcam feed. Utilizing libraries such as OpenCV, NumPy, Dlib, and Hypot, this project detects human faces in real-time and overlays a pig nose image onto the detected faces, creating an amusing effect similar to filters found on social media platforms.

## 🚀 Features

- **Real-Time Face Detection**: Detects human faces from the webcam feed using Dlib's facial landmark detection.
- **Filter Overlay**: Applies a pig nose image onto the detected face, aligning it accurately based on facial landmarks.
- **Live Webcam Feed**: Processes video frames in real-time, displaying the filtered output instantly.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Required Libraries**:
  - `opencv-python`
  - `numpy`
  - `dlib`
  - `hypot` (Note: `hypot` is a function from the `math` module; ensure it's imported correctly.)

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/InstagramFilter.git
cd InstagramFilter
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install opencv-python numpy dlib
```

*Note*: Ensure that CMake and Boost are installed on your system, as they are prerequisites for installing Dlib.

3. **Download Pre-trained Shape Predictor**:

Download the `shape_predictor_68_face_landmarks.dat` file from [Dlib's model zoo](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2), extract it, and place it in the project directory.

## 🚀 Usage

Run the script using Python:

```bash
python instafilter.py
```

The script will:

1. Access your system's default webcam.
2. Detect faces in the video feed.
3. Overlay a pig nose image onto each detected face.
4. Display the live video with the applied filter.

Press the `Esc` key to exit the application.

## 📁 Project Structure

```
InstagramFilter/
├── instafilter.py                 # Main script
├── pig.png                        # Pig nose image
├── shape_predictor_68_face_landmarks.dat  # Facial landmark model
└── README.md                      # Project documentation
```

## ⚠️ Notes

- Ensure your webcam is properly connected and accessible by the system.
- The accuracy of the filter overlay depends on the quality of the webcam and lighting conditions.
- The `pig.png` image should have a transparent background for optimal results.


