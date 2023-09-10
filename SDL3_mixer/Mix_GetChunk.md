###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetChunk

Get the [Mix_Chunk](Mix_Chunk) currently associated with a mixer channel.

## Syntax

```c
Mix_Chunk * Mix_GetChunk(int channel);

```

## Function Parameters

|                 |                       |
| --------------- | --------------------- |
| **channel**     | the channel to query. |

## Return Value

Returns the associated chunk, if any, or NULL if it's an invalid channel.

## Remarks

You may not specify MAX_CHANNEL_POST or -1 for a channel.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

