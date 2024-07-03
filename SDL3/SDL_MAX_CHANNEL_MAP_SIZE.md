###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MAX_CHANNEL_MAP_SIZE

Maximum channels that an [SDL_AudioSpec](SDL_AudioSpec) channel map can handle.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_MAX_CHANNEL_MAP_SIZE 16
```

## Remarks

This is (currently) double the number of channels that SDL supports, to
allow for future expansion while maintaining binary compatibility.

## Version

This macro is available since SDL 3.0.0.

## See Also

- [SDL_AudioSpec](SDL_AudioSpec)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

