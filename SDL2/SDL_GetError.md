###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetError

Retrieve a message about the last error that occurred on the current thread.

## Header File

Defined in [SDL_error.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_error.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
const char* SDL_GetError(void);

```

## Return Value

Returns a message with information about the specific error that occurred,
or an empty string if there hasn't been an error message set since the last
call to [SDL_ClearError](SDL_ClearError)(). The message is only applicable
when an SDL function has signaled an error. You must check the return
values of SDL function calls to determine when to appropriately call
[SDL_GetError](SDL_GetError)().

## Remarks

It is possible for multiple errors to occur before calling
[SDL_GetError](SDL_GetError)(). Only the last error is returned.

The message is only applicable when an SDL function has signaled an error.
You must check the return values of SDL function calls to determine when to
appropriately call [SDL_GetError](SDL_GetError)(). You should *not* use the
results of [SDL_GetError](SDL_GetError)() to decide if an error has
occurred! Sometimes SDL will set an error string even when reporting
success.

SDL will *not* clear the error string for successful API calls. You *must*
check return values for failure cases before you can assume the error
string applies.

Error strings are set per-thread, so an error set in a different thread
will not interfere with the current thread's operation.

The returned string is internally allocated and must not be freed by the
application.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_ClearError](SDL_ClearError)
* [SDL_SetError](SDL_SetError)

----
[CategoryAPI](CategoryAPI), [CategoryError](CategoryError)


