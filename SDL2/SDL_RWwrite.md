###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWwrite

Write to an [SDL_RWops](SDL_RWops) data stream.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
size_t SDL_RWwrite(SDL_RWops *context,
                   const void *ptr, size_t size,
                   size_t num);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure |
| **ptr**         | a pointer to a buffer containing data to write   |
| **size**        | the size of an object to write, in bytes         |
| **num**         | the number of objects to write                   |

## Return Value

Returns the number of objects written, which will be less than **num** on
error; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function writes exactly `num` objects each of size `size` from the
area pointed at by `ptr` to the stream. If this fails for any reason, it'll
return less than `num` to demonstrate how far the write progressed. On
success, it returns `num`.

[SDL_RWwrite](SDL_RWwrite) is actually a function wrapper that calls the
[SDL_RWops](SDL_RWops)'s `write` method appropriately, to simplify
application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## See Also

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromFP](SDL_RWFromFP)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWread](SDL_RWread)
* [SDL_RWseek](SDL_RWseek)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

