###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_TagTrack

Assign an arbitrary tag to a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_TagTrack(MIX_Track *track, const char *tag);
```

## Function Parameters

|                          |           |                            |
| ------------------------ | --------- | -------------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to add a tag to. |
| const char *             | **tag**   | the tag to add.            |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

A tag can be any valid C string in UTF-8 encoding. It can be useful to
group tracks in various ways. For example, everything in-game might be
marked as "game", so when the user brings up the settings menu, the app can
pause all tracks involved in gameplay at once, but keep background music
and menu sound effects running.

A track can have as many tags as desired, until the machine runs out of
memory.

It's legal to add the same tag to a track more than once; the extra
attempts will report success but not change anything.

Tags can later be removed with [MIX_UntagTrack](MIX_UntagTrack)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_UntagTrack](MIX_UntagTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

