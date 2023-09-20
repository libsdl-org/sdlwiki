###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamQueued

Get the number of sample frames currently queued.

## Syntax

```c
int SDL_GetAudioStreamQueued(SDL_AudioStream *stream);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **stream**     | The audio stream to query |

## Return Value

Returns the number of sample frames queued.

## Remarks

Since audio streams can change their input format at any time, even if
there is still data queued in a different format, this reports the queued
_sample frames_, so if you queue two stereo samples in float32 format and
then queue five mono samples in Sint16 format, this will return 6.

Queued data is not converted until it is consumed by
[SDL_GetAudioStreamData](SDL_GetAudioStreamData), so this value should be
representative of the exact data that was put into the stream.

If the stream has so much data that it would overflow an int, the return
value is clamped to a maximum value, but no queued data is lost; if there
are gigabytes of data queued, the app might need to read some of it with
[SDL_GetAudioStreamData](SDL_GetAudioStreamData) before this function's
return value is no longer clamped.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)

----
[CategoryAPI](CategoryAPI)

