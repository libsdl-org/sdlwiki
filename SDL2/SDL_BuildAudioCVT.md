###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_BuildAudioCVT

Initialize an [SDL_AudioCVT](SDL_AudioCVT.md) structure for conversion.

## Syntax

```c
int SDL_BuildAudioCVT(SDL_AudioCVT * cvt,
                      SDL_AudioFormat src_format,
                      Uint8 src_channels,
                      int src_rate,
                      SDL_AudioFormat dst_format,
                      Uint8 dst_channels,
                      int dst_rate);

```

## Function Parameters

|                      |                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **cvt**              | an [SDL_AudioCVT](SDL_AudioCVT.md) structure filled in with audio conversion information          |
| **src_format**       | the source format of the audio data; for more info see [SDL_AudioFormat](SDL_AudioFormat.md)      |
| **src_channels**     | the number of channels in the source                                                           |
| **src_rate**         | the frequency (sample-frames-per-second) of the source                                         |
| **dst_format**       | the destination format of the audio data; for more info see [SDL_AudioFormat](SDL_AudioFormat.md) |
| **dst_channels**     | the number of channels in the destination                                                      |
| **dst_rate**         | the frequency (sample-frames-per-second) of the destination                                    |

## Return Value

Returns 1 if the audio filter is prepared, 0 if no conversion is needed, or
a negative error code on failure; call [SDL_GetError](SDL_GetError.md)() for
more information.

## Remarks

Before an [SDL_AudioCVT](SDL_AudioCVT.md) structure can be used to convert
audio data it must be initialized with source and destination information.

This function will zero out every field of the
[SDL_AudioCVT](SDL_AudioCVT.md), so it must be called before the application
fills in the final buffer information.

Once this function has returned successfully, and reported that a
conversion is necessary, the application fills in the rest of the fields in
[SDL_AudioCVT](SDL_AudioCVT.md), now that it knows how large a buffer it needs
to allocate, and then can call [SDL_ConvertAudio](SDL_ConvertAudio.md)() to
complete the conversion.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_ConvertAudio](SDL_ConvertAudio.md)

----
[CategoryAPI](CategoryAPI.md)
