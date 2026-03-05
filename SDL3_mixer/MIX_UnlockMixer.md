###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_UnlockMixer

Unlock a mixer previously locked by a call to [MIX_LockMixer](MIX_LockMixer)().

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_UnlockMixer(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                                   |
| ------------------------ | --------- | --------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to unlock. May be NULL. |

## Remarks

While locked, the mixer will not be able to mix more audio or change its
internal state another thread. Those other threads will block until the
mixer is unlocked again.

Under the hood, this function calls SDL_LockMutex(), so all the same rules
apply: the lock can be recursive, it must be unlocked the same number of
times from the same thread that locked it, etc.

Unlocking a NULL mixer is a safe no-op.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

