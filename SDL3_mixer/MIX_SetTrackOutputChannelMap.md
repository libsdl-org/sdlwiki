###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackOutputChannelMap

Set the current output channel map of a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackOutputChannelMap(MIX_Track *track, const int *chmap, int count);
```

## Function Parameters

|                          |           |                                                |
| ------------------------ | --------- | ---------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to change.                           |
| const int *              | **chmap** | the new channel map, NULL to reset to default. |
| int                      | **count** | The number of channels in the map.             |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Channel maps are optional; most things do not need them, instead passing
data in the order that SDL expects.

The output channel map reorders track data after transformations and before
it is mixed into a mixer group. This can be useful for reversing stereo
channels, for example.

Each item in the array represents an input channel, and its value is the
channel that it should be remapped to. To reverse a stereo signal's left
and right values, you'd have an array of `{ 1, 0 }`. It is legal to remap
multiple channels to the same thing, so `{ 1, 1 }` would duplicate the
right channel to both channels of a stereo signal. An element in the
channel map set to -1 instead of a valid channel will mute that channel,
setting it to a silence value.

You cannot change the number of channels through a channel map, just
reorder/mute them.

Tracks default to no remapping applied. Passing a NULL channel map is
legal, and turns off remapping.

SDL_mixer will copy the channel map; the caller does not have to save this
array after this call.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

