###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_MasterVolume

Set the master volume for all channels.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_MasterVolume(int volume);
```

## Function Parameters

|     |            |                                                                                 |
| --- | ---------- | ------------------------------------------------------------------------------- |
| int | **volume** | the new volume, between 0 and [MIX_MAX_VOLUME](MIX_MAX_VOLUME), or -1 to query. |

## Return Value

(int) Returns the previous volume. If the specified volume is -1, this
returns the current volume.

## Remarks

SDL_mixer keeps a per-channel volume, a per-chunk volume, and a master
volume, and considers all three when mixing audio. This function sets the
master volume, which is applied to all playing channels when mixing.

The volume must be between 0 (silence) and [MIX_MAX_VOLUME](MIX_MAX_VOLUME)
(full volume). Note that [MIX_MAX_VOLUME](MIX_MAX_VOLUME) is 128. Values
greater than [MIX_MAX_VOLUME](MIX_MAX_VOLUME) are clamped to
[MIX_MAX_VOLUME](MIX_MAX_VOLUME).

Specifying a negative volume will not change the current volume; as such,
this can be used to query the current volume without making changes, as
this function returns the previous (in this case, still-current) value.

Note that the master volume does not affect any playing music; it is only
applied when mixing chunks. Use [Mix_VolumeMusic](Mix_VolumeMusic)() for
that.\

## Version

This function is available since SDL_mixer 2.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

