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
which the current thread is attached, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is the JNIEnv one needs to access the Java virtual machine from native
code, and is needed for many Android APIs to be usable from C.

The prototype of the function in SDL's code actually declare a void* return
type, even if the implementation returns a pointer to a JNIEnv. The
rationale being that the SDL headers can avoid including jni.h.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c++
#include <SDL3/SDL.h>
#include <jni.h>

// This example requires C++ and a custom Java method named "void showHome()"

// Calls the void showHome() method of the Java instance of the activity.
void showHome(void)
{
    // retrieve the JNI environment.
    JNIEnv* env = (JNIEnv*)SDL_GetAndroidJNIEnv();

    // retrieve the Java instance of the SDLActivity
    jobject activity = (jobject)SDL_GetAndroidActivity();

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

- [SDL_GetAndroidActivity](SDL_GetAndroidActivity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

