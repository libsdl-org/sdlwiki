###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupChannel

Assign a tag to a channel.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_GroupChannel(int which, int tag);
```

## Function Parameters

|     |           |                                         |
| --- | --------- | --------------------------------------- |
| int | **which** | the channel to set the tag on.          |
| int | **tag**   | an arbitrary value to assign a channel. |

## Return Value

(int) Returns non-zero on success, zero on error (no such channel).

## Remarks

A tag is an arbitary number that can be assigned to several mixer channels,
to form groups of channels.

If 'tag' is -1, the tag is removed (actually -1 is the tag used to
represent the group of all the channels).

This function replaces the requested channel's current tag; you may only
have one tag per channel.

You may not specify MAX_CHANNEL_POST for a channel.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

