###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadWAV_RW

Load the audio data of a WAVE file into memory.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
SDL_AudioSpec* SDL_LoadWAV_RW(SDL_RWops * src,
                              int freesrc,
                              SDL_AudioSpec * spec,
                              Uint8 ** audio_buf,
                              Uint32 * audio_len);

```

## Function Parameters

|                   |                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------- |
| **src**           | The data source for the WAVE data                                                            |
| **freesrc**       | If non-zero, SDL will _always_ free the data source                                          |
| **spec**          | An [SDL_AudioSpec](SDL_AudioSpec) that will be filled in with the wave file's format details |
| **audio_buf**     | A pointer filled with the audio data, allocated by the function.                             |
| **audio_len**     | A pointer filled with the length of the audio data buffer in bytes                           |

## Return Value

Returns This function, if successfully called, returns `spec`, which will
be filled with the audio data format of the wave source data. `audio_buf`
will be filled with a pointer to an allocated buffer containing the audio
data, and `audio_len` is filled with the length of that audio buffer in
bytes.

This function returns NULL if the .WAV file cannot be opened, uses an
unknown data format, or is corrupt; call [SDL_GetError](SDL_GetError)() for
more information.

When the application is done with the data returned in `audio_buf`, it
should call [SDL_FreeWAV](SDL_FreeWAV)() to dispose of it.

## Remarks

Loading a WAVE file requires `src`, `spec`, `audio_buf` and `audio_len` to
be valid pointers. The entire data portion of the file is then loaded into
memory and decoded if necessary.

If `freesrc` is non-zero, the data source gets automatically closed and
freed before the function returns.

Supported formats are RIFF WAVE files with the formats PCM (8, 16, 24, and
32 bits), IEEE Float (32 bits), Microsoft ADPCM and IMA ADPCM (4 bits), and
A-law and mu-law (8 bits). Other formats are currently unsupported and
cause an error.

If this function succeeds, the pointer returned by it is equal to `spec`
and the pointer to the audio data allocated by the function is written to
`audio_buf` and its length in bytes to `audio_len`. The
[SDL_AudioSpec](SDL_AudioSpec) members `freq`, `channels`, and `format` are
set to the values of the audio data in the buffer. The `samples` member is
set to a sane default and all others are set to zero.

It's necessary to use [SDL_FreeWAV](SDL_FreeWAV)() to free the audio data
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
SDL_LoadWAV_RW(SDL_RWFromFile("sample.wav", "rb"), 1, &spec, &buf, &len);
```

Note that the [SDL_LoadWAV](SDL_LoadWAV) macro does this same thing for
you, but in a less messy way:

```c
SDL_LoadWAV("sample.wav", &spec, &buf, &len);
```

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_FreeWAV](SDL_FreeWAV)
- [SDL_LoadWAV](SDL_LoadWAV)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

