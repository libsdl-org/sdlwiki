###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Paused

Query whether a particular channel is paused.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_Paused(int channel);
```

## Function Parameters

|     |             |                                                    |
| --- | ----------- | -------------------------------------------------- |
| int | **channel** | the channel to query, or -1 to query all channels. |

## Return Value

(int) Return 1 if channel paused, 0 otherwise. If `channel` is -1, returns
the number of paused channels.

## Remarks

If an invalid channel is specified, this function returns zero.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

