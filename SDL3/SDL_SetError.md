###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetError

Set the SDL error message for the current thread.

## Header File

Defined in [SDL_error.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_SetError(SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(1);

```

## Function Parameters

|             |                                                                     |
| ----------- | ------------------------------------------------------------------- |
| **fmt**     | a printf()-style message format string                              |
| **...**     | additional parameters matching % tokens in the `fmt` string, if any |

## Return Value

Returns always -1.

## Remarks

Calling this function will replace any previous error message that was set.

This function always returns -1, since SDL frequently uses -1 to signify an
failing result, leading to this idiom:

```c
if (error_code) {
    return SDL_SetError("This operation has failed: %d", error_code);
}
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_SetError("Something unexpected happened!");
```
```c++
int errorCode = 0;
...
errorCode = -37;
...
if (errorCode < 0)
    SDL_SetError("Something unexpected happened: Error Code %d", errorCode);
```

## See Also

* [SDL_ClearError](SDL_ClearError)
* [SDL_GetError](SDL_GetError)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)


