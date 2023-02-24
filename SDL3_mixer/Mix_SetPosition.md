###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetPosition

Set the position of a channel.

## Syntax

```c
int Mix_SetPosition(int channel, Sint16 angle, Uint8 distance);

```

## Function Parameters

|                  |                                                                         |
| ---------------- | ----------------------------------------------------------------------- |
| **channel**      | The mixer channel to position, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |
| **angle**        | angle, in degrees. North is 0, and goes clockwise.                      |
| **distance**     | distance; 0 is the listener, 255 is maxiumum distance away.             |

## Return Value

Returns zero if error (no such channel or
[Mix_RegisterEffect](Mix_RegisterEffect)() fails), nonzero if position
effect is enabled. Error messages can be retrieved from
[Mix_GetError](Mix_GetError)().

## Remarks

`angle` is an integer from 0 to 360, that specifies the location of the
sound in relation to the listener. `angle` will be reduced as neccesary
(540 becomes 180 degrees, -100 becomes 260). Angle 0 is due north, and
rotates clockwise as the value increases. For efficiency, the precision of
this effect may be limited (angles 1 through 7 might all produce the same
effect, 8 through 15 are equal, etc). `distance` is an integer between 0
and 255 that specifies the space between the sound and the listener. The
larger the number, the further away the sound is. Using 255 does not
guarantee that the channel will be removed from the mixing process or be
completely silent. For efficiency, the precision of this effect may be
limited (distance 0 through 5 might all produce the same effect, 6 through
10 are equal, etc). Setting `angle` and `distance` to 0 unregisters this
effect, since the data would be unchanged.

If you need more precise positional audio, consider using OpenAL for
spatialized effects instead of SDL_mixer. This is only meant to be a basic
effect for simple "3D" games.

If the audio device is configured for mono output, then you won't get any
effectiveness from the angle; however, distance attenuation on the channel
will still occur. While this effect will function with stereo voices, it
makes more sense to use voices with only one channel of sound, so when they
are mixed through this effect, the positioning will sound correct. You can
convert them to mono through SDL before giving them to the mixer in the
first place if you like.

Setting the channel to [MIX_CHANNEL_POST](MIX_CHANNEL_POST) registers this
as a posteffect, and the positioning will be done to the final mixed stream
before passing it on to the audio device.

This is a convenience wrapper over [Mix_SetDistance](Mix_SetDistance)() and
[Mix_SetPanning](Mix_SetPanning)().

Note that unlike most SDL and SDL_mixer functions, this function returns
zero if there's an error, not on success. We apologize for the API design
inconsistency here.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

