###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupNewer

Find the "most recent" sample playing in a group of channels.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_GroupNewer(int tag);
```

## Function Parameters

|     |         |                                                              |
| --- | ------- | ------------------------------------------------------------ |
| int | **tag** | an arbitrary value, assigned to channels, to search through. |

## Return Value

(int) Returns the "most recent" sample playing in a group of channels

## Remarks

Specifically, this function returns the channel number that is assigned the
specified tag, is currently playing, and has the highest start time, based
on the value of SDL_GetTicks() when the channel started playing.

If no channel with this tag is currently playing, this function returns -1.

## Version

This function is available since SDL_mixer 2.0.0.

## See Also

- [Mix_GroupOldest](Mix_GroupOldest)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

