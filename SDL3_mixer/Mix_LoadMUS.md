###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_LoadMUS

Load a supported audio format into a music object.

## Syntax

```c
Mix_Music * Mix_LoadMUS(const char *file);

```

## Function Parameters

|              |                                            |
| ------------ | ------------------------------------------ |
| **file**     | a file path from where to load music data. |

## Return Value

Returns a new music object, or NULL on error.

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

When done with this music, the app should dispose of it with a call to
[Mix_FreeMusic](Mix_FreeMusic)().

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_FreeMusic](Mix_FreeMusic)

----
[CategoryAPI](CategoryAPI)

