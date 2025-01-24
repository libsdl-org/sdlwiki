# SDL_AudioSpec

Format specifier for audio data.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef struct SDL_AudioSpec
{
    SDL_AudioFormat format;     /**< Audio data format */
    int channels;               /**< Number of channels: 1 mono, 2 stereo, etc */
    int freq;                   /**< sample rate: sample frames per second */
} SDL_AudioSpec;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_AudioFormat](SDL_AudioFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryAudio](CategoryAudio)

