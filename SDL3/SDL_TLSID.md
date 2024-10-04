###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TLSID

Thread local storage ID.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef SDL_AtomicInt SDL_TLSID;
```

## Remarks

0 is the invalid ID. An app can create these and then set data for these
IDs that is unique to each thread.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_GetTLS](SDL_GetTLS)
- [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryThread](CategoryThread)

