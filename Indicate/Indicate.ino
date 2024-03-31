int redLED = 10;
int greenLED = 11;
int whiteLED = 12;
int blueLED = 13;
int buzzer = 9;
int buttonPin = 2; // Button pin
bool buttonPressed = false;

void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(whiteLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP); // Use internal pull-up
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  // Check if button is pressed
  if (buttonState == LOW) {
    if (!buttonPressed) {
      Serial.println("reset");
      buttonPressed = true; // Avoid multiple prints
      delay(500); // Debounce delay
    }
  } else {
    buttonPressed = false;
  }

  // Handle incoming commands from Python script
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // Remove any whitespace

    // Turn off all LEDs and the buzzer first
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
    digitalWrite(whiteLED, LOW);
    digitalWrite(blueLED, LOW);
    noTone(buzzer);

    if (command == "ideal") {
      // Turn on the buzzer for the ideal state
      tone(buzzer, 1000); // Set buzzer to 1kHz
    } else if (command == "off") {
      // Turn off the buzzer, already handled above
    } else {
      // Parse the direction command and control LEDs
      if (command.indexOf("left") != -1) {
        digitalWrite(redLED, HIGH);
      }
      if (command.indexOf("right") != -1) {
        digitalWrite(greenLED, HIGH);
      }
      if (command.indexOf("up") != -1) {
        digitalWrite(whiteLED, HIGH);
      }
      if (command.indexOf("down") != -1) {
        digitalWrite(blueLED, HIGH);
      }
    }
  }
}

