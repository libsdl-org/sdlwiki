# SDL_SetAudioStreamPutCallback

Set a callback that runs when data is added to an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_SetAudioStreamPutCallback(SDL_AudioStream *stream, SDL_AudioStreamCallback callback, void *userdata);
```

## Function Parameters

|                                                    |              |                                                                      |
| -------------------------------------------------- | ------------ | -------------------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) *               | **stream**   | the audio stream to set the new callback on.                         |
| [SDL_AudioStreamCallback](SDL_AudioStreamCallback) | **callback** | the new callback function to call when data is added to the stream.  |
| void *                                             | **userdata** | an opaque pointer provided to the callback for its own personal use. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information. This only fails if
`stream` is NULL.

## Remarks

This callback is called _after_ the data is added to the stream, giving the
callback the chance to obtain it immediately.

The callback can (optionally) call
[SDL_GetAudioStreamData](SDL_GetAudioStreamData)() to obtain audio from the
stream during this call.

The callback's `additional_amount` argument is how many bytes of
_converted_ data (in the stream's output format) was provided by the
caller, although this may underestimate a little for safety. This value
might be less than what is currently available in the stream, if data was
already there, and might be less than the caller provided if the stream
needs to keep a buffer to aid in resampling. Which means the callback may
be provided with zero bytes, and a different amount on each call.

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

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetAudioStreamGetCallback](SDL_SetAudioStreamGetCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

