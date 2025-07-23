###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetAudioDuration

Get the length of a [MIX_Audio](MIX_Audio)'s playback in sample frames.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_GetAudioDuration(MIX_Audio *audio);


#define MIX_DURATION_UNKNOWN -1
#define MIX_DURATION_INFINITE -2
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio to query. |

## Return Value

(Sint64) Returns the length of the audio in sample frames, or
[MIX_DURATION_UNKNOWN](MIX_DURATION_UNKNOWN) or
[MIX_DURATION_INFINITE](MIX_DURATION_INFINITE).

## Remarks

This information is also available via the
[MIX_PROP_METADATA_DURATION_FRAMES_NUMBER](MIX_PROP_METADATA_DURATION_FRAMES_NUMBER)
property, but it's common enough to provide a simple accessor function.

This reports the length of the data in _sample frames_, so sample-perfect
mixing can be possible. Sample frames are only meaningful as a measure of
time if the sample rate (frequency) is also known. To convert from sample
frames to milliseconds, use [MIX_AudioFramesToMS](MIX_AudioFramesToMS)().

Not all audio file formats can report the complete length of the data they
will produce through decoding: some can't calculate it, some might produce
infinite audio.

Also, some file formats can only report duration as a unit of time, which
means SDL_mixer might have to estimate sample frames from that information.
With less precision, the reported duration might be off by a few sample
frames in either direction.

This will return a value >= 0 if a duration is known. It might also return
[MIX_DURATION_UNKNOWN](MIX_DURATION_UNKNOWN) or
[MIX_DURATION_INFINITE](MIX_DURATION_INFINITE).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

