###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetErrorV

Set the SDL error message for the current thread.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
bool SDL_SetErrorV(const char *fmt, va_list ap);
```

## Function Parameters

|              |         |                                         |
| ------------ | ------- | --------------------------------------- |
| const char * | **fmt** | a printf()-style message format string. |
| va_list      | **ap**  | a variable argument list.               |

## Return Value

(bool) Returns false.

## Remarks

Calling this function will replace any previous error message that was set.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.4.

## See Also

- [SDL_ClearError](SDL_ClearError)
- [SDL_GetError](SDL_GetError)
- [SDL_SetError](SDL_SetError)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

