# Object Tracking and Feedback System

This project merges the capabilities of computer vision and microcontroller programming to create a dynamic system that tracks an object's position and provides immediate feedback through visual signals (LEDs) and sound (buzzer). It's perfect for educational purposes, hobbyist projects, or anyone interested in exploring the intersection of software and hardware.

## Features

- **Real-Time Object Detection:** Leverages a pre-trained YOLOv5 model for accurate detection within the camera's view.
- **Interactive Feedback:** Utilizes LEDs for directional feedback and a buzzer for distance-related auditory signals.
- **Dynamic State Reset:** Incorporates a push button to allow users to redefine the "ideal state" dynamically.

## Getting Started

### Prerequisites

- A computer with Python 3.x installed.
- Arduino IDE for uploading the sketch to the Arduino board.
- A USB webcam or a camera module that can be accessed by OpenCV.
- An Arduino board (Uno, Mega, etc.), LEDs, buzzer, push button, resistors, breadboard, and jumper wires.

### Hardware Setup

1. **LEDs:** Connect each LED through a resistor to specified PWM pins on Arduino (Red: 9, Green: 10, White: 11, Blue: 6) and their other legs to GND.
2. **Buzzer:** Attach the positive leg to pin 5 and the negative leg to GND on the Arduino.
3. **Push Button:** Link one leg to pin 2 and the other directly to GND. This will use Arduino's internal pull-up resistor.

### Software Installation

1. **Arduino Sketch:**
   - Open the Arduino IDE, load the provided `.ino` file, select the correct board and port under the Tools menu, and upload the sketch to your Arduino.

2. **Python Environment Setup:**
   - It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide packages. Navigate to your project directory in the terminal and run:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`
   - Install the required Python libraries:
     ```bash
     pip install opencv-python numpy pyserial torch torchvision torchaudio
     ```

### Running the System

- With the Arduino connected and the virtual environment activated, run the Python script:
  ```bash
  python main.py

