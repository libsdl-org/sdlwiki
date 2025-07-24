###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PlayTrack

Start (or restart) mixing a track for playback.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_PlayTrack(MIX_Track *track, SDL_PropertiesID options);
```

## Function Parameters

|                          |             |                                                         |
| ------------------------ | ----------- | ------------------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**   | the track to start (or restart) mixing.                 |
| SDL_PropertiesID         | **options** | a set of properties that control playback. May be zero. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

The track will use whatever input was last assigned to it when playing; an
input must be assigned to this track or this function will fail. Inputs are
assigned with calls to [MIX_SetTrackAudio](MIX_SetTrackAudio)(),
[MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)(), or
[MIX_SetTrackIOStream](MIX_SetTrackIOStream)().

If the track is already playing, or paused, this will restart the track
with the newly-specified parameters.

As there are several parameters, and more may be added in the future, they
are specified with an SDL_PropertiesID. The parameters have reasonable
defaults, and specifying a 0 for `options` will choose defaults for
everything.

These are the supported properties:

- [`MIX_PROP_PLAY_LOOPS_NUMBER`](MIX_PROP_PLAY_LOOPS_NUMBER): The number of
  times to loop the track when it reaches the end. A value of 1 will loop
  to the start one time. Zero will not loop at all. A value of -1 requests
  infinite loops. If the input is not seekable and this value isn't zero,
  this function will report success but the track will stop at the point it
  should loop. Default 0.
- [`MIX_PROP_PLAY_MAX_FRAME_NUMBER`](MIX_PROP_PLAY_MAX_FRAME_NUMBER): Mix
  at most to this sample frame position in the track. This will be treated
  as if the input reach EOF at this point in the audio file. If -1, mix all
  available audio without a limit. Default -1.
- [`MIX_PROP_PLAY_MAX_MILLISECONDS_NUMBER`](MIX_PROP_PLAY_MAX_MILLISECONDS_NUMBER):
  The same as using the
  [MIX_PROP_PLAY_MAX_FRAME_NUMBER](MIX_PROP_PLAY_MAX_FRAME_NUMBER)
  property, but the value is specified in milliseconds instead of sample
  frames. If both properties are specified, the sample frames value is
  favored. Default -1.
- [`MIX_PROP_PLAY_START_FRAME_NUMBER`](MIX_PROP_PLAY_START_FRAME_NUMBER):
  Start mixing from this sample frame position in the track's input. A
  value <= 0 will begin from the start of the track's input. If the input
  is not seekable and this value is > 0, this function will report failure.
  Default 0.
- [`MIX_PROP_PLAY_START_MILLISECOND_NUMBER`](MIX_PROP_PLAY_START_MILLISECOND_NUMBER):
  The same as using the
  [MIX_PROP_PLAY_START_FRAME_NUMBER](MIX_PROP_PLAY_START_FRAME_NUMBER)
  property, but the value is specified in milliseconds instead of sample
  frames. If both properties are specified, the sample frames value is
  favored. Default 0.
- [`MIX_PROP_PLAY_LOOP_START_FRAME_NUMBER`](MIX_PROP_PLAY_LOOP_START_FRAME_NUMBER):
  If the track is looping, this is the sample frame position that the track
  will loop back to; this lets one play an intro at the start of a track on
  the first iteration, but have a loop point somewhere in the middle
  thereafter. A value <= 0 will begin the loop from the start of the
  track's input. Default 0.
- [`MIX_PROP_PLAY_LOOP_START_MILLISECOND_NUMBER`](MIX_PROP_PLAY_LOOP_START_MILLISECOND_NUMBER):
  The same as using the
  [MIX_PROP_PLAY_LOOP_START_FRAME_NUMBER](MIX_PROP_PLAY_LOOP_START_FRAME_NUMBER)
  property, but the value is specified in milliseconds instead of sample
  frames. If both properties are specified, the sample frames value is
  favored. Default 0.
- [`MIX_PROP_PLAY_FADE_IN_FRAMES_NUMBER`](MIX_PROP_PLAY_FADE_IN_FRAMES_NUMBER):
  The number of sample frames over which to fade in the newly-started
  track. The track will begin mixing silence and reach full volume smoothly
  over this many sample frames. If the track loops before the fade-in is
  complete, it will continue to fade correctly from the loop point. A value
  <= 0 will disable fade-in, so the track starts mixing at full volume.
  Default 0.
- [`MIX_PROP_PLAY_FADE_IN_MILLISECONDS_NUMBER`](MIX_PROP_PLAY_FADE_IN_MILLISECONDS_NUMBER):
  The same as using the
  [MIX_PROP_PLAY_FADE_IN_FRAMES_NUMBER](MIX_PROP_PLAY_FADE_IN_FRAMES_NUMBER)
  property, but the value is specified in milliseconds instead of sample
  frames. If both properties are specified, the sample frames value is
  favored. Default 0.
- [`MIX_PROP_PLAY_APPEND_SILENCE_FRAMES_NUMBER`](MIX_PROP_PLAY_APPEND_SILENCE_FRAMES_NUMBER):
  At the end of mixing this track, after all loops are complete, append
  this many sample frames of silence as if it were part of the audio file.
  This allows for apps to implement effects in callbacks, like reverb, that
  need to generate samples past the end of the stream's audio, or perhaps
  introduce a delay before starting a new sound on the track without having
  to manage it directly. A value <= 0 generates no silence before stopping
  the track. Default 0.
- [`MIX_PROP_PLAY_APPEND_SILENCE_MILLISECONDS_NUMBER`](MIX_PROP_PLAY_APPEND_SILENCE_MILLISECONDS_NUMBER):
  The same as using the
  [MIX_PROP_PLAY_APPEND_SILENCE_FRAMES_NUMBER](MIX_PROP_PLAY_APPEND_SILENCE_FRAMES_NUMBER)
  property, but the value is specified in milliseconds instead of sample
  frames. If both properties are specified, the sample frames value is
  favored. Default 0.

If this function fails, mixing of this track will not start (or restart, if
it was already started).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PlayTag](MIX_PlayTag)
- [MIX_PlayAudio](MIX_PlayAudio)
- [MIX_StopTrack](MIX_StopTrack)
- [MIX_PauseTrack](MIX_PauseTrack)
- [MIX_TrackPlaying](MIX_TrackPlaying)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

