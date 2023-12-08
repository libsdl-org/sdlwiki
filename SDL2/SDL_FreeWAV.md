###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeWAV

Free data previously allocated with [SDL_LoadWAV](SDL_LoadWAV.md)() or [SDL_LoadWAV_RW](SDL_LoadWAV_RW.md)().

## Syntax

```c
void SDL_FreeWAV(Uint8 * audio_buf);

```

## Function Parameters

|                   |                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| **audio_buf**     | a pointer to the buffer created by [SDL_LoadWAV](SDL_LoadWAV.md)() or [SDL_LoadWAV_RW](SDL_LoadWAV_RW.md)() |

## Remarks

After a WAVE file has been opened with [SDL_LoadWAV](SDL_LoadWAV.md)() or
[SDL_LoadWAV_RW](SDL_LoadWAV_RW.md)() its data can eventually be freed with
[SDL_FreeWAV](SDL_FreeWAV.md)(). It is safe to call this function with a NULL
pointer.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadWAV](SDL_LoadWAV.md)
* [SDL_LoadWAV_RW](SDL_LoadWAV_RW.md)

----
[CategoryAPI](CategoryAPI.md)
