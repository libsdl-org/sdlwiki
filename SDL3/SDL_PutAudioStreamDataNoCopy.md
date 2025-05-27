# SDL_PutAudioStreamDataNoCopy

Add external data to an audio stream without copying it.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_PutAudioStreamDataNoCopy(SDL_AudioStream *stream, const void *buf, int len, SDL_AudioStreamDataCompleteCallback callback, void *userdata);
```

## Function Parameters

|                                                                            |              |                                                                                             |
| -------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) *                                       | **stream**   | the stream the audio data is being added to.                                                |
| const void *                                                               | **buf**      | a pointer to the audio data to add.                                                         |
| int                                                                        | **len**      | the number of bytes to add to the stream.                                                   |
| [SDL_AudioStreamDataCompleteCallback](SDL_AudioStreamDataCompleteCallback) | **callback** | the callback function to call when the data is no longer needed by the stream. May be NULL. |
| void *                                                                     | **userdata** | an opaque pointer provided to the callback for its own personal use.                        |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Unlike [SDL_PutAudioStreamData](SDL_PutAudioStreamData)(), this function
does not make a copy of the provided data, instead storing the provided
pointer. This means that the put operation does not need to allocate and
copy the data, but the original data must remain available until the stream
is done with it, either by being read from the stream in its entirety, or a
call to [SDL_ClearAudioStream](SDL_ClearAudioStream)() or
[SDL_DestroyAudioStream](SDL_DestroyAudioStream)().

The data must match the format/channels/samplerate specified in the latest
call to [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat), or the format
specified when creating the stream if it hasn't been changed.

An optional callback may be provided, which is called when the stream no
longer needs the data. Once this callback fires, the stream will not access
the data again. This callback will fire for any reason the data is no
longer needed, including clearing or destroying the stream.

Note that there is still an allocation to store tracking information, so
this function is more efficient for larger blocks of data. If you're
planning to put a few samples at a time, it will be more efficient to use
[SDL_PutAudioStreamData](SDL_PutAudioStreamData)(), which allocates and
buffers in blocks.

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

