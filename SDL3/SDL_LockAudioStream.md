###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockAudioStream

Lock an audio stream for serialized access.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_LockAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                           |
| ------------------------------------ | ---------- | ------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | The audio stream to lock. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each [SDL_AudioStream](SDL_AudioStream) has an internal mutex it uses to
protect its data structures from threading conflicts. This function allows
an app to lock that mutex, which could be useful if registering callbacks
on this stream.

One does not need to lock a stream to use in it most cases, as the stream
manages this lock internally. However, this lock is held during callbacks,
which may run from arbitrary threads at any time, so if an app needs to
protect shared data during those callbacks, locking the stream guarantees
that the callback is not running while the lock is held.

As this is just a wrapper over [SDL_LockMutex](SDL_LockMutex) for an
internal lock; it has all the same attributes (recursive locks are allowed,
etc).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UnlockAudioStream](SDL_UnlockAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

