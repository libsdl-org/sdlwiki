###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidGetActivity

Retrieve the Java instance of the Android activity class.

## Syntax

```c
void * SDL_AndroidGetActivity(void);

```

## Return Value

Returns the jobject representing the instance of the Activity class of the
Android application, or NULL on error.

## Remarks

The prototype of the function in SDL's code actually declares a void*
return type, even if the implementation returns a jobject. The rationale
being that the SDL headers can avoid including jni.h.

The jobject returned by the function is a local reference and must be
released by the caller. See the PushLocalFrame() and PopLocalFrame() or
DeleteLocalRef() functions of the Java native interface:

https://docs.oracle.com/javase/1.5.0/docs/guide/jni/spec/functions.html

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AndroidGetJNIEnv](SDL_AndroidGetJNIEnv.md)

----
[CategoryAPI](CategoryAPI.md)
