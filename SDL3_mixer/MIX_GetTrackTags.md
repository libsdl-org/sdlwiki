###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackTags

Get the tags currently associated with a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
char ** MIX_GetTrackTags(MIX_Track *track, int *count);
```

## Function Parameters

|                          |           |                                                                    |
| ------------------------ | --------- | ------------------------------------------------------------------ |
| [MIX_Track](MIX_Track) * | **track** | the track to query.                                                |
| int *                    | **count** | a pointer filled in with the number of tags returned, can be NULL. |

## Return Value

(char **) Returns an array of the tags, NULL-terminated, or NULL on
failure; call SDL_GetError() for more information. This is a single
allocation that should be freed with SDL_free() when it is no longer
needed.

## Remarks

Tags are not provided in any guaranteed order.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

