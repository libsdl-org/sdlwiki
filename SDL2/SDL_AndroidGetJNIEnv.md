###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidGetJNIEnv

Get the Android Java Native Interface Environment of the current thread.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
void * SDL_AndroidGetJNIEnv(void);

```

## Return Value

Returns a pointer to Java native interface object (JNIEnv) to which the
current thread is attached, or 0 on error.

## Remarks

This is the JNIEnv one needs to access the Java virtual machine from native
code, and is needed for many Android APIs to be usable from C.

The prototype of the function in SDL's code actually declare a void* return
type, even if the implementation returns a pointer to a JNIEnv. The
rationale being that the SDL headers can avoid including jni.h.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AndroidGetActivity](SDL_AndroidGetActivity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

