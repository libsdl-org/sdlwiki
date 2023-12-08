###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDefaultAssertionHandler

Get the default assertion handler.

## Syntax

```c
SDL_AssertionHandler SDL_GetDefaultAssertionHandler(void);

```

## Return Value

Returns the default [SDL_AssertionHandler](SDL_AssertionHandler.md) that is
called when an assert triggers.

## Remarks

This returns the function pointer that is called by default when an
assertion is triggered. This is an internal function provided by SDL, that
is used for assertions when
[SDL_SetAssertionHandler](SDL_SetAssertionHandler.md)() hasn't been used to
provide a different function.

## Version

This function is available since SDL 2.0.2.

## Related Functions

* [SDL_GetAssertionHandler](SDL_GetAssertionHandler.md)

----
[CategoryAPI](CategoryAPI.md)
