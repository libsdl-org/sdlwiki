###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_UnregisterEffect

Explicitly unregister a special effect function.

## Syntax

```c
int Mix_UnregisterEffect(int channel, Mix_EffectFunc_t f);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **channel**     | the channel to unregister an effect on, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |
| **f**           | effect the callback stop calling in future mixing iterations.                    |

## Return Value

Returns zero if error (no such channel or effect), nonzero if removed.
Error messages can be retrieved from [Mix_GetError](Mix_GetError)().

## Remarks

You may not need to call this at all, unless you need to stop an effect
from processing in the middle of a chunk's playback.

Posteffects are never implicitly unregistered as they are for channels (as
the output stream does not have an end), but they may be explicitly
unregistered through this function by specifying
[MIX_CHANNEL_POST](MIX_CHANNEL_POST) for a channel.

Note that unlike most SDL and SDL_mixer functions, this function returns
zero if there's an error, not on success. We apologize for the API design
inconsistency here.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

