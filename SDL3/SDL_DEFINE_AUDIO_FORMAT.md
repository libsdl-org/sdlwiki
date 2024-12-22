###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DEFINE_AUDIO_FORMAT

Define an [SDL_AudioFormat](SDL_AudioFormat) value.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
#define SDL_DEFINE_AUDIO_FORMAT(signed, bigendian, flt, size) \
    (((Uint16)(signed) << 15) | ((Uint16)(bigendian) << 12) | ((Uint16)(flt) << 8) | ((size) & SDL_AUDIO_MASK_BITSIZE))
```

## Macro Parameters

|               |                                                |
| ------------- | ---------------------------------------------- |
| **signed**    | 1 for signed data, 0 for unsigned data.        |
| **bigendian** | 1 for bigendian data, 0 for littleendian data. |
| **flt**       | 1 for floating point data, 0 for integer data. |
| **size**      | number of bits per sample.                     |

## Return Value

Returns a format value in the style of [SDL_AudioFormat](SDL_AudioFormat).

## Remarks

SDL does not support custom audio formats, so this macro is not of much use
externally, but it can be illustrative as to what the various bits of an
[SDL_AudioFormat](SDL_AudioFormat) mean.

For example, [SDL_AUDIO_S32LE](SDL_AUDIO_S32LE) looks like this:

```c
SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 32)
```

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAudio](CategoryAudio)

