###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_QuickLoad_RAW

Load a raw audio data from memory as quickly as possible.

## Syntax

```c
Mix_Chunk * Mix_QuickLoad_RAW(Uint8 *mem, Uint32 len);

```

## Function Parameters

|             |                                                 |
| ----------- | ----------------------------------------------- |
| **mem**     | memory buffer containing raw PCM data.          |
| **len**     | length of buffer pointed to by `mem`, in bytes. |

## Return Value

Returns a new chunk, or NULL on error.

## Remarks

The audio data MUST be in the exact same format as the audio device. This
function will not attempt to convert it, or even verify it's in the right
format.

If this function is successful, the provided memory buffer must remain
available until [Mix_FreeChunk](Mix_FreeChunk)() is called on the returned
chunk.

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_FreeChunk](Mix_FreeChunk)

----
[CategoryAPI](CategoryAPI)

