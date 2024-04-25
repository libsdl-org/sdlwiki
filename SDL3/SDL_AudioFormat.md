###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioFormat

Audio format flags.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef Uint16 SDL_AudioFormat;
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

