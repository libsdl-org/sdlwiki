###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSilenceValueForFormat

Get the appropriate memset value for silencing an audio format.

## Syntax

```c
int SDL_GetSilenceValueForFormat(SDL_AudioFormat format);

```

## Function Parameters

|                |                                 |
| -------------- | ------------------------------- |
| **format**     | the audio data format to query. |

## Return Value

Returns A byte value that can be passed to memset.

## Remarks

The value returned by this function can be used as the second argument to
memset (or [SDL_memset](SDL_memset)) to set an audio buffer in a specific
format to silence.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

