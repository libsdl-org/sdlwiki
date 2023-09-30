###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_SimulateStreamPacketLoss

Enable simulated stream socket failures.

## Syntax

```c
void SDLNet_SimulateStreamPacketLoss(SDLNet_StreamSocket *sock, int percent_loss);

```

## Function Parameters

|                      |                                                                          |
| -------------------- | ------------------------------------------------------------------------ |
| **sock**             | The socket to set a failure rate on.                                     |
| **percent_loss**     | A number between 0 and 100. Higher means more failures. Zero to disable. |

## Remarks

Often times, testing a networked app on your development machine--which
might have a wired connection to a fast, reliable network service--won't
expose bugs that happen when networks intermittently fail in the real
world, when the wifi is flakey and firewalls get in the way.

This function allows you to tell the library to pretend that some
percentage of stream socket data transmission will fail.

Since stream sockets are reliable, failure in this case pretends that
packets are getting lost on the network, making the stream retransmit to
deal with it. To simulate this, the library will introduce some amount of
delay before it sends or receives data on the socket. The higher the
percentage, the more delay is introduced for bytes to make their way to
their final destination. The library may also decide to drop connections at
random, to simulate disasterous network conditions.

Setting this to zero (the default) will disable the simulation. Setting to
100 means _everything_ fails unconditionally and no further data will get
through (and perhaps your sockets eventually fail). At what percent the
system merely borders on unusable is left as an exercise to the app
developer.

This is intended for debugging purposes, to simulate real-world conditions
that are various degrees of terrible. You probably should _not_ call this
in production code, where you'll likely see real failures anyhow.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI)

