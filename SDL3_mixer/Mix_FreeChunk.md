###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FreeChunk

Free an audio chunk.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
void Mix_FreeChunk(Mix_Chunk *chunk);

```

## Function Parameters

|               |                    |
| ------------- | ------------------ |
| **chunk**     | the chunk to free. |

## Remarks

An app should call this function when it is done with a
[Mix_Chunk](Mix_Chunk) and wants to dispose of its resources.

SDL_mixer will stop any channels this chunk is currently playing on. This
will deregister all effects on those channels and call any callback
specified by [Mix_ChannelFinished](Mix_ChannelFinished)() for each removed
channel.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

* [Mix_LoadWAV](Mix_LoadWAV)
* [Mix_LoadWAV_IO](Mix_LoadWAV_IO)
* [Mix_QuickLoad_WAV](Mix_QuickLoad_WAV)
* [Mix_QuickLoad_RAW](Mix_QuickLoad_RAW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

