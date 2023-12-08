###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetLocalAddresses

Obtain a list of local addresses on the system.

## Syntax

```c
extern DECLSPEC SDLNet_Address **SDLCALL SDLNet_GetLocalAddresses(int *num_addresses);

```

## Function Parameters

|                       |                                                                        |
| --------------------- | ---------------------------------------------------------------------- |
| **num_addresses**     | on exit, will be set to the number of addresses returned. Can be NULL. |

## Return Value

Returns A NULL-terminated array of [SDLNet_Address](SDLNet_Address.md)
pointers, one for each bindable address on the system, or NULL on error;
call SDL_GetError() for details.

## Remarks

This returns addresses that you can theoretically bind a socket to, to
accept connections from other machines at that address.

You almost never need this function; first, it's hard to tell _what_ is a
good address to bind to, without asking the user (who will likely find it
equally hard to decide). Second, most machines will have lots of _private_
addresses that are accessible on the same LAN, but not public ones that are
accessible from the outside Internet.

Usually it's better to use [SDLNet_CreateServer](SDLNet_CreateServer.md)() or
[SDLNet_CreateDatagramSocket](SDLNet_CreateDatagramSocket.md)() with a NULL
address, to say "bind to all interfaces."

The array of addresses returned from this is guaranteed to be
NULL-terminated. You can also pass a pointer to an int, which will return
the final count, not counting the NULL at the end of the array.

Pass the returned array to
[SDLNet_FreeLocalAddresses](SDLNet_FreeLocalAddresses.md) when you are done
with it. It is safe to keep any addresses you want from this array even
after calling that function, as long as you called
[SDLNet_RefAddress](SDLNet_RefAddress.md)() on them.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
