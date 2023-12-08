###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ConvertAudio

Convert audio data to a desired audio format.

## Syntax

```c
int SDL_ConvertAudio(SDL_AudioCVT * cvt);

```

## Function Parameters

|             |                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| **cvt**     | an [SDL_AudioCVT](SDL_AudioCVT.md) structure that was previously set up by [SDL_BuildAudioCVT](SDL_BuildAudioCVT.md)(). |

## Return Value

Returns 0 if the conversion was completed successfully or a negative error
code on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function does the actual audio data conversion, after the application
has called [SDL_BuildAudioCVT](SDL_BuildAudioCVT.md)() to prepare the
conversion information and then filled in the buffer details.

Once the application has initialized the `cvt` structure using
[SDL_BuildAudioCVT](SDL_BuildAudioCVT.md)(), allocated an audio buffer and
filled it with audio data in the source format, this function will convert
the buffer, in-place, to the desired format.

The data conversion may go through several passes; any given pass may
possibly temporarily increase the size of the data. For example, SDL might
expand 16-bit data to 32 bits before resampling to a lower frequency,
shrinking the data size after having grown it briefly. Since the supplied
buffer will be both the source and destination, converting as necessary
in-place, the application must allocate a buffer that will fully contain
the data during its largest conversion pass. After
[SDL_BuildAudioCVT](SDL_BuildAudioCVT.md)() returns, the application should
set the `cvt->len` field to the size, in bytes, of the source data, and
allocate a buffer that is `cvt->len * cvt->len_mult` bytes long for the
`buf` field.

The source data should be copied into this buffer before the call to
[SDL_ConvertAudio](SDL_ConvertAudio.md)(). Upon successful return, this buffer
will contain the converted audio, and `cvt->len_cvt` will be the size of
the converted data, in bytes. Any bytes in the buffer past `cvt->len_cvt`
are undefined once this function returns.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BuildAudioCVT](SDL_BuildAudioCVT.md)

----
[CategoryAPI](CategoryAPI.md)
