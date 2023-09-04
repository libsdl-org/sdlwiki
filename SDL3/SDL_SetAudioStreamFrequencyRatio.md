###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamFrequencyRatio

Change the frequency ratio of an audio stream.

## Syntax

```c
int SDL_SetAudioStreamFrequencyRatio(SDL_AudioStream *stream, float ratio);

```

## Function Parameters

|                |                                                                         |
| -------------- | ----------------------------------------------------------------------- |
| **stream**     | The stream the frequency ratio is being changed                         |
| **ratio**      | The frequency ratio. 1.0 is normal speed. Must be between 0.01 and 100. |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

The frequency ratio is used to adjust the rate at which input data is
consumed. Changing this effectively modifies the speed and pitch of the
audio. A value greater than 1.0 will play the audio faster, and at a higher
pitch. A value less than 1.0 will play the audio slower, and at a lower
pitch.

This is applied during [SDL_GetAudioStreamData](SDL_GetAudioStreamData),
and can be continuously changed to create various effects.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAudioStreamFrequencyRatio](SDL_GetAudioStreamFrequencyRatio)
* [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat)

----
[CategoryAPI](CategoryAPI)

