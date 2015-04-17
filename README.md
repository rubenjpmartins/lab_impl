# lab_impl
server-client implementation

Chat based on TFTP protocol. The server is launched and it's supposed to process requests from the running clients. At the moment, it can only process requests form two users.
The first client that registers is able to choose Read or Write mode; the other client that registers is attributed the mode that's left. From then on, everytime a message is sent and read, the modes switch and allow communication in the opposite way (Read mode client receives the message, Write mode client sends it).
Looking for someone to implement TCP mode, only runs on UDP at the moment.
