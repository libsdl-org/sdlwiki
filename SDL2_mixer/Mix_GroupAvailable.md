###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupAvailable

Finds the first available channel in a group of channels.

## Syntax

```c
int Mix_GroupAvailable(int tag);

```

## Function Parameters

|             |                                                          |
| ----------- | -------------------------------------------------------- |
| **tag**     | an arbitrary value, assigned to channels, to search for. |

## Return Value

Returns first available channel, or -1 if none are available.

## Remarks

A tag is an arbitary number that can be assigned to several mixer channels,
to form groups of channels.

This function searches all channels with a specified tag, and returns the
channel number of the first one it finds that is currently unused.

If no channels with the specified tag are unused, this function returns -1.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
