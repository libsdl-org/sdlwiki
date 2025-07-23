###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Track

An opaque object that represents a source of sound output to be mixed.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef struct MIX_Track MIX_Track;
```

## Remarks

A [MIX_Mixer](MIX_Mixer) has an arbitrary number of tracks, and each track
manages its own unique audio to be mixed together.

Tracks also have other properties: gain, loop points, fading, 3D position,
and other attributes that alter the produced sound; many can be altered
during playback.

## Version

This datatype is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLMixer](CategorySDLMixer)

