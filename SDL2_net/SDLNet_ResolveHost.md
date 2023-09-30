###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_ResolveHost

Resolve a host name and port to an IP address in network form.

## Syntax

```c
int SDLNet_ResolveHost(IPaddress *address, const char *host, Uint16 port);

```

## Function Parameters

|                 |                                                             |
| --------------- | ----------------------------------------------------------- |
| **address**     | to be filled in with the resolved address and port.         |
| **host**        | the hostname to lookup (like "libsdl.org")                  |
| **port**        | the port intended to be connected to, to fill into address. |

## Return Value

Returns zero on success, -1 on error.

## Remarks

If `host` is NULL, the resolved host will be set to `INADDR_ANY`.

If the host couldn't be resolved, the host portion of the returned address
will be INADDR_NONE, and the function will return -1.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI)

