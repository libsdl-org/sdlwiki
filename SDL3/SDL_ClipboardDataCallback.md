###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClipboardDataCallback

Callback function that will be called when data for the specified mime-type is requested by the OS.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
typedef const void *(SDLCALL *SDL_ClipboardDataCallback)(void *userdata, const char *mime_type, size_t *size);
```

## Function Parameters

|               |                                                           |
| ------------- | --------------------------------------------------------- |
| **userdata**  | a pointer to provided user data.                          |
| **mime_type** | the requested mime-type.                                  |
| **size**      | a pointer filled in with the length of the returned data. |

## Return Value

Returns a pointer to the data for the provided mime-type. Returning NULL or
setting length to 0 will cause no data to be sent to the "receiver". It is
up to the receiver to handle this. Essentially returning no data is more or
less undefined behavior and may cause breakage in receiving applications.
The returned data will not be freed so it needs to be retained and dealt
with internally.

## Remarks

The callback function is called with NULL as the mime_type when the
clipboard is cleared or new data is set. The clipboard is automatically
cleared in [SDL_Quit](SDL_Quit)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetClipboardData](SDL_SetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryClipboard](CategoryClipboard)

