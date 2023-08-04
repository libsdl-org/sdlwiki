###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockAudioStream

Unlock an audio stream for serialized access.

## Syntax

```c
int SDL_UnlockAudioStream(SDL_AudioStream *stream);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **stream**     | The audio stream to unlock. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This unlocks an audio stream after a call to
[SDL_LockAudioStream](SDL_LockAudioStream).

## Thread Safety

You should only call this from the same thread that previously called
[SDL_LockAudioStream](SDL_LockAudioStream).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockAudioStream](SDL_LockAudioStream)
* [SDL_SetAudioStreamPutCallback](SDL_SetAudioStreamPutCallback)
* [SDL_SetAudioStreamGetCallback](SDL_SetAudioStreamGetCallback)

----
[CategoryAPI](CategoryAPI)

