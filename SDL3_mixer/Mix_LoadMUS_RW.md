###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_LoadMUS_RW

Load a supported audio format into a music object.

## Syntax

```c
Mix_Music * Mix_LoadMUS_RW(SDL_RWops *src, SDL_bool freesrc);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **src**         | an SDL_RWops that data will be read from.                                          |
| **freesrc**     | SDL_TRUE to close/free the SDL_RWops before returning, SDL_FALSE to leave it open. |

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

If `freesrc` is SDL_TRUE, the RWops will be closed before returning,
whether this function succeeds or not. SDL_mixer reads everything it needs
from the RWops during this call in any case.

As a convenience, there is a function to read files from disk without
having to deal with SDL_RWops: `Mix_LoadMUS("filename.mp3")` will manage
those details for you.

This function attempts to guess the file format from incoming data. If the
caller knows the format, or wants to force it, it should use
[Mix_LoadMUSType_RW](Mix_LoadMUSType_RW.md)() instead.

When done with this music, the app should dispose of it with a call to
[Mix_FreeMusic](Mix_FreeMusic.md)().

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_FreeMusic](Mix_FreeMusic.md)

----
[CategoryAPI](CategoryAPI.md)
