###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UnrefAddress

Drop a reference to an [SDLNet_Address](SDLNet_Address.md).

## Syntax

```c
void SDLNet_UnrefAddress(SDLNet_Address *address);

```

## Function Parameters

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| **address**     | The [SDLNet_Address](SDLNet_Address.md) to drop a reference to. |

## Remarks

Since several pieces of the library might share a single
[SDLNet_Address](SDLNet_Address.md), including a background thread that's
working on resolving, these objects are referenced counted. This allows
everything that's using it to declare they still want it, and drop their
reference to the address when they are done with it. The object's resources
are freed when the last reference is dropped.

This function drops a reference to an [SDLNet_Address](SDLNet_Address.md),
decreasing its reference count by one.

The documentation will tell you when the app has to explicitly unref an
address. For example, [SDLNet_ResolveHostname](SDLNet_ResolveHostname.md)()
creates addresses that are already referenced, so the caller needs to unref
it when done.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
