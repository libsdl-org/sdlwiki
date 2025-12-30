###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTaggedTracks

Get all tracks with a specific tag.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Track ** MIX_GetTaggedTracks(MIX_Mixer *mixer, const char *tag, int *count);
```

## Function Parameters

|                          |           |                                                                      |
| ------------------------ | --------- | -------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to query.                                                  |
| const char *             | **tag**   | the tag to search.                                                   |
| int *                    | **count** | a pointer filled in with the number of tracks returned, can be NULL. |

## Return Value

([MIX_Track](MIX_Track) **) Returns an array of the tracks,
NULL-terminated, or NULL on failure; call SDL_GetError() for more
information. The returned pointer hould be freed with SDL_free() when it is
no longer needed.

## Remarks

Tracks are not provided in any guaranteed order.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

