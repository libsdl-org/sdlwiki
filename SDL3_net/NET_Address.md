###### (This function is part of SDL_net, a separate library from SDL.)
# NET_Address

Opaque representation of a computer-readable network address.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef struct NET_Address NET_Address;
```

## Remarks

This is an opaque datatype, to be treated by the app as a handle.

SDL_net uses these to identify other servers; you use them to connect to a
remote machine, and you use them to find out who connected to you. They are
also used to decide what network interface to use when creating a server.

These are intended to be protocol-independent; a given address might be for
IPv4, IPv6, or something more esoteric. SDL_net attempts to hide the
differences.

## Version

This datatype is available since SDL_net 3.0.0.

## See Also

- [NET_ResolveHostname](NET_ResolveHostname)
- [NET_GetLocalAddresses](NET_GetLocalAddresses)
- [NET_CompareAddresses](NET_CompareAddresses)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLNet](CategorySDLNet)

