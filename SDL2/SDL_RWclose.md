###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWclose

Close and free an allocated [SDL_RWops](SDL_RWops.md) structure.

## Syntax

```c
int SDL_RWclose(SDL_RWops *context);

```

## Function Parameters

|                 |                                           |
| --------------- | ----------------------------------------- |
| **context**     | [SDL_RWops](SDL_RWops.md) structure to close |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

[SDL_RWclose](SDL_RWclose.md)() closes and cleans up the
[SDL_RWops](SDL_RWops.md) stream. It releases any resources used by the stream
and frees the [SDL_RWops](SDL_RWops.md) itself with
[SDL_FreeRW](SDL_FreeRW.md)(). This returns 0 on success, or -1 if the stream
failed to flush to its output (e.g. to disk).

Note that if this fails to flush the stream to disk, this function reports
an error, but the [SDL_RWops](SDL_RWops.md) is still invalid once this
function returns.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## Related Functions

* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromFP](SDL_RWFromFP.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md)
