###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadFunction

Look up the address of the named function in a shared object.

## Syntax

```c
SDL_FunctionPointer SDL_LoadFunction(void *handle, const char *name);

```

## Function Parameters

|                |                                                                             |
| -------------- | --------------------------------------------------------------------------- |
| **handle**     | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject.md)() |
| **name**       | the name of the function to look up                                         |

## Return Value

Returns a pointer to the function or NULL if there was an error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function pointer is no longer valid after calling
[SDL_UnloadObject](SDL_UnloadObject.md)().

This function can only look up C function names. Other languages may have
name mangling and intrinsic language support that varies from compiler to
compiler.

Make sure you declare your function pointers with the same calling
convention as the actual library function. Your code will crash
mysteriously if you do not do this.

If the requested function doesn't exist, NULL is returned.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"

/* Variable declaration */
void* myHandle = NULL;
char* myFunctionName = "myFancyFunction";
void (*myFancyFunction)(int anInt);

/* Dynamically load mylib.so */
myHandle = SDL_LoadObject("mylib.so");

/* Load the exported function from mylib.so
 * The exported function has the following prototype
 * void myFancyFunction(int anInt);
 */
myFancyFunction = (void (*)(int))SDL_LoadFunction(myHandle, myFunctionName);

/* Call myFancyFunction with a random integer */
if (myFancyFunction != NULL) {
    myFancyFunction(15);
} else {
    /* Error handling here */
}
```

## Related Functions

* [SDL_LoadObject](SDL_LoadObject.md)
* [SDL_UnloadObject](SDL_UnloadObject.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySharedObject](CategorySharedObject.md)
