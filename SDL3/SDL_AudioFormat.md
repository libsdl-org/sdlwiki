###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioFormat

Audio format flags.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef Uint16 SDL_AudioFormat;

#define SDL_AUDIO_U8        0x0008  /**< Unsigned 8-bit samples */
#define SDL_AUDIO_S8        0x8008  /**< Signed 8-bit samples */

#define SDL_AUDIO_S16LE     0x8010  /**< Signed 16-bit samples */
#define SDL_AUDIO_S16BE     0x9010  /**< As above, but big-endian byte order */

#define SDL_AUDIO_S32LE     0x8020  /**< 32-bit integer samples */
#define SDL_AUDIO_S32BE     0x9020  /**< As above, but big-endian byte order */

#define SDL_AUDIO_F32LE     0x8120  /**< 32-bit floating point samples */
#define SDL_AUDIO_F32BE     0x9120  /**< As above, but big-endian byte order */

#if SDL_BYTEORDER == SDL_LIL_ENDIAN
#define SDL_AUDIO_S16    SDL_AUDIO_S16LE
#define SDL_AUDIO_S32    SDL_AUDIO_S32LE
#define SDL_AUDIO_F32    SDL_AUDIO_F32LE
#else
#define SDL_AUDIO_S16    SDL_AUDIO_S16BE
#define SDL_AUDIO_S32    SDL_AUDIO_S32BE
#define SDL_AUDIO_F32    SDL_AUDIO_F32BE
```

## Remarks

These are what the 16 bits in [SDL_AudioFormat](SDL_AudioFormat) currently
mean... (Unspecified bits are always zero).

```
++-----------------------sample is signed if set
||
||       ++-----------sample is bigendian if set
||       ||
||       ||          ++---sample is float if set
||       ||          ||
||       ||          || +=--sample bit size--++
||       ||          || ||                   ||
15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00
```

There are macros to query these bits.

## Version

This datatype is available since SDL 3.0.0.

## See Also

* [SDL_AUDIO_BITSIZE](SDL_AUDIO_BITSIZE)
* [SDL_AUDIO_BYTESIZE](SDL_AUDIO_BYTESIZE)
* [SDL_AUDIO_ISINT](SDL_AUDIO_ISINT)
* [SDL_AUDIO_ISFLOAT](SDL_AUDIO_ISFLOAT)
* [SDL_AUDIO_ISBIGENDIAN](SDL_AUDIO_ISBIGENDIAN)
* [SDL_AUDIO_ISLITTLEENDIAN](SDL_AUDIO_ISLITTLEENDIAN)
* [SDL_AUDIO_ISSIGNED](SDL_AUDIO_ISSIGNED)
* [SDL_AUDIO_ISUNSIGNED](SDL_AUDIO_ISUNSIGNED)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

