###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ResetAssertionReport

Clear the list of all assertion failures.

## Syntax

```c
void SDL_ResetAssertionReport(void);

```

## Remarks

This function will clear the list of all assertions triggered up to that
point. Immediately following this call,
[SDL_GetAssertionReport](SDL_GetAssertionReport.md) will return no items. In
addition, any previously-triggered assertions will be reset to a
trigger_count of zero, and their always_ignore state will be false.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetAssertionReport](SDL_GetAssertionReport.md)

----
[CategoryAPI](CategoryAPI.md)
