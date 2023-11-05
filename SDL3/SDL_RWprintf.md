###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWprintf

Print to an [SDL_RWops](SDL_RWops) data stream.

## Syntax

```c
size_t SDL_RWprintf(SDL_RWops *context, SDL_PRINTF_FORMAT_STRING const char *fmt, ...)  SDL_PRINTF_VARARG_FUNC(2);

```

## Function Parameters

|                 |                                                                     |
| --------------- | ------------------------------------------------------------------- |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure                    |
| **fmt**         | a printf() style format string                                      |
| **...**         | additional parameters matching % tokens in the `fmt` string, if any |

## Return Value

Returns the number of bytes written, or 0 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function does formatted printing to the stream.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWread](SDL_RWread)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI)

