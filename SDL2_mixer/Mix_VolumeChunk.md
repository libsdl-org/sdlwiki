###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_VolumeChunk

Set the volume for a specific chunk.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
int Mix_VolumeChunk(Mix_Chunk *chunk, int volume);

```

## Function Parameters

|                |                                                                                 |
| -------------- | ------------------------------------------------------------------------------- |
| **chunk**      | the chunk whose volume to adjust.                                               |
| **volume**     | the new volume, between 0 and [MIX_MAX_VOLUME](MIX_MAX_VOLUME), or -1 to query. |

## Return Value

Returns the previous volume. If the specified volume is -1, this returns
the current volume. If `chunk` is NULL, this returns -1.

## Remarks

In addition to channels having a volume setting, individual chunks also
maintain a separate volume. Both values are considered when mixing, so both
affect the final attenuation of the sound. This lets an app adjust the
volume for all instances of a sound in addition to specific instances of
that sound.

The volume must be between 0 (silence) and [MIX_MAX_VOLUME](MIX_MAX_VOLUME)
(full volume). Note that [MIX_MAX_VOLUME](MIX_MAX_VOLUME) is 128. Values
greater than [MIX_MAX_VOLUME](MIX_MAX_VOLUME) are clamped to
[MIX_MAX_VOLUME](MIX_MAX_VOLUME).

Specifying a negative volume will not change the current volume; as such,
this can be used to query the current volume without making changes, as
this function returns the previous (in this case, still-current) value.

The default volume for a chunk is [MIX_MAX_VOLUME](MIX_MAX_VOLUME) (no
attenuation).

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

