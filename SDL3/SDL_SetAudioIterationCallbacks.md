# SDL_SetAudioIterationCallbacks

Set callbacks that fire around a new iteration of audio device processing.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_SetAudioIterationCallbacks(SDL_AudioDeviceID devid, SDL_AudioIterationCallback start, SDL_AudioIterationCallback end, void *userdata);
```

## Function Parameters

|                                                          |              |                                                                             |
| -------------------------------------------------------- | ------------ | --------------------------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID)                   | **devid**    | the ID of an opened audio device.                                           |
| [SDL_AudioIterationCallback](SDL_AudioIterationCallback) | **start**    | a callback function to be called at the start of an iteration. Can be NULL. |
| [SDL_AudioIterationCallback](SDL_AudioIterationCallback) | **end**      | a callback function to be called at the end of an iteration. Can be NULL.   |
| void *                                                   | **userdata** | app-controlled pointer passed to callback. Can be NULL.                     |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Two callbacks are provided here: one that runs when a device is about to
process its bound audio streams, and another that runs when the device has
finished processing them.

These callbacks can run at any time, and from any thread; if you need to
serialize access to your app's data, you should provide and use a mutex or
other synchronization device.

Generally these callbacks are used to apply state that applies to multiple
bound audio streams, with a guarantee that the audio device's thread isn't
halfway through processing them. Generally a finer-grained lock through
[SDL_LockAudioStream](SDL_LockAudioStream)() is more appropriate.

The callbacks are extremely time-sensitive; the callback should do the
least amount of work possible and return as quickly as it can. The longer
the callback runs, the higher the risk of audio dropouts or other problems.

This function will block until the audio device is in between iterations,
so any existing callback that might be running will finish before this
function sets the new callback and returns.

Physical devices do not accept these callbacks, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.

Setting a NULL callback function disables any previously-set callback.
Either callback may be NULL, and the same callback is permitted to be used
for both.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

