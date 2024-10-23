###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_UnlockAudioStream

Unlock an audio stream for serialized access.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_UnlockAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                             |
| ------------------------------------ | ---------- | --------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to unlock. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This unlocks an audio stream after a call to
[SDL_LockAudioStream](SDL_LockAudioStream).

## Thread Safety

You should only call this from the same thread that previously called
[SDL_LockAudioStream](SDL_LockAudioStream).

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_LockAudioStream](SDL_LockAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

