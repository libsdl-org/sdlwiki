###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioQuit

Use this function to shut down audio if you initialized it with [SDL_AudioInit](SDL_AudioInit.md)().

## Syntax

```c
void SDL_AudioQuit(void);

```

## Remarks

This function is used internally, and should not be used unless you have a
specific need to specify the audio driver you want to use. You should
normally use [SDL_Quit](SDL_Quit.md)() or
[SDL_QuitSubSystem](SDL_QuitSubSystem.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AudioInit](SDL_AudioInit.md)

----
[CategoryAPI](CategoryAPI.md)
