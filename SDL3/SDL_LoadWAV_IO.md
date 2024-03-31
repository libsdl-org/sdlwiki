###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadWAV_IO

Load the audio data of a WAVE file into memory.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_LoadWAV_IO(SDL_IOStream * src, SDL_bool closeio,
                   SDL_AudioSpec * spec, Uint8 ** audio_buf,
                   Uint32 * audio_len);

```

## Function Parameters

|                   |                                                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **src**           | The data source for the WAVE data                                                                                      |
| **closeio**       | If [SDL_TRUE](SDL_TRUE), calls [SDL_CloseIO](SDL_CloseIO)() on `src` before returning, even in the case of an error    |
| **spec**          | A pointer to an [SDL_AudioSpec](SDL_AudioSpec) that will be set to the WAVE data's format details on successful return |
| **audio_buf**     | A pointer filled with the audio data, allocated by the function                                                        |
| **audio_len**     | A pointer filled with the length of the audio data buffer in bytes                                                     |

## Return Value

Returns This function, if successfully called, returns 0. `audio_buf` will
be filled with a pointer to an allocated buffer containing the audio data,
and `audio_len` is filled with the length of that audio buffer in bytes.

This function returns -1 if the .WAV file cannot be opened, uses an unknown
data format, or is corrupt; call [SDL_GetError](SDL_GetError)() for more
information.

When the application is done with the data returned in `audio_buf`, it
should call [SDL_free](SDL_free)() to dispose of it.

## Remarks

Loading a WAVE file requires `src`, `spec`, `audio_buf` and `audio_len` to
be valid pointers. The entire data portion of the file is then loaded into
memory and decoded if necessary.

Supported formats are RIFF WAVE files with the formats PCM (8, 16, 24, and
32 bits), IEEE Float (32 bits), Microsoft ADPCM and IMA ADPCM (4 bits), and
A-law and mu-law (8 bits). Other formats are currently unsupported and
cause an error.

If this function succeeds, the return value is zero and the pointer to the
audio data allocated by the function is written to `audio_buf` and its
length in bytes to `audio_len`. The [SDL_AudioSpec](SDL_AudioSpec) members
`freq`, `channels`, and `format` are set to the values of the audio data in
the buffer.

It's necessary to use [SDL_free](SDL_free)() to free the audio data
returned in `audio_buf` when it is no longer used.

Because of the underspecification of the .WAV format, there are many
problematic files in the wild that cause issues with strict decoders. To
provide compatibility with these files, this decoder is lenient in regards
to the truncation of the file, the fact chunk, and the size of the RIFF
chunk. The hints
[`SDL_HINT_WAVE_RIFF_CHUNK_SIZE`](SDL_HINT_WAVE_RIFF_CHUNK_SIZE),
[`SDL_HINT_WAVE_TRUNCATION`](SDL_HINT_WAVE_TRUNCATION), and
[`SDL_HINT_WAVE_FACT_CHUNK`](SDL_HINT_WAVE_FACT_CHUNK) can be used to tune
the behavior of the loading process.

Any file that is invalid (due to truncation, corruption, or wrong values in
the headers), too big, or unsupported causes an error. Additionally, any
critical I/O error from the data source will terminate the loading process
with an error. The function returns NULL on error and in all cases (with
the exception of `src` being NULL), an appropriate error message will be
set.

It is required that the data source supports seeking.

Example:

```c
SDL_LoadWAV_IO(SDL_IOFromFile("sample.wav", "rb"), 1, &spec, &buf, &len);
```

Note that the [SDL_LoadWAV](SDL_LoadWAV) function does this same thing for
you, but in a less messy way:

```c
SDL_LoadWAV("sample.wav", &spec, &buf, &len);
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_free](SDL_free)
* [SDL_LoadWAV](SDL_LoadWAV)

----
[CategoryAPI](CategoryAPI)

