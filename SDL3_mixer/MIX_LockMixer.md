###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_LockMixer

Lock a mixer by obtaining its internal mutex.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_LockMixer(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                                 |
| ------------------------ | --------- | ------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to lock. May be NULL. |

## Remarks

While locked, the mixer will not be able to mix more audio or change its
internal state in another thread. Those other threads will block until the
mixer is unlocked again.

Under the hood, this function calls SDL_LockMutex(), so all the same rules
apply: the lock can be recursive, it must be unlocked the same number of
times from the same thread that locked it, etc.

Just about every SDL_mixer API _also_ locks the mixer while doing its work,
as does the SDL audio device thread while actual mixing is in progress, so
basic use of this library never requires the app to explicitly lock the
device to be thread safe. There are two scenarios where this can be useful,
however:

- The app has a provided a callback that the mixing thread might call, and
  there is some app state that needs to be protected against race
  conditions as changes are made and mixing progresses simultaneously. Any
  lock can be used for this, but this is a conveniently-available lock.
- The app wants to make multiple, atomic changes to the mix. For example,
  to start several tracks at the exact same moment, one would lock the
  mixer, call [MIX_PlayTrack](MIX_PlayTrack) multiple times, and then
  unlock again; all the tracks will start mixing on the same sample frame.

Do not lock the mixer for significant amounts of time, or it can cause
audio dropouts. Just do simply things quickly and unlock again.

Locking a NULL mixer is a safe no-op.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

