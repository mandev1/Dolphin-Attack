# Dolphin-Attack
Source Code of Dolphin Attack code for Smart Speaker

Audio hijacking is a hacking method used to
transmit instructions by air using ultrasonic waves. 
This technique is called the dolphin attack, because of the way
It works the same way dolphins communicate with their herd.

In this Case, there is a sending computer acting as Command
and Control (CnC), sends instructions to the computer that is used
intermediary for sending instructions to the smart speaker. CnC sends instructions for
smart speaker in text form and sent to the target computer via a socket.
Once the target computer has received the instructions, it is converted to audible
audio, then modulated into inaudible audio and played on the target computer and
heard by smart speakers. The concept of how the dolphin attack works can be seen
in Figure 3.1.

The server program entered on the target computer acts as a
intermediary target computer and CnC to transmit instructions and convert
into ultrasonic sound waves. The server program is in charge of
converts the instructions given from the server to wave
ultrasonic and emitted by the target computer loudspeaker. When the program
running, the server then looks for the client connection then ready to receive 
instructions from the client. 

Once connected, the client can send instructions using the
socket, received by the server and processed on the target computer. How the program works
client can be seen in Figure 3.2.

When the client sends an instruction, the server receives the instruction and then
converted to inaudible sound. This ultrasonic wave is then emitted
by the loudspeaker and received by the smart speaker. How the server program works can be
seen in Figure 3.3.
