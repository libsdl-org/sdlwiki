###### (This is part of SDL_net, a separate library from SDL.)
# SDLNet_StreamSocket

An opaque data type in SDL3_Net for stream sockets.

Stream sockets map to TCP sockets. They offer data as an ongoing stream of bytes that can flow in either direction.

You can create one of these with either [SDLNet_CreateClient](SDLNet_CreateClient) (to connect to a remote server) or [SDLNet_AcceptClient](SDLNet_AcceptClient) (to accept the client connection to your server). The actual object returned is an opaque data structure; your code should just treat it like a handle to various SDL3_net functions.

Stream sockets are _reliable_, which is to say the system will deal with lost data on your behalf by verifying data arrived at the remote end, and retransmitting as necessary through a careful protocol; to the socket though, it just looks like bytes arrived as they were sent.

The downside of this reliability is potential lag: until the system has received everything it needs to present the next bytes in the stream, it presents nothing, and in poor network conditions, this can be dramatic.

You can only connect a stream socket to one destination (client to server), and those two ends can talk back and forth. A server might have multiple streams connected to different clients, but each one is unique. In contrast, a single [SDLNet_DatagramSocket](SDLNet_DatagramSocket) might be receiving and sending packets of data to many different systems, each of which might also be doing the same with their socket.

Often times, realtime multimedia apps--like games, streaming media, and video chat programs--will use datagram sockets instead of stream sockets, but they need to be carefully designed to carry on when individual chunks of data are lost in transit. While the end result might be a more flexible and robust application, this design work can be difficult.

And, it's worth saying: not always necessary! World of Warcraft, for example, might have thousands of people on a single server, updating a complex world in realtime...and each player is connected to the server with a stream socket! So consider what your app needs carefully--and test!--before you start significant coding.

In terms of compatibility with the general Internet: lots of standard services run on TCP sockets. So if you want to connect to a web server to do an HTTP request, your first step is to connect to it with an SDLNet_StreamSocket (and then implement the HTTP protocol on top of this, to be clear).