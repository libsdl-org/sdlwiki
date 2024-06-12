###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupChannels

Assign several consecutive channels to the same tag.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_GroupChannels(int from, int to, int tag);
```

## Function Parameters

|     |          |                                                |
| --- | -------- | ---------------------------------------------- |
| int | **from** | the first channel to set the tag on.           |
| int | **to**   | the last channel to set the tag on, inclusive. |
| int | **tag**  | an arbitrary value to assign a channel.        |

## Return Value

(int) Returns 0 if successful, negative on error

## Remarks

A tag is an arbitrary number that can be assigned to several mixer
channels, to form groups of channels.

If 'tag' is -1, the tag is removed (actually -1 is the tag used to
represent the group of all the channels).

This function replaces the requested channels' current tags; you may only
have one tag per channel.

You may not specify MAX_CHANNEL_POST for a channel.

Note that this returns success and failure in the _opposite_ way from
[Mix_GroupChannel](Mix_GroupChannel)(). We regret the API design mistake.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

