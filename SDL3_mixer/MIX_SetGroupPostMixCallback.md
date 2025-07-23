###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetGroupPostMixCallback

Set a callback that fires when a mixer group has completed mixing.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetGroupPostMixCallback(MIX_Group *group, MIX_GroupMixCallback cb, void *userdata);
```

## Function Parameters

|                                              |              |                                                                      |
| -------------------------------------------- | ------------ | -------------------------------------------------------------------- |
| [MIX_Group](MIX_Group) *                     | **group**    | the mixing group to assign this callback to.                         |
| [MIX_GroupMixCallback](MIX_GroupMixCallback) | **cb**       | the function to call when the group mixes. May be NULL.              |
| void *                                       | **userdata** | an opaque pointer provided to the callback for its own personal use. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

After all playing tracks in a mixer group have pulled in more data from
their inputs, transformed it, and mixed together into a single buffer, a
callback can be fired. This lets an app view the data at the last moment
that it is still a part of this group. It can also change the data in any
way it pleases during this callback, and the mixer will continue as if this
data came directly from the group's mix buffer.

Each group has its own unique callback. Tracks that aren't in an explicit
[MIX_Group](MIX_Group) are mixed in an internal grouping that is not
available to the app.

Passing a NULL callback here is legal; it disables this group's callback.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GroupMixCallback](MIX_GroupMixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

