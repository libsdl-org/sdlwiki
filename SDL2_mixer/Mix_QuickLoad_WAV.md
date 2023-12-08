###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_QuickLoad_WAV

Load a WAV file from memory as quickly as possible.

## Syntax

```c
Mix_Chunk * Mix_QuickLoad_WAV(Uint8 *mem);

```

## Function Parameters

|             |                                         |
| ----------- | --------------------------------------- |
| **mem**     | memory buffer containing of a WAV file. |

## Return Value

Returns a new chunk, or NULL on error.

## Remarks

Unlike [Mix_LoadWAV_RW](Mix_LoadWAV_RW.md), this function has several
requirements, and unless you control all your audio data and know what
you're doing, you should consider this function unsafe and not use it.

- The provided audio data MUST be in Microsoft WAV format.
- The provided audio data shouldn't use any strange WAV extensions.
- The audio data MUST be in the exact same format as the audio device. This
  function will not attempt to convert it, or even verify it's in the right
  format.
- The audio data must be valid; this function does not know the size of the
  memory buffer, so if the WAV data is corrupted, it can read past the end
  of the buffer, causing a crash.
- The audio data must live at least as long as the returned
  [Mix_Chunk](Mix_Chunk.md), because SDL_mixer will use that data directly and
  not make a copy of it.

This function will do NO error checking! Be extremely careful here!

(Seriously, use [Mix_LoadWAV_RW](Mix_LoadWAV_RW.md) instead.)

If this function is successful, the provided memory buffer must remain
available until [Mix_FreeChunk](Mix_FreeChunk.md)() is called on the returned
chunk.

## Version

This function is available since SDL_mixer 2.0.0.

## Related Functions

* [Mix_LoadWAV_RW](Mix_LoadWAV_RW.md)
* [Mix_FreeChunk](Mix_FreeChunk.md)

----
[CategoryAPI](CategoryAPI.md)
