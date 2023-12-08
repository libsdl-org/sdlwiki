###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamSpeed

Get the playback speed of an audio stream.

## Syntax

```c
float SDL_GetAudioStreamSpeed(SDL_AudioStream *stream);

```

## Function Parameters

|                |                                                  |
| -------------- | ------------------------------------------------ |
| **stream**     | the [SDL_AudioStream](SDL_AudioStream.md) to query. |

## Return Value

Returns the playback speed of the stream, or 0.0 on error

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetAudioStreamSpeed](SDL_SetAudioStreamSpeed.md)

----
[CategoryAPI](CategoryAPI.md)
