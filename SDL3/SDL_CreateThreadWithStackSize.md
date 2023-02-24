###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateThreadWithStackSize

Create a new thread with a specific stack size.

## Syntax

```c
extern DECLSPEC SDL_Thread *SDLCALL
SDL_CreateThreadWithStackSize(SDL_ThreadFunction fn, const char *name, const size_t stacksize, void *data);

```

## Function Parameters

|                   |                                                                                 |
| ----------------- | ------------------------------------------------------------------------------- |
| **fn**            | the [SDL_ThreadFunction](SDL_ThreadFunction) function to call in the new thread |
| **name**          | the name of the thread                                                          |
| **stacksize**     | the size, in bytes, to allocate for the new thread stack.                       |
| **data**          | a pointer that is passed to `fn`                                                |

## Return Value

Returns an opaque pointer to the new thread object on success, NULL if the
new thread could not be created; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

SDL makes an attempt to report `name` to the system, so that debuggers can
display it. Not all platforms support this.

Thread naming is a little complicated: Most systems have very small limits
for the string length (Haiku has 32 bytes, Linux currently has 16, Visual
C++ 6.0 has _nine_!), and possibly other arbitrary rules. You'll have to
see what happens with your system's debugger. The name should be UTF-8 (but
using the naming limits of C identifiers is a better bet). There are no
requirements for thread naming conventions, so long as the string is
null-terminated UTF-8, but these guidelines are helpful in choosing a name:

https://stackoverflow.com/questions/149932/naming-conventions-for-threads

If a system imposes requirements, SDL will try to munge the string for it
(truncate, etc), but the original string contents will be available from
[SDL_GetThreadName](SDL_GetThreadName)().

The size (in bytes) of the new stack can be specified. Zero means "use the
system default" which might be wildly different between platforms. x86
Linux generally defaults to eight megabytes, an embedded device might be a
few kilobytes instead. You generally need to specify a stack that is a
multiple of the system's page size (in many cases, this is 4 kilobytes, but
check your system documentation).

In SDL 2.1, stack size will be folded into the original
[SDL_CreateThread](SDL_CreateThread) function, but for backwards
compatibility, this is currently a separate function.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_WaitThread](SDL_WaitThread)

----
[CategoryAPI](CategoryAPI)

