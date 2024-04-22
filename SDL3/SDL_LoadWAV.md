###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadWAV

Loads a WAV from a file path.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_LoadWAV(const char *path, SDL_AudioSpec * spec,
                Uint8 ** audio_buf, Uint32 * audio_len);

```

## Function Parameters

|                   |                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **path**          | The file path of the WAV file to open.                                                                                  |
| **spec**          | A pointer to an [SDL_AudioSpec](SDL_AudioSpec) that will be set to the WAVE data's format details on successful return. |
| **audio_buf**     | A pointer filled with the audio data, allocated by the function.                                                        |
| **audio_len**     | A pointer filled with the length of the audio data buffer in bytes                                                      |

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

This is a convenience function that is effectively the same as:

```c
SDL_LoadWAV_IO(SDL_IOFromFile(path, "rb"), 1, spec, audio_buf, audio_len);
```

Note that in SDL2, this was a preprocessor macro and not a real function.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_free](SDL_free)
* [SDL_LoadWAV_IO](SDL_LoadWAV_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), CategoryAudio


