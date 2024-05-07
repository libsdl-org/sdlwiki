###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CloseAudio

This function is a legacy means of closing the audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

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
[SDL_OpenAudio](SDL_OpenAudio)() function.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_OpenAudio](SDL_OpenAudio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

