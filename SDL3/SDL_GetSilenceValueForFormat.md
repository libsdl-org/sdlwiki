###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSilenceValueForFormat

Get the appropriate memset value for silencing an audio format.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_GetSilenceValueForFormat(SDL_AudioFormat format);
```

## Function Parameters

|                                    |            |                                 |
| ---------------------------------- | ---------- | ------------------------------- |
| [SDL_AudioFormat](SDL_AudioFormat) | **format** | the audio data format to query. |

## Return Value

(int) Returns a byte value that can be passed to memset.

## Remarks

The value returned by this function can be used as the second argument to
memset (or [SDL_memset](SDL_memset)) to set an audio buffer in a specific
format to silence.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

