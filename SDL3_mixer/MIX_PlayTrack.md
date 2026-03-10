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

SDL_PropertiesID are discussed in
[SDL's documentation](https://wiki.libsdl.org/SDL3/CategoryProperties)
.

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
- [`MIX_PROP_PLAY_FADE_IN_START_GAIN_FLOAT`](MIX_PROP_PLAY_FADE_IN_START_GAIN_FLOAT):
  If fading in, start fading from this volume level. 0.0f is silence and
  1.0f is full volume, every in between is a linear change in gain. The
  specified value will be clamped between 0.0f and 1.0f. Default 0.0f.
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
- [`MIX_PROP_PLAY_HALT_WHEN_EXHAUSTED_BOOLEAN`](MIX_PROP_PLAY_HALT_WHEN_EXHAUSTED_BOOLEAN):
  If true, when input is completely consumed for the track, the mixer will
  mark the track as stopped (and call any appropriate
  [MIX_TrackStoppedCallback](MIX_TrackStoppedCallback), etc); to play more,
  the track will need to be restarted. If false, the track will just not
  contribute to the mix, but it will not be marked as stopped. There may be
  clever logic tricks this exposes generally, but this property is
  specifically useful when the track's input is an SDL_AudioStream assigned
  via [MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)(). Setting this
  property to true can be useful when pushing a complete piece of audio to
  the stream that has a definite ending, as the track will operate like any
  other audio was applied. Setting to false means as new data is added to
  the stream, the mixer will start using it as soon as possible, which is
  useful when audio should play immediately as it drips in: new VoIP
  packets, etc. Note that in this situation, if the audio runs out when
  needed, there _will_ be gaps in the mixed output, so try to buffer enough
  data to avoid this when possible. Note that a track is not consider
  exhausted until all its loops and appended silence have been mixed (and
  also, that loops don't mean anything when the input is an AudioStream).
  Default true.
- [`MIX_PROP_PLAY_START_ORDER_NUMBER`](MIX_PROP_PLAY_START_ORDER_NUMBER):
  This is a special-case property that most apps can ignore. For mod file
  formats, start mixing from a specific "order" index instead of the start
  of the file. A value < 0 will cause this property to be ignored. If the
  decoder doesn't support this property, it will also be ignored. If this
  property is _not_ ignored, the
  [MIX_PROP_PLAY_START_FRAME_NUMBER](MIX_PROP_PLAY_START_FRAME_NUMBER) and
  [MIX_PROP_PLAY_START_MILLISECOND_NUMBER](MIX_PROP_PLAY_START_MILLISECOND_NUMBER)
  properties will be ignored instead. Default -1. Since SDL_mixer 3.2.2.

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

