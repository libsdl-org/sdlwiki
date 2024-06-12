###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetChunk

Get the [Mix_Chunk](Mix_Chunk) currently associated with a mixer channel.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
Mix_Chunk * Mix_GetChunk(int channel);
```

## Function Parameters

|     |             |                       |
| --- | ----------- | --------------------- |
| int | **channel** | the channel to query. |

## Return Value

([Mix_Chunk](Mix_Chunk) *) Returns the associated chunk, if any, or NULL if
it's an invalid channel.

## Remarks

You may not specify MAX_CHANNEL_POST or -1 for a channel.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

