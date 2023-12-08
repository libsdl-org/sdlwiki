###### (This is part of SDL_net, a separate library from SDL.)
# SDLNet_DatagramSocket

An opaque data type in SDL3_Net for datagram sockets.

Datagram sockets map to [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) sockets. They offer data as stateless packets of data sent between arbitrary network addresses.

You can create one of these with [SDLNet_CreateDatagramSocket](SDLNet_CreateDatagramSocket.md). Unlike with [SDLNet_StreamSockets](SDLNet_StreamSocket.md), there is no client and server; everything uses the same type of datagram socket. The actual object returned is an opaque data structure; your code should just treat it like a handle to various SDL3_net functions.

Datagram sockets are _unreliable_, which is to say that when you send packets out into the world, they might arrive in a different order than you sent them, and some or all of them may not arrive at all! There is no indication that any given packet arrived, unless the other side sends back a packet of its own that indicates in some way that it saw a specific packet arrive.

Datagram packets either arrive completely or not at all. You never receive a partial packet. Each packet may be a different size.

There is no client/server relationship implicit in datagram sockets, although one can certainly structure an app to behave as such. Any socket can send to any address/port on the network that it can reach, and each received packet will contain the sender's address/port so that a reply can be made. There is no state or concept of an ongoing connection, so a single packet might be the complete relationship between the two sockets.

Datagram packets also have extremely strict size requirements! In theory, you can send one that's up to 64 kilobytes in size, but in practice, you should _never_ send one more than about 1200 bytes (to allow space for IPv6 headers and maybe future protocols); Internet routers might have to fragment larger packets and if a single fragment is lost the entire packet is lost. Furthermore, some popular routers in homes have hardcoded limits, and will unconditionally drop all packets larger than this limit! This is not an SDL3_net limitation; this is just the reality of UDP packets traveling across the Internet. Plan to split up your data into packets of this size or less.

Since packets have no rules for reliability, it means there is never a delay in their reception: the system never has to wait for lost packets to arrive, because it's built to assume packets will be lost and it will be the app's responsibility to deal with that. This can be a serious design burden for the app developer, and can make stream sockets more attractive.

In terms of compatibility with the general Internet: lots of standard services and games run on UDP sockets. So if you want to connect to a VoIP system, your first step might be to connect to it with an SDLNet_DatagramSocket (and then implement the specific VoIP protocol on top of this, to be clear).
