###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

## Code Examples

```c++
extern SDL_AudioFormat fmt;
if (SDL_AUDIO_ISFLOAT(fmt)) {
    printf("floating point data\n");
} else {
    printf("integer data\n");
}
printf("%d bits per sample\n", (int) SDL_AUDIO_BITSIZE(fmt));
```

## Related Structures

[SDL_AudioCVT](SDL_AudioCVT)
[SDL_AudioSpec](SDL_AudioSpec)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryEnum](CategoryEnum), [CategoryAudio](CategoryAudio)


