###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioDeviceID

SDL Audio Device IDs.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
typedef Uint32 SDL_AudioDeviceID;
```

## Remarks

A successful call to [SDL_OpenAudio](SDL_OpenAudio)() is always device id
1, and legacy SDL audio APIs assume you want this device ID.
[SDL_OpenAudioDevice](SDL_OpenAudioDevice)() calls always returns devices
>= 2 on success. The legacy calls are good both for backwards compatibility
and when you don't care about multiple, specific, or capture devices.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

