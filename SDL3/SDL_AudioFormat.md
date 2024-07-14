###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioFormat

Audio format.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef enum SDL_AudioFormat
{
    SDL_AUDIO_U8        = 0x0008u,  /**< Unsigned 8-bit samples */
        /* SDL_DEFINE_AUDIO_FORMAT(0, 0, 0, 8), */
    SDL_AUDIO_S8        = 0x8008u,  /**< Signed 8-bit samples */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 8), */
    SDL_AUDIO_S16LE     = 0x8010u,  /**< Signed 16-bit samples */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 16), */
    SDL_AUDIO_S16BE     = 0x9010u,  /**< As above, but big-endian byte order */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 0, 16), */
    SDL_AUDIO_S32LE     = 0x8020u,  /**< 32-bit integer samples */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 32), */
    SDL_AUDIO_S32BE     = 0x9020u,  /**< As above, but big-endian byte order */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 0, 32), */
    SDL_AUDIO_F32LE     = 0x8120u,  /**< 32-bit floating point samples */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 1, 32), */
    SDL_AUDIO_F32BE     = 0x9120u,  /**< As above, but big-endian byte order */
        /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 1, 32), */
} SDL_AudioFormat;
```

## Version

This enum is available since SDL 3.0.0.

## See Also

- [SDL_AUDIO_BITSIZE](SDL_AUDIO_BITSIZE)
- [SDL_AUDIO_BYTESIZE](SDL_AUDIO_BYTESIZE)
- [SDL_AUDIO_ISINT](SDL_AUDIO_ISINT)
- [SDL_AUDIO_ISFLOAT](SDL_AUDIO_ISFLOAT)
- [SDL_AUDIO_ISBIGENDIAN](SDL_AUDIO_ISBIGENDIAN)
- [SDL_AUDIO_ISLITTLEENDIAN](SDL_AUDIO_ISLITTLEENDIAN)
- [SDL_AUDIO_ISSIGNED](SDL_AUDIO_ISSIGNED)
- [SDL_AUDIO_ISUNSIGNED](SDL_AUDIO_ISUNSIGNED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryAudio](CategoryAudio), [CategoryAPIDatatype](CategoryAPIDatatype), 


