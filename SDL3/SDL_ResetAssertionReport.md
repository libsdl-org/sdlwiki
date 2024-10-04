###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ResetAssertionReport

Clear the list of all assertion failures.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

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

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAssertionReport](SDL_GetAssertionReport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAssert](CategoryAssert)

