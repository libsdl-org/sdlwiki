###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_UnregisterAllEffects

Explicitly unregister all special effect functions.

## Syntax

```c
int Mix_UnregisterAllEffects(int channel);

```

## Function Parameters

|              |                                                                                    |
| ------------ | ---------------------------------------------------------------------------------- |
| **chan**     | the channel to unregister all effects on, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |

## Return Value

Returns zero if error (no such channel), nonzero if all effects removed.
Error messages can be retrieved from [Mix_GetError](Mix_GetError)().

## Remarks

You may not need to call this at all, unless you need to stop all effects
from processing in the middle of a chunk's playback.

Note that this will also shut off some internal effect processing, since
[Mix_SetPanning](Mix_SetPanning)() and others may use this API under the
hood. This is called internally when a channel completes playback.
Posteffects are never implicitly unregistered as they are for channels, but
they may be explicitly unregistered through this function by specifying
[MIX_CHANNEL_POST](MIX_CHANNEL_POST) for a channel.

Note that unlike most SDL and SDL_mixer functions, this function returns
zero if there's an error, not on success. We apologize for the API design
inconsistency here.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

