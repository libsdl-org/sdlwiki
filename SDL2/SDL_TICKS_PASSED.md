###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TICKS_PASSED

Compare 32-bit SDL ticks values, and return true if `A` has passed `B`.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
#define SDL_TICKS_PASSED(A, B)  ((Sint32)((B) - (A)) <= 0)
```

## Remarks

This should be used with results from [SDL_GetTicks](SDL_GetTicks)(), as
this macro attempts to deal with the 32-bit counter wrapping back to zero
every ~49 days, but should _not_ be used with
[SDL_GetTicks64](SDL_GetTicks64)(), which does not have that problem.

For example, with [SDL_GetTicks](SDL_GetTicks)(), if you want to wait 100
ms, you could do this:

```c
const Uint32 timeout = SDL_GetTicks() + 100;
while (!SDL_TICKS_PASSED(SDL_GetTicks(), timeout)) {
    // ... do work until timeout has elapsed
}
```

Note that this does not handle tick differences greater than 2^31 so take
care when using the above kind of code with large timeout delays (tens of
days).

## Code Examples

```c++
/* if you want to wait 100 ms, you could do this: */
Uint32 timeout = SDL_GetTicks() + 100;
while (!SDL_TICKS_PASSED(SDL_GetTicks(), timeout)) {
    /* ... do work until timeout has elapsed */
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryTimer](CategoryTimer)


