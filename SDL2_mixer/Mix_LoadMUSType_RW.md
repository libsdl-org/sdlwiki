###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_LoadMUSType_RW

Load an audio format into a music object, assuming a specific format.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
Mix_Music * Mix_LoadMUSType_RW(SDL_RWops *src, Mix_MusicType type, int freesrc);
```

## Function Parameters

|                                |             |                                                                               |
| ------------------------------ | ----------- | ----------------------------------------------------------------------------- |
| SDL_RWops *                    | **src**     | an SDL_RWops that data will be read from.                                     |
| [Mix_MusicType](Mix_MusicType) | **type**    | the type of audio data provided by `src`.                                     |
| int                            | **freesrc** | non-zero to close/free the SDL_RWops before returning, zero to leave it open. |

## Return Value

([Mix_Music](Mix_Music) *) Returns a new music object, or NULL on error.

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

This function loads music data, and lets the application specify the type
of music being loaded, which might be useful if SDL_mixer cannot figure it
out from the data stream itself.

Currently, the following types are supported:

- `MUS_NONE` (SDL_mixer should guess, based on the data)
- `MUS_WAV` (Microsoft WAV files)
- `MUS_MOD` (Various tracker formats)
- `MUS_MID` (MIDI files)
- `MUS_OGG` (Ogg Vorbis files)
- `MUS_MP3` (MP3 files)
- `MUS_FLAC` (FLAC files)
- `MUS_OPUS` (Opus files)
- `MUS_WAVPACK` (WavPack files)

If `freesrc` is non-zero, the RWops will be closed when SDL_mixer is done
with it, which will be before this function call returns if there is an
error, or perhaps much later if the music is streaming for some time. The
app should not attempt to use the RWops again, as it may become invalid
without warning.

As a convenience, there is a function to read files from disk without
having to deal with SDL_RWops: `Mix_LoadMUS("filename.mp3")` will manage
those details for you (but not let you specify the music type explicitly)..

When done with this music, the app should dispose of it with a call to
[Mix_FreeMusic](Mix_FreeMusic)().

## Version

This function is available since SDL_mixer 2.0.0.

## See Also

- [Mix_FreeMusic](Mix_FreeMusic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

