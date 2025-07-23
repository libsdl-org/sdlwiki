###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_CreateTrack

Create a new track on a mixer.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Track * MIX_CreateTrack(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                                          |
| ------------------------ | --------- | ---------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer on which to create this track. |

## Return Value

([MIX_Track](MIX_Track) *) Returns a new [MIX_Track](MIX_Track) on success,
NULL on error; call SDL_GetError() for more informations.

## Remarks

A track provides a single source of audio. All currently-playing tracks
will be processed and mixed together to form the final output from the
mixer.

There are no limits to the number of tracks on may create, beyond running
out of memory, but in normal practice there are a small number of tracks
that are reused between all loaded audio as appropriate.

Tracks are unique to a specific [MIX_Mixer](MIX_Mixer) and can't be
transferred between them.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyTrack](MIX_DestroyTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

