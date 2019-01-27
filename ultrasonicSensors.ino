const int trigPin1 = 10;
const int echoPin1 = 11;
const int trigPin2 = 3;
const int echoPin2 = 4;

// defines variables
long duration1;
int distance1;

long duration2;
int distance2;
void setup() {
pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT); 
Serial.begin(115200); // Starts the serial communication
}

void loop() {
  String sensorData;
// Clears the trigPin
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);
distance1= duration1*0.034/2;

digitalWrite(trigPin2, LOW);
delayMicroseconds(2);
digitalWrite(trigPin2, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin2, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration2 = pulseIn(echoPin2, HIGH);
// Calculating the distance
distance2= duration2*0.034/2;

// Prints the distance on the Serial Monitor
sensorData+= String(distance1)+",";
sensorData+= String(0)+",";
sensorData+= String(distance2);
Serial.println(sensorData);
}
