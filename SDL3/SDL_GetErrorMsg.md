###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetErrorMsg

Get the last error message that was set for the current thread.

## Syntax

```c
char * SDL_GetErrorMsg(char *errstr, int maxlen);

```

## Function Parameters

|                |                                                                                  |
| -------------- | -------------------------------------------------------------------------------- |
| **errstr**     | A buffer to fill with the last error message that was set for the current thread |
| **maxlen**     | The size of the buffer pointed to by the errstr parameter                        |

## Return Value

Returns the pointer passed in as the `errstr` parameter.

## Remarks

This allows the caller to copy the error string into a provided buffer, but
otherwise operates exactly the same as [SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetError](SDL_GetError)

----
[CategoryAPI](CategoryAPI)

