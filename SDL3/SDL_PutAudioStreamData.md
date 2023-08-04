###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PutAudioStreamData

Add data to be converted/resampled to the stream.

## Syntax

```c
int SDL_PutAudioStreamData(SDL_AudioStream *stream, const void *buf, int len);

```

## Function Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **stream**     | The stream the audio data is being added to |
| **buf**        | A pointer to the audio data to add          |
| **len**        | The number of bytes to write to the stream  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This data must match the format/channels/samplerate specified in the latest
call to [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat), or the format
specified when creating the stream if it hasn't been changed.

Note that this call simply queues unconverted data for later. This is
different than SDL2, where data was converted during the Put call and the
Get call would just dequeue the previously-converted data.

## Thread Safety

It is safe to call this function from any thread, but if the stream has a
callback set, the caller might need to manage extra locking.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

