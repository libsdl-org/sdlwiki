###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetPostMixCallback

Set a callback that fires when all mixing has completed.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetPostMixCallback(MIX_Mixer *mixer, MIX_PostMixCallback cb, void *userdata);
```

## Function Parameters

|                                            |              |                                                                      |
| ------------------------------------------ | ------------ | -------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) *                   | **mixer**    | the mixer to assign this callback to.                                |
| [MIX_PostMixCallback](MIX_PostMixCallback) | **cb**       | the function to call when the mixer mixes. May be NULL.              |
| void *                                     | **userdata** | an opaque pointer provided to the callback for its own personal use. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

After all mixer groups have processed, their buffers are mixed together
into a single buffer for the final output, at which point a callback can be
fired. This lets an app view the data at the last moment before mixing
completes. It can also change the data in any way it pleases during this
callback, and the mixer will continue as if this data is the final output.

Each mixer has its own unique callback.

Passing a NULL callback here is legal; it disables this mixer's callback.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PostMixCallback](MIX_PostMixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

