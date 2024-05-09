###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupOldest

Find the "oldest" sample playing in a group of channels.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
int Mix_GroupOldest(int tag);

```

## Function Parameters

|             |                                                              |
| ----------- | ------------------------------------------------------------ |
| **tag**     | an arbitrary value, assigned to channels, to search through. |

## Return Value

Returns the "oldest" sample playing in a group of channels

## Remarks

Specifically, this function returns the channel number that is assigned the
specified tag, is currently playing, and has the lowest start time, based
on the value of SDL_GetTicks() when the channel started playing.

If no channel with this tag is currently playing, this function returns -1.

## Version

This function is available since SDL_mixer 2.0.0.

## See Also

- [Mix_GroupNewer](Mix_GroupNewer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

