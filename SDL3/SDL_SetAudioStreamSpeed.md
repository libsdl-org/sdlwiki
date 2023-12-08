###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamSpeed

Change the playback speed of an audio stream.

## Syntax

```c
int SDL_SetAudioStreamSpeed(SDL_AudioStream *stream,
                            float speed);

```

## Function Parameters

|                |                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------- |
| **stream**     | The stream the speed is being changed                                                     |
| **speed**      | The new speed. 1.0 is normal speed, 1.2 is 20% faster, etc. Must be between 0.01 and 100. |

## Return Value

Returns 0 on success, or -1 on error.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAudioStreamSpeed](SDL_GetAudioStreamSpeed.md)
* [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat.md)

----
[CategoryAPI](CategoryAPI.md)
