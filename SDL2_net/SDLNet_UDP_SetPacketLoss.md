###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_SetPacketLoss

Set the percentage of simulated packet loss for packets sent on the socket.

## Syntax

```c
void SDLNet_UDP_SetPacketLoss(UDPsocket sock, int percent);

```

## Function Parameters

|                 |                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| **sock**        | the socket to simulate packet loss on.                                                                     |
| **percent**     | a value from 0 to 100 of likelihood to drop a packet (higher the number means more likelihood of dropping. |

## Remarks

SDL_net can optionally, at random, drop packets that are being sent and
received, to simulate bad networking conditions. As these sort of
conditions can happen in the real world but likely won't between machines
on the same LAN, you can use this function in testing to make sure your app
is robust against network problems even on a fast, reliable network.

You probably don't want to use this function outside of local testing.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
