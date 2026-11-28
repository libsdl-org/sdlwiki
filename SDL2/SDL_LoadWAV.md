# SDL_LoadWAV

Loads a WAV from a file.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
#define SDL_LoadWAV(file, spec, audio_buf, audio_len) \
    SDL_LoadWAV_RW(SDL_RWFromFile(file, "rb"),1, spec,audio_buf,audio_len)
```

## Remarks

This is designed as a convenience function for loading audio from trusted
sources. Crashes or other issues with invalid content should not be
considered security issues. If you want to load arbitrary audio you should
use an audio loading library designed with security in mind.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

