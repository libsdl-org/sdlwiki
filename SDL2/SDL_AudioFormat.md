# SDL_AudioFormat

Audio format flags.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

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
||       ||          || +---sample bit size---+
||       ||          || |                     |
15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00
```

There are macros in SDL 2.0 and later to query these bits.





----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

