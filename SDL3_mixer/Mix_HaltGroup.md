###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HaltGroup

Halt playing of a group of channels by arbitrary tag.

## Syntax

```c
int Mix_HaltGroup(int tag);

```

## Function Parameters

|             |                                                          |
| ----------- | -------------------------------------------------------- |
| **tag**     | an arbitrary value, assigned to channels, to search for. |

## Return Value

Returns zero, whether any channels were halted or not.

## Remarks

This will stop further playback on all channels with a specific tag, until
a new chunk is started there.

A tag is an arbitrary number that can be assigned to several mixer
channels, to form groups of channels.

The default tag for a channel is -1.

Any halted channels will have any currently-registered effects
deregistered, and will call any callback specified by
[Mix_ChannelFinished](Mix_ChannelFinished)() before this function returns.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

