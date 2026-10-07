# SDL_LockAudioStream

Lock an audio stream for serialized access.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_LockAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                           |
| ------------------------------------ | ---------- | ------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to lock. |

## Return Value

(bool) Returns true on success or false on failure; call
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

Note that when the stream's callback runs, SDL is holding both an internal
mutex for the audio device and the stream's lock, in that order. Which is
to say: while this function can protect arbitrary data, calling into some
SDL audio functions while holding this lock may cause a deadlock--the app
holds this lock, and then calls into something that wants to obtain the
device lock, in the opposite order that SDL's audio thread obtained them.
Therefore, best practice is to use this function to protect simple app data
against the audio callback, and be careful about what SDL functions one
calls while locked outside of the callback.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_UnlockAudioStream](SDL_UnlockAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

