###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetReverseStereo

Cause a channel to reverse its stereo.

## Syntax

```c
int Mix_SetReverseStereo(int channel, int flip);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **channel**     | The mixer channel to reverse, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST.md). |
| **flip**        | non-zero to reverse stereo, zero to disable this effect.               |

## Return Value

Returns zero if error (no such channel or
[Mix_RegisterEffect](Mix_RegisterEffect.md)() fails), nonzero if reversing
effect is enabled. Note that an audio device in mono mode is a no-op, but
this call will return successful in that case. Error messages can be
retrieved from [Mix_GetError](Mix_GetError.md)().

## Remarks

This is handy if the user has his speakers hooked up backwards, or you
would like to have a trippy sound effect.

Calling this function with `flip` set to non-zero reverses the chunks's
usual channels. If `flip` is zero, the effect is unregistered.

This uses the [Mix_RegisterEffect](Mix_RegisterEffect.md)() API internally,
and thus is probably more CPU intensive than having the user just plug in
his speakers correctly. [Mix_SetReverseStereo](Mix_SetReverseStereo.md)()
returns without registering the effect function if the audio device is not
configured for stereo output.

If you specify [MIX_CHANNEL_POST](MIX_CHANNEL_POST.md) for `channel`, then
this effect is used on the final mixed stream before sending it on to the
audio device (a posteffect).

Note that unlike most SDL and SDL_mixer functions, this function returns
zero if there's an error, not on success. We apologize for the API design
inconsistency here.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
