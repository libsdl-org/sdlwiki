###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackRawIOStream

Set a [MIX_Track](MIX_Track)'s input to an SDL_IOStream providing raw PCM data.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackRawIOStream(MIX_Track *track, SDL_IOStream *io, const SDL_AudioSpec *spec, bool closeio);
```

## Function Parameters

|                          |             |                                                                |
| ------------------------ | ----------- | -------------------------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**   | the track on which to set a new audio input.                   |
| SDL_IOStream *           | **io**      | the new i/o stream to use as the track's input.                |
| const SDL_AudioSpec *    | **spec**    | the format of the PCM data that the SDL_IOStream will provide. |
| bool                     | **closeio** | if true, close the stream when done with it.                   |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

This is not the recommended way to set a track's input, but this can be
useful for a very specific scenario: a large file, to be played once, that
must be read from disk in small chunks as needed. In most cases, however,
it is preferable to create a [MIX_Audio](MIX_Audio) ahead of time and use
[MIX_SetTrackAudio](MIX_SetTrackAudio)() instead.

Also, an [MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)() can _also_
provide raw PCM audio to a track, via an SDL_AudioStream, which might be
preferable unless the data is already coming directly from an SDL_IOStream.

The stream supplied here should provide an audio in raw PCM format.

A given IOStream may only be assigned to a single track at a time;
duplicate assignments won't return an error, but assigning a stream to
multiple tracks will cause each track to read from the stream arbitrarily,
causing confusion and incorrect mixing.

Once a track has a valid input, it can start mixing sound by calling
[MIX_PlayTrack](MIX_PlayTrack)(), or possibly [MIX_PlayTag](MIX_PlayTag)().

Calling this function with a NULL stream is legal, and removes any input
from the track. If the track was currently playing, the next time the mixer
runs, it'll notice this and mark the track as stopped, calling any assigned
[MIX_TrackStoppedCallback](MIX_TrackStoppedCallback).

It is legal to change the input of a track while it's playing, however some
states, like loop points, may cease to make sense with the new audio. In
such a case, one can call [MIX_PlayTrack](MIX_PlayTrack) again to adjust
parameters.

The provided stream must remain valid until the track no longer needs it
(either by changing the track's input or destroying the track).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)
- [MIX_SetTrackIOStream](MIX_SetTrackIOStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

