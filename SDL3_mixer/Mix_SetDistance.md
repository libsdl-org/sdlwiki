###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetDistance

Set the "distance" of a channel.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_SetDistance(int channel, Uint8 distance);
```

## Function Parameters

|       |              |                                                                          |
| ----- | ------------ | ------------------------------------------------------------------------ |
| int   | **channel**  | The mixer channel to attenuate, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |
| Uint8 | **distance** | distance; 0 is the listener, 255 is maxiumum distance away.              |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

`distance` is an integer from 0 to 255 that specifies the location of the
sound in relation to the listener. Distance 0 is overlapping the listener,
and 255 is as far away as possible. A distance of 255 does not guarantee
silence; in such a case, you might want to try changing the chunk's volume,
or just cull the sample from the mixing process with
[Mix_HaltChannel](Mix_HaltChannel)(). For efficiency, the precision of this
effect may be limited (distances 1 through 7 might all produce the same
effect, 8 through 15 are equal, etc). (distance) is an integer between 0
and 255 that specifies the space between the sound and the listener. The
larger the number, the further away the sound is. Setting the distance to 0
unregisters this effect, since the data would be unchanged. If you need
more precise positional audio, consider using OpenAL for spatialized
effects instead of SDL_mixer. This is only meant to be a basic effect for
simple "3D" games.

Setting the channel to [MIX_CHANNEL_POST](MIX_CHANNEL_POST) registers this
as a posteffect, and the distance attenuation will be done to the final
mixed stream before passing it on to the audio device.

This uses the [Mix_RegisterEffect](Mix_RegisterEffect)() API internally.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

