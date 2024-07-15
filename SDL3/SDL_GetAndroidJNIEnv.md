###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAndroidJNIEnv

Get the Android Java Native Interface Environment of the current thread.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
void * SDL_GetAndroidJNIEnv(void);
```

## Return Value

(void *) Returns a pointer to Java native interface object (JNIEnv) to
which the current thread is attached, or 0 on error.

## Remarks

This is the JNIEnv one needs to access the Java virtual machine from native
code, and is needed for many Android APIs to be usable from C.

The prototype of the function in SDL's code actually declare a void* return
type, even if the implementation returns a pointer to a JNIEnv. The
rationale being that the SDL headers can avoid including jni.h.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAndroidActivity](SDL_GetAndroidActivity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

