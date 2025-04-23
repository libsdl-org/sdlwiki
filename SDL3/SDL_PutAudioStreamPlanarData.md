# SDL_PutAudioStreamPlanarData

Add data to the stream with each channel in a separate array.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_PutAudioStreamPlanarData(SDL_AudioStream *stream, const void * const *channel_buffers, int num_samples);
```

## Function Parameters

|                                      |                     |                                                           |
| ------------------------------------ | ------------------- | --------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream**          | the stream the audio data is being added to.              |
| const void * const *                 | **channel_buffers** | a pointer to an array of arrays, one array per channel.   |
| int                                  | **num_samples**     | the number of _samples_ per array to write to the stream. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This data must match the format/channels/samplerate specified in the latest
call to [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat), or the format
specified when creating the stream if it hasn't been changed.

The data will be interleaved and queued. Note that
[SDL_AudioStream](SDL_AudioStream) only operates on interleaved data, so
this is simply a convenience function for easily queueing data from sources
that provide separate arrays. There is no equivalent function to retrieve
planar data.

The arrays in `channel_buffers` are ordered as they are to be interleaved;
the first array will be the first sample in the interleaved data. Any
individual array may be NULL; in this case, silence will be interleaved for
that channel.

Note that `num_samples` is the number of _samples per array_. This can also
be thought of as the number of _sample frames_ to be queued. A value of 1
with stereo arrays will queue two samples to the stream. This is different
than [SDL_PutAudioStreamData](SDL_PutAudioStreamData), which wants the size
of a single array in bytes.

## Thread Safety

It is safe to call this function from any thread, but if the stream has a
callback set, the caller might need to manage extra locking.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_ClearAudioStream](SDL_ClearAudioStream)
- [SDL_FlushAudioStream](SDL_FlushAudioStream)
- [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
- [SDL_GetAudioStreamQueued](SDL_GetAudioStreamQueued)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

