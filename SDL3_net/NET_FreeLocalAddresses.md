###### (This function is part of SDL_net, a separate library from SDL.)
# NET_FreeLocalAddresses

Free the results from [NET_GetLocalAddresses](NET_GetLocalAddresses).

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void NET_FreeLocalAddresses(NET_Address **addresses);
```

## Function Parameters

|                               |               |                                                                         |
| ----------------------------- | ------------- | ----------------------------------------------------------------------- |
| [NET_Address](NET_Address) ** | **addresses** | A pointer returned by [NET_GetLocalAddresses](NET_GetLocalAddresses)(). |

## Remarks

This will unref all addresses in the array and free the array itself.

Since addresses are reference counted, it is safe to keep any addresses you
want from this array even after calling this function, as long as you
called [NET_RefAddress](NET_RefAddress)() on them first.

It is safe to pass a NULL in here, it will be ignored.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

