###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_LoadAudioNoCopy

Load audio for playback from a memory buffer without making a copy.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_LoadAudioNoCopy(MIX_Mixer *mixer, const void *data, size_t datalen, bool free_when_done);
```

## Function Parameters

|                          |                    |                                                                                           |
| ------------------------ | ------------------ | ----------------------------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer**          | a mixer this audio is intended to be used with. May be NULL.                              |
| const void *             | **data**           | the buffer where the audio data lives.                                                    |
| size_t                   | **datalen**        | the size, in bytes, of the buffer.                                                        |
| bool                     | **free_when_done** | if true, `data` will be given to SDL_free() when the [MIX_Audio](MIX_Audio) is destroyed. |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns an audio object that can be used to make
sound on a mixer, or NULL on failure; call SDL_GetError() for more
information.

## Remarks

When loading audio through most other LoadAudio functions, the data will be
cached fully in RAM in its original data format, for decoding on-demand.
This function does most of the same work as those functions, but instead
uses a buffer of memory provided by the app that it does not make a copy
of.

This buffer must live for the entire time the returned
[MIX_Audio](MIX_Audio) lives, as the mixer will access the buffer whenever
it needs to mix more data.

This function is meant to maximize efficiency: if the data is already in
memory and can remain there, don't copy it. This data can be in any
supported audio file format (WAV, MP3, etc); it will be decoded on the fly
while mixing. Unlike [MIX_LoadAudio](MIX_LoadAudio)(), there is no
`predecode` option offered here, as this is meant to optimize for data
that's already in memory and intends to exist there for significant time;
since predecoding would only need the file format data once, upfront, one
could simply wrap it in SDL_CreateIOFromConstMem() and pass that to
[MIX_LoadAudio_IO](MIX_LoadAudio_IO)().

[MIX_Audio](MIX_Audio) objects can be shared between multiple mixers. The
`mixer` parameter just suggests the most likely mixer to use this audio, in
case some optimization might be applied, but this is not required, and a
NULL mixer may be specified.

If `free_when_done` is true, SDL_mixer will call `SDL_free(data)` when the
returned [MIX_Audio](MIX_Audio) is eventually destroyed. This can be useful
when the data is not static, but rather loaded elsewhere for this specific
[MIX_Audio](MIX_Audio) and simply wants to avoid the extra copy.

As audio format information is obtained from the file format metadata, this
isn't useful for raw PCM data; in that case, use
[MIX_LoadRawAudioNoCopy](MIX_LoadRawAudioNoCopy)() instead, which offers an
SDL_AudioSpec.

Once a [MIX_Audio](MIX_Audio) is created, it can be assigned to a
[MIX_Track](MIX_Track) with [MIX_SetTrackAudio](MIX_SetTrackAudio)(), or
played without any management with [MIX_PlayAudio](MIX_PlayAudio)().

When done with a [MIX_Audio](MIX_Audio), it can be freed with
[MIX_DestroyAudio](MIX_DestroyAudio)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyAudio](MIX_DestroyAudio)
- [MIX_SetTrackAudio](MIX_SetTrackAudio)
- [MIX_LoadRawAudioNoCopy](MIX_LoadRawAudioNoCopy)
- [MIX_LoadAudio_IO](MIX_LoadAudio_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

