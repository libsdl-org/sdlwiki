###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_LoadRawAudioNoCopy

Load raw PCM data from a memory buffer without making a copy.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_LoadRawAudioNoCopy(MIX_Mixer *mixer, const void *data, size_t datalen, const SDL_AudioSpec *spec, bool free_when_done);
```

## Function Parameters

|                          |                    |                                                                                           |
| ------------------------ | ------------------ | ----------------------------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer**          | a mixer this audio is intended to be used with. May be NULL.                              |
| const void *             | **data**           | the buffer where the raw PCM data lives.                                                  |
| size_t                   | **datalen**        | the size, in bytes, of the buffer.                                                        |
| const SDL_AudioSpec *    | **spec**           | what format the raw data is in.                                                           |
| bool                     | **free_when_done** | if true, `data` will be given to SDL_free() when the [MIX_Audio](MIX_Audio) is destroyed. |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns an audio object that can be used to make
sound on a mixer, or NULL on failure; call SDL_GetError() for more
information.

## Remarks

This buffer must live for the entire time the returned
[MIX_Audio](MIX_Audio) lives, as it will access it whenever it needs to mix
more data.

This function is meant to maximize efficiency: if the data is already in
memory and can remain there, don't copy it. But it can also lead to some
interesting tricks, like changing the buffer's contents to alter multiple
playing tracks at once. (But, of course, be careful when being too clever.)

[MIX_Audio](MIX_Audio) objects can be shared between multiple mixers. The
`mixer` parameter just suggests the most likely mixer to use this audio, in
case some optimization might be applied, but this is not required, and a
NULL mixer may be specified.

If `free_when_done` is true, SDL_mixer will call `SDL_free(data)` when the
returned [MIX_Audio](MIX_Audio) is eventually destroyed. This can be useful
when the data is not static, but rather composed dynamically for this
specific [MIX_Audio](MIX_Audio) and simply wants to avoid the extra copy.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyAudio](MIX_DestroyAudio)
- [MIX_SetTrackAudio](MIX_SetTrackAudio)
- [MIX_LoadRawAudio](MIX_LoadRawAudio)
- [MIX_LoadRawAudio_IO](MIX_LoadRawAudio_IO)
- [MIX_LoadAudio_IO](MIX_LoadAudio_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

