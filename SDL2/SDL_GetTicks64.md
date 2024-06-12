###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTicks64

Get the number of milliseconds since SDL library initialization.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
Uint64 SDL_GetTicks64(void);
```

## Return Value

(Uint64) Returns an unsigned 64-bit value representing the number of
milliseconds since the SDL library initialized.

## Remarks

Note that you should not use the [SDL_TICKS_PASSED](SDL_TICKS_PASSED) macro
with values returned by this function, as that macro does clever math to
compensate for the 32-bit overflow every ~49 days that
[SDL_GetTicks](SDL_GetTicks)() suffers from. 64-bit values from this
function can be safely compared directly.

For example, if you want to wait 100 ms, you could do this:

```c
const Uint64 timeout = SDL_GetTicks64() + 100;
while (SDL_GetTicks64() < timeout) {
    // ... do work until timeout has elapsed
}
```

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

