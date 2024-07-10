###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamOutputChannelMap

Set the current output channel map of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_SetAudioStreamOutputChannelMap(SDL_AudioStream *stream, const int *chmap, int count);
```

## Function Parameters

|                                      |            |                                                   |
| ------------------------------------ | ---------- | ------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the [SDL_AudioStream](SDL_AudioStream) to change. |
| const int *                          | **chmap**  | the new channel map, NULL to reset to default.    |
| int                                  | **count**  | The number of channels in the map.                |

## Return Value

(int) Returns 0 on success, -1 on error.

## Remarks

Channel maps are optional; most things do not need them, instead passing
data in the [order that SDL expects](CategoryAudio#channel-layouts).

The output channel map reorders data that leaving a stream via
[SDL_GetAudioStreamData](SDL_GetAudioStreamData).

Each item in the array represents an output channel, and its value is the
channel that it should be remapped to. To reverse a stereo signal's left
and right values, you'd have an array of `{ 1, 0 }`. It is legal to remap
multiple channels to the same thing, so `{ 1, 1 }` would duplicate the
right channel to both channels of a stereo signal. You cannot change the
number of channels through a channel map, just reorder them.

The output channel map can be changed at any time, as output remapping is
applied during [SDL_GetAudioStreamData](SDL_GetAudioStreamData).

Audio streams default to no remapping applied. Passing a NULL channel map
is legal, and turns off remapping.

SDL will copy the channel map; the caller does not have to save this array
after this call.

If `count` is not equal to the current number of channels in the audio
stream's format, this will fail. This is a safety measure to make sure a a
race condition hasn't changed the format while you this call is setting the
channel map.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running. Don't change the stream's format to
have a different number of channels from a a different thread at the same
time, though!

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetAudioStreamInputChannelMap](SDL_SetAudioStreamInputChannelMap)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

