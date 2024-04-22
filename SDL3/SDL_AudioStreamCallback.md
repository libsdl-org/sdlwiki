###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioStreamCallback

A callback that fires when data passes through an [SDL_AudioStream](SDL_AudioStream).

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef void (SDLCALL *SDL_AudioStreamCallback)(void *userdata, SDL_AudioStream *stream, int additional_amount, int total_amount);
```

## Function Parameters

|                           |                                                                               |
| ------------------------- | ----------------------------------------------------------------------------- |
| **stream**                | The SDL audio stream associated with this callback.                           |
| **additional_amount**     | The amount of data, in bytes, that is needed right now.                       |
| **total_amount**          | The total amount of data requested, in bytes, that is requested or available. |
| **userdata**              | An opaque pointer provided by the app for their personal use.                 |

## Remarks

Apps can (optionally) register a callback with an audio stream that is
called when data is added with
[SDL_PutAudioStreamData](SDL_PutAudioStreamData), or requested with
[SDL_GetAudioStreamData](SDL_GetAudioStreamData).

Two values are offered here: one is the amount of additional data needed to
satisfy the immediate request (which might be zero if the stream already
has enough data queued) and the other is the total amount being requested.
In a Get call triggering a Put callback, these values can be different. In
a Put call triggering a Get callback, these values are always the same.

Byte counts might be slightly overestimated due to buffering or resampling,
and may change from call to call.

This callback is not required to do anything. Generally this is useful for
adding/reading data on demand, and the app will often put/get data as
appropriate, but the system goes on with the data currently available to it
if this callback does nothing.

## Thread Safety

This callbacks may run from any thread, so if you need to protect shared
data, you should use [SDL_LockAudioStream](SDL_LockAudioStream) to
serialize access; this lock will be held before your callback is called, so
your callback does not need to manage the lock explicitly.

## Version

This datatype is available since SDL 3.0.0.

## See Also

* [SDL_SetAudioStreamGetCallback](SDL_SetAudioStreamGetCallback)
* [SDL_SetAudioStreamPutCallback](SDL_SetAudioStreamPutCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

