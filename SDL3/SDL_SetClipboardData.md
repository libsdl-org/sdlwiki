###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetClipboardData

Offer clipboard data to the OS 

## Syntax

```c
int SDL_SetClipboardData(SDL_ClipboardDataCallback callback, SDL_ClipboardCleanupCallback cleanup, void *userdata, const char **mime_types, size_t num_mime_types);

```

## Function Parameters

|                        |                                                                      |
| ---------------------- | -------------------------------------------------------------------- |
| **callback**           | A function pointer to the function that provides the clipboard data  |
| **cleanup**            | A function pointer to the function that cleans up the clipboard data |
| **userdata**           | An opaque pointer that will be forwarded to the callbacks            |
| **mime_types**         | A list of mime-types that are being offered                          |
| **num_mime_types**     | The number of mime-types in the mime_types list                      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Tell the operating system that the application is offering clipboard data
for each of the proivded mime-types. Once another application requests the
data the callback function will be called allowing it to generate and
respond with the data for the requested mime-type.

The size of text data does not include any terminator, and the text does
not need to be null terminated (e.g. you can directly copy a portion of a
document)

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_ClipboardDataCallback](SDL_ClipboardDataCallback)
* [SDL_SetClipboardData](SDL_SetClipboardData)
* [SDL_GetClipboardData](SDL_GetClipboardData)
* [SDL_HasClipboardData](SDL_HasClipboardData)

----
[CategoryAPI](CategoryAPI)

