###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CloseAudio

This function is a legacy means of closing the audio device.

## Syntax

```c
void SDL_CloseAudio(void);

```

## Remarks

This function is equivalent to calling...

```c
SDL_CloseAudioDevice(1);
```

...and is only useful if you used the legacy
[SDL_OpenAudio](SDL_OpenAudio.md)() function.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_OpenAudio](SDL_OpenAudio.md)

----
[CategoryAPI](CategoryAPI.md)
