###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetPanning

Set the panning of a channel.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_SetPanning(int channel, Uint8 left, Uint8 right);
```

## Function Parameters

|       |             |                                                                   |
| ----- | ----------- | ----------------------------------------------------------------- |
| int   | **channel** | The mixer channel to pan or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |
| Uint8 | **left**    | Volume of stereo left channel, 0 is silence, 255 is full volume.  |
| Uint8 | **right**   | Volume of stereo right channel, 0 is silence, 255 is full volume. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The left and right channels are specified as integers between 0 and 255,
quietest to loudest, respectively.

Technically, this is just individual volume control for a sample with two
(stereo) channels, so it can be used for more than just panning. If you
want real panning, call it like this:

```c
Mix_SetPanning(channel, left, 255 - left);
```

Setting `channel` to [MIX_CHANNEL_POST](MIX_CHANNEL_POST) registers this as
a posteffect, and the panning will be done to the final mixed stream before
passing it on to the audio device.

This uses the [Mix_RegisterEffect](Mix_RegisterEffect)() API internally,
and returns without registering the effect function if the audio device is
not configured for stereo output. Setting both `left` and `right` to 255
causes this effect to be unregistered, since that is the data's normal
state.

Note that an audio device in mono mode is a no-op, but this call will
return successful in that case. Error messages can be retrieved from
[Mix_GetError](Mix_GetError)().

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [Mix_SetPosition](Mix_SetPosition)
- [Mix_SetDistance](Mix_SetDistance)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

