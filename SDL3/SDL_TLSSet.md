###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_TLSSet

Set the current thread's value associated with a thread local storage ID.

## Syntax

```c
int SDL_TLSSet(SDL_TLSID id, const void *value, void (SDLCALL *destructor)(void*));

```

## Function Parameters

|                    |                                                            |
| ------------------ | ---------------------------------------------------------- |
| **id**             | the thread local storage ID                                |
| **value**          | the value to associate with the ID for the current thread  |
| **destructor**     | a function called when the thread exits, to free the value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The function prototype for `destructor` is:

```c
void destructor(void *value)
```

where its parameter `value` is what was passed as `value` to
[SDL_TLSSet](SDL_TLSSet.md)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_TLSCreate](SDL_TLSCreate.md)
* [SDL_TLSGet](SDL_TLSGet.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryThread](CategoryThread.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
