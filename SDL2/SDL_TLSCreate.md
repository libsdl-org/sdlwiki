###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TLSCreate

Create a piece of thread-local storage.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_thread.h)

## Syntax

```c
SDL_TLSID SDL_TLSCreate(void);

```

## Return Value

Returns the newly created thread local storage identifier or 0 on error.

## Remarks

This creates an identifier that is globally visible to all threads but
refers to data that is thread-specific.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_TLSGet](SDL_TLSGet)
- [SDL_TLSSet](SDL_TLSSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

