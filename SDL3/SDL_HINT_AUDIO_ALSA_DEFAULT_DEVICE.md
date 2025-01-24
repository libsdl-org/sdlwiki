# SDL_HINT_AUDIO_ALSA_DEFAULT_DEVICE

Specify the default ALSA audio device name.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_ALSA_DEFAULT_DEVICE "SDL_AUDIO_ALSA_DEFAULT_DEVICE"
```

## Remarks

This variable is a specific audio device to open when the "default" audio
device is used.

This hint will be ignored when opening the default playback device if
[SDL_HINT_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE](SDL_HINT_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE)
is set, or when opening the default recording device if
[SDL_HINT_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE](SDL_HINT_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE)
is set.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.2.0.

## See Also

- [SDL_HINT_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE](SDL_HINT_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE)
- [SDL_HINT_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE](SDL_HINT_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

