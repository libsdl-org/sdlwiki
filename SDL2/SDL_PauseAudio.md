###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_PauseAudio

This function is a legacy means of pausing the audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_PauseAudio(int pause_on);

```

## Function Parameters

|                  |                                 |
| ---------------- | ------------------------------- |
| **pause_on**     | non-zero to pause, 0 to unpause |

## Remarks

New programs might want to use
[SDL_PauseAudioDevice](SDL_PauseAudioDevice)() instead. This function is
equivalent to calling...

```c
SDL_PauseAudioDevice(1, pause_on);
```

...and is only useful if you used the legacy
[SDL_OpenAudio](SDL_OpenAudio)() function.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetAudioStatus](SDL_GetAudioStatus)
- [SDL_PauseAudioDevice](SDL_PauseAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

