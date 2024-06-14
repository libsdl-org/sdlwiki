###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetLocalAddresses

Get the addresses of network interfaces on this system.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
int SDLNet_GetLocalAddresses(IPaddress *addresses, int maxcount);
```

## Function Parameters

|             |               |                                                          |
| ----------- | ------------- | -------------------------------------------------------- |
| IPaddress * | **addresses** | where to store the returned information.                 |
| int         | **maxcount**  | the number of results that can be stored at `addresses`. |

## Return Value

(int) Returns the number of addresses saved in `addresses`.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

