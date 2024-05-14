###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_LoadWAV

Load a supported audio format into a chunk.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
Mix_Chunk * Mix_LoadWAV(const char *file);

```

## Function Parameters

|              |                                        |
| ------------ | -------------------------------------- |
| **file**     | the filesystem path to load data from. |

## Return Value

Returns a new chunk, or NULL on error.

## Remarks

SDL_mixer has two separate data structures for audio data. One it calls a
"chunk," which is meant to be a file completely decoded into memory up
front, and the other it calls "music" which is a file intended to be
decoded on demand. Originally, simple formats like uncompressed WAV files
were meant to be chunks and compressed things, like MP3s, were meant to be
music, and you would stream one thing for a game's music and make repeating
sound effects with the chunks.

In modern times, this isn't split by format anymore, and most are
interchangeable, so the question is what the app thinks is worth
predecoding or not. Chunks might take more memory, but once they are loaded
won't need to decode again, whereas music always needs to be decoded on the
fly. Also, crucially, there are as many channels for chunks as the app can
allocate, but SDL_mixer only offers a single "music" channel.

If you would rather use the abstract SDL_IOStream interface to load data
from somewhere other than the filesystem, you can use
[Mix_LoadWAV_IO](Mix_LoadWAV_IO)() instead.

When done with a chunk, the app should dispose of it with a call to
[Mix_FreeChunk](Mix_FreeChunk)().

Note that before SDL_mixer 3.0.0, this function was a macro that called
[Mix_LoadWAV_IO](Mix_LoadWAV_IO)(), creating a IOStream and setting
`closeio` to SDL_TRUE. This macro has since been promoted to a proper API
function. Older binaries linked against a newer SDL_mixer will still call
[Mix_LoadWAV_IO](Mix_LoadWAV_IO) directly, as they are using the macro,
which was available since the dawn of time.

## Version

This function is available since SDL_mixer 3.0.0

## See Also

- [Mix_LoadWAV_IO](Mix_LoadWAV_IO)
- [Mix_FreeChunk](Mix_FreeChunk)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

