###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_UntagTrack

Remove an arbitrary tag from a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_UntagTrack(MIX_Track *track, const char *tag);
```

## Function Parameters

|                          |           |                                       |
| ------------------------ | --------- | ------------------------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track from which to remove a tag. |
| const char *             | **tag**   | the tag to remove.                    |

## Remarks

A tag can be any valid C string in UTF-8 encoding. It can be useful to
group tracks in various ways. For example, everything in-game might be
marked as "game", so when the user brings up the settings menu, the app can
pause all tracks involved in gameplay at once, but keep background music
and menu sound effects running.

It's legal to remove a tag that the track doesn't have; this function
doesn't report errors, so this simply does nothing.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TagTrack](MIX_TagTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

