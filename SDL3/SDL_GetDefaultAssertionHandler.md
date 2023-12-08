###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAssertionHandler](SDL_GetAssertionHandler.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAssertions](CategoryAssertions.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
