###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTLS

Create a piece of thread-local storage.

## Syntax

```c
SDL_TLSID SDL_CreateTLS(void);

```

## Return Value

Returns the newly created thread local storage identifier or 0 on error.

## Remarks

This creates an identifier that is globally visible to all threads but
refers to data that is thread-specific.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTLS](SDL_GetTLS)
* [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI)

