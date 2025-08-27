###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_LoadAudio_IO

Load audio for playback from an SDL_IOStream.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_LoadAudio_IO(MIX_Mixer *mixer, SDL_IOStream *io, bool predecode, bool closeio);
```

## Function Parameters

|                          |               |                                                                            |
| ------------------------ | ------------- | -------------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer**     | a mixer this audio is intended to be used with. May be NULL.               |
| SDL_IOStream *           | **io**        | the SDL_IOStream to load data from.                                        |
| bool                     | **predecode** | if true, data will be fully uncompressed before returning.                 |
| bool                     | **closeio**   | true if SDL_mixer should close `io` before returning (success or failure). |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns an audio object that can be used to make
sound on a mixer, or NULL on failure; call SDL_GetError() for more
information.

## Remarks

In normal usage, apps should load audio once, maybe at startup, then play
it multiple times.

When loading audio, it will be cached fully in RAM in its original data
format. Each time it plays, the data will be decoded. For example, an MP3
will be stored in memory in MP3 format and be decompressed on the fly
during playback. This is a tradeoff between i/o overhead and memory usage.

If `predecode` is true, the data will be decompressed during load and
stored as raw PCM data. This might dramatically increase loading time and
memory usage, but there will be no need to decompress data during playback.

(One could also use [MIX_SetTrackIOStream](MIX_SetTrackIOStream)() to
bypass loading the data into RAM upfront at all, but this offers still
different tradeoffs. The correct approach depends on the app's needs and
employing different approaches in different situations can make sense.)

[MIX_Audio](MIX_Audio) objects can be shared between mixers. This function
takes a [MIX_Mixer](MIX_Mixer), to imply this is the most likely place it
will be used and loading should try to match its audio format, but the
resulting audio can be used elsewhere. If `mixer` is NULL, SDL_mixer will
set reasonable defaults.

Once a [MIX_Audio](MIX_Audio) is created, it can be assigned to a
[MIX_Track](MIX_Track) with [MIX_SetTrackAudio](MIX_SetTrackAudio)(), or
played without any management with [MIX_PlayAudio](MIX_PlayAudio)().

When done with a [MIX_Audio](MIX_Audio), it can be freed with
[MIX_DestroyAudio](MIX_DestroyAudio)().

This function loads data from an SDL_IOStream. There is also a version that
loads from a path on the filesystem ([MIX_LoadAudio](MIX_LoadAudio)()), and
one that accepts properties for ultimate control
([MIX_LoadAudioWithProperties](MIX_LoadAudioWithProperties)()).

The SDL_IOStream provided must be able to seek, or loading will fail. If
the stream can't seek (data is coming from an HTTP connection, etc),
consider caching the data to memory or disk first and creating a new stream
to read from there.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyAudio](MIX_DestroyAudio)
- [MIX_SetTrackAudio](MIX_SetTrackAudio)
- [MIX_LoadAudio](MIX_LoadAudio)
- [MIX_LoadAudioWithProperties](MIX_LoadAudioWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

