###### (This function is part of SDL_net, a separate library from SDL.)
# NET_UnrefAddress

Drop a reference to an [NET_Address](NET_Address).

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void NET_UnrefAddress(NET_Address *address);
```

## Function Parameters

|                              |             |                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------ |
| [NET_Address](NET_Address) * | **address** | The [NET_Address](NET_Address) to drop a reference to. |

## Remarks

Since several pieces of the library might share a single
[NET_Address](NET_Address), including a background thread that's working on
resolving, these objects are referenced counted. This allows everything
that's using it to declare they still want it, and drop their reference to
the address when they are done with it. The object's resources are freed
when the last reference is dropped.

This function drops a reference to an [NET_Address](NET_Address),
decreasing its reference count by one.

The documentation will tell you when the app has to explicitly unref an
address. For example, [NET_ResolveHostname](NET_ResolveHostname)() creates
addresses that are already referenced, so the caller needs to unref it when
done.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

