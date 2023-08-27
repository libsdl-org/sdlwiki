###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamPutCallback

Set a callback that runs when data is added to an audio stream.

## Syntax

```c
int SDL_SetAudioStreamPutCallback(SDL_AudioStream *stream, SDL_AudioStreamCallback callback, void *userdata);

```

## Function Parameters

|                  |                                                                      |
| ---------------- | -------------------------------------------------------------------- |
| **stream**       | the audio stream to set the new callback on.                         |
| **callback**     | the new callback function to call when data is added to the stream.  |
| **userdata**     | an opaque pointer provided to the callback for its own personal use. |

## Return Value

Returns 0 on success, -1 on error. This only fails if `stream` is NULL.

## Remarks

This callback is called _after_ the data is added to the stream, giving the
callback the chance to obtain it immediately.

The callback can (optionally) call
[SDL_GetAudioStreamData](SDL_GetAudioStreamData)() to obtain audio from the
stream during this call.

The callback's `approx_request` argument is how many bytes of _converted_
data (in the stream's output format) was provided by the caller, although
this may underestimate a little for safety. This value might be less than
what is currently available in the stream, if data was already there, and
might be less than the caller provided if the stream needs to keep a buffer
to aid in resampling. Which means the callback may be provided with zero
bytes, and a different amount on each call.

The callback may call
[SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable) to see the total
amount currently available to read from the stream, instead of the total
provided by the current call.

The callback is not required to obtain all data. It is allowed to read less
or none at all. Anything not read now simply remains in the stream for
later access.

Clearing or flushing an audio stream does not call this callback.

This function obtains the stream's lock, which means any existing callback
(get or put) in progress will finish running before setting the new
callback.

Setting a NULL function turns off the callback.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetAudioStreamGetCallback](SDL_SetAudioStreamGetCallback)

----
[CategoryAPI](CategoryAPI)

