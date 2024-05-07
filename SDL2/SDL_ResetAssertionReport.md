###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ResetAssertionReport

Clear the list of all assertion failures.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_assert.h)

## Syntax

```c
void SDL_ResetAssertionReport(void);

```

## Remarks

This function will clear the list of all assertions triggered up to that
point. Immediately following this call,
[SDL_GetAssertionReport](SDL_GetAssertionReport) will return no items. In
addition, any previously-triggered assertions will be reset to a
trigger_count of zero, and their always_ignore state will be false.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetAssertionReport](SDL_GetAssertionReport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

