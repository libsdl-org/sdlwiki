###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Paused

Query whether a particular channel is paused.

## Syntax

```c
int Mix_Paused(int channel);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **channel**     | the channel to query, or -1 to query all channels. |

## Return Value

Return 1 if channel paused, 0 otherwise. If `channel` is -1, returns the
number of paused channels.

## Remarks

If an invalid channel is specified, this function returns zero.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

