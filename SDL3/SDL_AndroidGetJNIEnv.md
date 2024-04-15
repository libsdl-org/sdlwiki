###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_AndroidGetJNIEnv

Get the Android Java Native Interface Environment of the current thread.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h), but apps should use `#include <SDL3/SDL.h>`

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

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"
#include <jni.h>

// This example requires C++ and a custom Java method named "void showHome()"

// Calls the void showHome() method of the Java instance of the activity.
void showHome(void)
{
    // retrieve the JNI environment.
    JNIEnv* env = (JNIEnv*)SDL_AndroidGetJNIEnv();

    // retrieve the Java instance of the SDLActivity
    jobject activity = (jobject)SDL_AndroidGetActivity();

    // find the Java class of the activity. It should be SDLActivity or a subclass of it.
    jclass clazz(env->GetObjectClass(activity));

    // find the identifier of the method to call
    jmethodID method_id = env->GetMethodID(clazz, "showHome", "()V");

    // effectively call the Java method
    env->CallVoidMethod(activity, method_id);

    // clean up the local references.
    env->DeleteLocalRef(activity);
    env->DeleteLocalRef(clazz);

    // Warning (and discussion of implementation details of SDL for Android):
    // Local references are automatically deleted if a native function called
    // from Java side returns. For SDL this native function is main() itself.
    // Therefore references need to be manually deleted because otherwise the
    // references will first be cleaned if main() returns (application exit).
}
```

## See Also

* [SDL_AndroidGetActivity](SDL_AndroidGetActivity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem), [CategoryDraft](CategoryDraft), [CategoryAndroid](CategoryAndroid)


