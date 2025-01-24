# SDL_InitState

A structure used for thread-safe initialization and shutdown.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
typedef struct SDL_InitState
{
    SDL_AtomicInt status;
    SDL_ThreadID thread;
    void *reserved;
} SDL_InitState;
```

## Remarks

Here is an example of using this:

```c
   static SDL_AtomicInitState init;

   bool InitSystem(void)
   {
       if (!SDL_ShouldInit(&init)) {
           // The system is initialized
           return true;
       }

       // At this point, you should not leave this function without calling SDL_SetInitialized()

       bool initialized = DoInitTasks();
       SDL_SetInitialized(&init, initialized);
       return initialized;
   }

   bool UseSubsystem(void)
   {
       if (SDL_ShouldInit(&init)) {
           // Error, the subsystem isn't initialized
           SDL_SetInitialized(&init, false);
           return false;
       }

       // Do work using the initialized subsystem

       return true;
   }

   void QuitSystem(void)
   {
       if (!SDL_ShouldQuit(&init)) {
           // The system is not initialized
           return;
       }

       // At this point, you should not leave this function without calling SDL_SetInitialized()

       DoQuitTasks();
       SDL_SetInitialized(&init, false);
   }
```

Note that this doesn't protect any resources created during initialization,
or guarantee that nobody is using those resources during cleanup. You
should use other mechanisms to protect those, if that's a concern for your
code.

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMutex](CategoryMutex)

