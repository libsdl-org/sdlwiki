###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_VolumeMusic

Set the volume for the music channel.

## Syntax

```c
int Mix_VolumeMusic(int volume);

```

## Function Parameters

|                |                                                                                 |
| -------------- | ------------------------------------------------------------------------------- |
| **volume**     | the new volume, between 0 and [MIX_MAX_VOLUME](MIX_MAX_VOLUME.md), or -1 to query. |

## Return Value

Returns the previous volume. If the specified volume is -1, this returns
the current volume.

## Remarks

The volume must be between 0 (silence) and [MIX_MAX_VOLUME](MIX_MAX_VOLUME.md)
(full volume). Note that [MIX_MAX_VOLUME](MIX_MAX_VOLUME.md) is 128. Values
greater than [MIX_MAX_VOLUME](MIX_MAX_VOLUME.md) are clamped to
[MIX_MAX_VOLUME](MIX_MAX_VOLUME.md).

Specifying a negative volume will not change the current volume; as such,
this can be used to query the current volume without making changes, as
this function returns the previous (in this case, still-current) value.

The default volume for music is [MIX_MAX_VOLUME](MIX_MAX_VOLUME.md) (no
attenuation).

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
