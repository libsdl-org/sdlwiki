###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetGroupMixer

Get the [MIX_Mixer](MIX_Mixer) that owns a [MIX_Group](MIX_Group).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Mixer * MIX_GetGroupMixer(MIX_Group *group);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Group](MIX_Group) * | **group** | the group to query. |

## Return Value

([MIX_Mixer](MIX_Mixer) *) Returns the mixer associated with the group, or
NULL on error; call SDL_GetError() for more information.

## Remarks

This is the mixer pointer that was passed to
[MIX_CreateGroup](MIX_CreateGroup)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

