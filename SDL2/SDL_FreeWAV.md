###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeWAV

Free data previously allocated with [SDL_LoadWAV](SDL_LoadWAV)() or [SDL_LoadWAV_RW](SDL_LoadWAV_RW)().

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_FreeWAV(Uint8 * audio_buf);

```

## Function Parameters

|                   |                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| **audio_buf**     | a pointer to the buffer created by [SDL_LoadWAV](SDL_LoadWAV)() or [SDL_LoadWAV_RW](SDL_LoadWAV_RW)() |

## Remarks

After a WAVE file has been opened with [SDL_LoadWAV](SDL_LoadWAV)() or
[SDL_LoadWAV_RW](SDL_LoadWAV_RW)() its data can eventually be freed with
[SDL_FreeWAV](SDL_FreeWAV)(). It is safe to call this function with a NULL
pointer.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_LoadWAV](SDL_LoadWAV)
* [SDL_LoadWAV_RW](SDL_LoadWAV_RW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

