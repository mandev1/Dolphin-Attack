# Dolphin-Attack
Source Code of Dolphin Attack code for Smart Speaker

## Introduction
Audio hijacking is a hacking method used to
transmit instructions by air using ultrasonic waves. 
This technique is called the dolphin attack, because of the way
It works the same way dolphins communicate with their herd.

## How it Works
In this Case, there is a sending computer acting as Command
and Control (CnC), sends instructions to the computer that is used
intermediary for sending instructions to the smart speaker. CnC sends instructions for
smart speaker in text form and sent to the target computer via a socket.
Once the target computer has received the instructions, it is converted to audible
audio, then modulated into inaudible audio and played on the target computer and
heard by smart speakers. The concept of how the dolphin attack works can be seen
in Figure below.

![image](https://user-images.githubusercontent.com/101856662/186618297-1ad98cb0-c41b-4c5f-9ac5-4a4c3a506df1.png)

## Source Code
The server program entered on the target computer acts as a
intermediary target computer and CnC to transmit instructions and convert
into ultrasonic sound waves. The server program is in charge of
converts the instructions given from the server to wave
ultrasonic and emitted by the target computer loudspeaker. When the program
running, the server then looks for the client connection then ready to receive 
instructions from the client. 

### Client side
Once connected, the client can send instructions using the
socket, received by the server and processed on the target computer. How the program works
client can be seen in Figure below.

![image](https://user-images.githubusercontent.com/101856662/186618436-6fe0fde9-9d5e-4490-a615-d7d9a8d887ad.png)

### Server Side
When the client sends an instruction, the server receives the instruction and then
converted to inaudible sound. This ultrasonic wave is then emitted
by the loudspeaker and received by the smart speaker. How the server program works can be
seen in Figure below.

![image](https://user-images.githubusercontent.com/101856662/186618507-6d019d4a-4aa8-4953-ba4b-9c6a493b911c.png)

## Result
### Hi Alexa, Hallo
![set(hallo)](https://user-images.githubusercontent.com/101856662/186622334-b94c5bbb-78e7-4e7e-86cb-956e510648e4.png)

### Hi Alexa, Open Demo Skill
![set(demoskill)](https://user-images.githubusercontent.com/101856662/186622590-0ca3583c-fda2-48b9-b191-5718c27370d5.png)

### Hi Alexa, How Are You
![set(how are you)](https://user-images.githubusercontent.com/101856662/186622686-bc42dd95-72fb-41fb-8bc4-c0de9b8dc39c.png)

### Hi Alexa, Tell Me a Joke
![set(tell me a joke)](https://user-images.githubusercontent.com/101856662/186622727-fe8a2461-b5e5-4c19-b667-c3c5b7733e65.png)

### Hi Alexa, Tell Me about Indonesia
![set(indonesia)](https://user-images.githubusercontent.com/101856662/186622775-a8f4bd11-77d8-4ad8-aa86-306f389f9a49.png)

## Information 
All of Audio files are located in Result Folder
