###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetAssertionHandler

Get the current assertion handler.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_assert.h)

## Syntax

```c
SDL_AssertionHandler SDL_GetAssertionHandler(void **puserdata);

```

## Function Parameters

|                   |                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **puserdata**     | pointer which is filled with the "userdata" pointer that was passed to [SDL_SetAssertionHandler](SDL_SetAssertionHandler)() |

## Return Value

Returns the [SDL_AssertionHandler](SDL_AssertionHandler) that is called
when an assert triggers.

## Remarks

This returns the function pointer that is called when an assertion is
triggered. This is either the value last passed to
[SDL_SetAssertionHandler](SDL_SetAssertionHandler)(), or if no
application-specified function is set, is equivalent to calling
[SDL_GetDefaultAssertionHandler](SDL_GetDefaultAssertionHandler)().

The parameter `puserdata` is a pointer to a void*, which will store the
"userdata" pointer that was passed to
[SDL_SetAssertionHandler](SDL_SetAssertionHandler)(). This value will
always be NULL for the default handler. If you don't care about this data,
it is safe to pass a NULL pointer to this function to ignore it.

## Version

This function is available since SDL 2.0.2.

## See Also

* [SDL_SetAssertionHandler](SDL_SetAssertionHandler)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

