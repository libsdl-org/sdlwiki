###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Volume

Set the volume for a specific channel.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
int Mix_Volume(int channel, int volume);

```

## Function Parameters

|                 |                                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| **channel**     | the channel on set/query the volume on, or -1 for all channels.                 |
| **volume**      | the new volume, between 0 and [MIX_MAX_VOLUME](MIX_MAX_VOLUME), or -1 to query. |

## Return Value

Returns the previous volume. If the specified volume is -1, this returns
the current volume. If `channel` is -1, this returns the average of all
channels.

## Remarks

The volume must be between 0 (silence) and [MIX_MAX_VOLUME](MIX_MAX_VOLUME)
(full volume). Note that [MIX_MAX_VOLUME](MIX_MAX_VOLUME) is 128. Values
greater than [MIX_MAX_VOLUME](MIX_MAX_VOLUME) are clamped to
[MIX_MAX_VOLUME](MIX_MAX_VOLUME).

Specifying a negative volume will not change the current volume; as such,
this can be used to query the current volume without making changes, as
this function returns the previous (in this case, still-current) value.

If the specified channel is -1, this function sets the volume for all
channels, and returns _the average_ of all channels' volumes prior to this
call.

The default volume for a channel is [MIX_MAX_VOLUME](MIX_MAX_VOLUME) (no
attenuation).

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

