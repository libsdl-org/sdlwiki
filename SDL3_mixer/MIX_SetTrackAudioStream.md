###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackAudioStream

Set a [MIX_Track](MIX_Track)'s input to an SDL_AudioStream.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackAudioStream(MIX_Track *track, SDL_AudioStream *stream);
```

## Function Parameters

|                          |            |                                               |
| ------------------------ | ---------- | --------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**  | the track on which to set a new audio input.  |
| SDL_AudioStream *        | **stream** | the audio stream to use as the track's input. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

Using an audio stream allows the application to generate any type of audio,
in any format, possibly procedurally or on-demand, and mix in with all
other tracks.

When a track uses an audio stream, it will call SDL_GetAudioStreamData as
it needs more audio to mix. The app can either buffer data to the stream
ahead of time, or set a callback on the stream to provide data as needed.
Please refer to SDL's documentation for details.

A given audio stream may only be assigned to a single track at a time;
duplicate assignments won't return an error, but assigning a stream to
multiple tracks will cause each track to read from the stream arbitarily,
causing confusion and incorrect mixing.

Once a track has a valid input, it can start mixing sound by calling
[MIX_PlayTrack](MIX_PlayTrack)(), or possibly [MIX_PlayTag](MIX_PlayTag)().

Calling this function with a NULL audio stream is legal, and removes any
input from the track. If the track was currently playing, the next time the
mixer runs, it'll notice this and mark the track as stopped, calling any
assigned [MIX_TrackStoppedCallback](MIX_TrackStoppedCallback).

It is legal to change the input of a track while it's playing, however some
states, like loop points, may cease to make sense with the new audio. In
such a case, one can call [MIX_PlayTrack](MIX_PlayTrack) again to adjust
parameters.

The provided audio stream must remain valid until the track no longer needs
it (either by changing the track's input or destroying the track).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

