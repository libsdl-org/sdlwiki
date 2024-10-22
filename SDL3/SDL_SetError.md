###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetError

Set the SDL error message for the current thread.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
bool SDL_SetError(const char *fmt, ...);
```

## Function Parameters

|              |         |                                                                      |
| ------------ | ------- | -------------------------------------------------------------------- |
| const char * | **fmt** | a printf()-style message format string.                              |
| ...          | **...** | additional parameters matching % tokens in the `fmt` string, if any. |

## Return Value

(bool) Returns false.

## Remarks

Calling this function will replace any previous error message that was set.

This function always returns false, since SDL frequently uses false to
signify a failing result, leading to this idiom:

```c
if (error_code) {
    return SDL_SetError("This operation has failed: %d", error_code);
}
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ClearError](SDL_ClearError)
- [SDL_GetError](SDL_GetError)
- [SDL_SetErrorV](SDL_SetErrorV)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

