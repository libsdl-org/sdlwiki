###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTicks

Get the number of milliseconds since SDL library initialization.

## Syntax

```c
Uint32 SDL_GetTicks(void);

```

## Return Value

Returns an unsigned 32-bit value representing the number of milliseconds
since the SDL library initialized.

## Remarks

This value wraps if the program runs for more than ~49 days.

This function is not recommended as of SDL 2.0.18; use
[SDL_GetTicks64](SDL_GetTicks64.md)() instead, where the value doesn't wrap
every ~49 days. There are places in SDL where we provide a 32-bit timestamp
that can not change without breaking binary compatibility, though, so this
function isn't officially deprecated.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_TICKS_PASSED](SDL_TICKS_PASSED.md)

----
[CategoryAPI](CategoryAPI.md)
