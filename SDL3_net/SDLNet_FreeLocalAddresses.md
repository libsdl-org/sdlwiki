###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreeLocalAddresses

Free the results from [SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses).

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void SDLNet_FreeLocalAddresses(SDLNet_Address **addresses);
```

## Function Parameters

|                                     |               |                                                                               |
| ----------------------------------- | ------------- | ----------------------------------------------------------------------------- |
| [SDLNet_Address](SDLNet_Address) ** | **addresses** | A pointer returned by [SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses)(). |

## Remarks

This will unref all addresses in the array and free the array itself.

Since addresses are reference counted, it is safe to keep any addresses you
want from this array even after calling this function, as long as you
called [SDLNet_RefAddress](SDLNet_RefAddress)() on them first.

It is safe to pass a NULL in here, it will be ignored.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

