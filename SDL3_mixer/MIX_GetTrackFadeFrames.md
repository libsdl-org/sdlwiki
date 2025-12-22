###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackFadeFrames

Query whether a given track is fading.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_GetTrackFadeFrames(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(Sint64) Returns less than 0 if the track is fading out, greater than 0 if
fading in, zero otherwise.

## Remarks

This specifically checks if the track is _not stopped_ (paused or playing),
and it is fading in or out, and returns the number of frames remaining in
the fade.

If fading out, the returned value will be negative. When fading in, the
returned value will be positive. If not fading, this function returns zero.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns 0, but there is no mechanism to distinguish errors from
tracks that aren't fading.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

