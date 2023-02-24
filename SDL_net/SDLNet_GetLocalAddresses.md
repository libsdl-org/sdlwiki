###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetLocalAddresses

Get the addresses of network interfaces on this system.

## Syntax

```c
int SDLNet_GetLocalAddresses(IPaddress *addresses, int maxcount);

```

## Function Parameters

|                   |                                                         |
| ----------------- | ------------------------------------------------------- |
| **addresses**     | where to store the returned information.                |
| **maxcount**      | the number of results that can be stored at `addresses` |

## Return Value

Returns the number of addresses saved in `addresses`

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI)

