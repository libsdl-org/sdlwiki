###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_CreateGroup

Create a mixing group.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Group * MIX_CreateGroup(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                                              |
| ------------------------ | --------- | -------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer on which to create a mixing group. |

## Return Value

([MIX_Group](MIX_Group) *) Returns a newly-created mixing group, or NULL on
error; call SDL_GetError() for more information.

## Remarks

Tracks are assigned to a mixing group (or if unassigned, they live in a
mixer's internal default group). All tracks in a group are mixed together
and the app can access this mixed data before it is mixed with all other
groups to produce the final output.

This can be a useful feature, but is completely optional; apps can ignore
mixing groups entirely and still have a full experience with SDL_mixer.

After creating a group, assign tracks to it with
[MIX_SetTrackGroup](MIX_SetTrackGroup)(). Use
[MIX_SetGroupPostMixCallback](MIX_SetGroupPostMixCallback)() to access the
group's mixed data.

A mixing group can be destroyed with [MIX_DestroyGroup](MIX_DestroyGroup)()
when no longer needed. Destroying the mixer will also destroy all its
still-existing mixing groups.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyGroup](MIX_DestroyGroup)
- [MIX_SetTrackGroup](MIX_SetTrackGroup)
- [MIX_SetGroupPostMixCallback](MIX_SetGroupPostMixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

