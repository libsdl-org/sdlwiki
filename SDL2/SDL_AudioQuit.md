###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioQuit

Use this function to shut down audio if you initialized it with [SDL_AudioInit](SDL_AudioInit)().

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_AudioQuit(void);

```

## Remarks

This function is used internally, and should not be used unless you have a
specific need to specify the audio driver you want to use. You should
normally use [SDL_Quit](SDL_Quit)() or
[SDL_QuitSubSystem](SDL_QuitSubSystem)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AudioInit](SDL_AudioInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

