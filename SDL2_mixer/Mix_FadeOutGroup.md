###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FadeOutGroup

Halt a playing group of channels by arbitrary tag, after fading them out for a specified time.

## Syntax

```c
int Mix_FadeOutGroup(int tag, int ms);

```

## Function Parameters

|             |                                                          |
| ----------- | -------------------------------------------------------- |
| **tag**     | an arbitrary value, assigned to channels, to search for. |
| **ms**      | number of milliseconds to fade before halting the group. |

## Return Value

Returns the number of channels that were scheduled for fading.

## Remarks

This will begin fading a group of channels with a specific tag from their
current volumes to silence over `ms` milliseconds. After that time, those
channels are halted.

A tag is an arbitrary number that can be assigned to several mixer
channels, to form groups of channels.

The default tag for a channel is -1.

Any halted channels will have any currently-registered effects
deregistered, and will call any callback specified by
[Mix_ChannelFinished](Mix_ChannelFinished.md)() once the halt occurs.

A fading channel will change it's volume progressively, as if
[Mix_Volume](Mix_Volume.md)() was called on it (which is to say: you probably
shouldn't call [Mix_Volume](Mix_Volume.md)() on a fading channel).

Note that this function does not block for the number of milliseconds
requested; it just schedules the group to fade and notes the time for the
mixer to manage later, and returns immediately.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
