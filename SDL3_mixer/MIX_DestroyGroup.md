###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_DestroyGroup

Destroy a mixing group.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_DestroyGroup(MIX_Group *group);
```

## Function Parameters

|                          |           |                              |
| ------------------------ | --------- | ---------------------------- |
| [MIX_Group](MIX_Group) * | **group** | the mixing group to destroy. |

## Remarks

Any tracks currently assigned to this group will be reassigned to the
mixer's internal default group.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_CreateGroup](MIX_CreateGroup)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

