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
