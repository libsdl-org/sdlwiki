###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AssertState

Possible outcomes from a triggered assertion.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_AssertState
{
    SDL_ASSERTION_RETRY,  /**< Retry the assert immediately. */
    SDL_ASSERTION_BREAK,  /**< Make the debugger trigger a breakpoint. */
    SDL_ASSERTION_ABORT,  /**< Terminate the program. */
    SDL_ASSERTION_IGNORE,  /**< Ignore the assert. */
    SDL_ASSERTION_ALWAYS_IGNORE  /**< Ignore the assert from now on. */
} SDL_AssertState;
```

## Remarks

When an enabled assertion triggers, it may call the assertion handler
(possibly one provided by the app via
[SDL_SetAssertionHandler](SDL_SetAssertionHandler)), which will return one
of these values, possibly after asking the user.

Then SDL will respond based on this outcome (loop around to retry the
condition, try to break in a debugger, kill the program, or ignore the
problem).

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

