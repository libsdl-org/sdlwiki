###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_TLSGet

Get the current thread's value associated with a thread local storage ID.

## Syntax

```c
void * SDL_TLSGet(SDL_TLSID id);

```

## Function Parameters

|            |                             |
| ---------- | --------------------------- |
| **id**     | the thread local storage ID |

## Return Value

Returns the value associated with the ID for the current thread or NULL if
no value has been set; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_TLSCreate](SDL_TLSCreate.md)
* [SDL_TLSSet](SDL_TLSSet.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryThread](CategoryThread.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
