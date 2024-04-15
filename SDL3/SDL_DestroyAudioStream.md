###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyAudioStream

Free an audio stream.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_DestroyAudioStream(SDL_AudioStream *stream);

```

## Function Parameters

|                |                          |
| -------------- | ------------------------ |
| **stream**     | The audio stream to free |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_CreateAudioStream](SDL_CreateAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

