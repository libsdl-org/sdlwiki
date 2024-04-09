###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamData

Get converted/resampled data from the stream.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetAudioStreamData(SDL_AudioStream *stream, void *buf, int len);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **stream**     | The stream the audio is being requested from |
| **buf**        | A buffer to fill with audio data             |
| **len**        | The maximum number of bytes to fill          |

## Return Value

Returns the number of bytes read from the stream, or -1 on error

## Remarks

The input/output data format/channels/samplerate is specified when creating
the stream, and can be changed after creation by calling
[SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat).

Note that any conversion and resampling necessary is done during this call,
and [SDL_PutAudioStreamData](SDL_PutAudioStreamData) simply queues
unconverted data for later. This is different than SDL2, where that work
was done while inputting new data to the stream and requesting the output
just copied the converted data.

## Thread Safety

It is safe to call this function from any thread, but if the stream has a
callback set, the caller might need to manage extra locking.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

