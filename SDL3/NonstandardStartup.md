# Starting up SDL in unusual ways

## Target audience

This is almost certainly _not_ the document you should read. If you have an application or game in C or C++ that uses SDL, you should just use [the normal app entry points](README-main-functions).

If you are managing an app that uses SDL in a strange way, or perhaps a scripting language maintainer that wants to integrate tightly with SDL, this is probably for you.


## Normal applications written in C/C++

Traditional apps will `#include <SDL3/SDL_main.h>` and provide either a standard C `main` function, or use the "main callbacks" (SDL_AppInit, SDL_AppEvent, SDL_AppIterate, and SDL_AppQuit). These are covered in [README-main-functions](README-main-functions). However, it could be instructive to study [SDL_main.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h) and [SDL_main_impl.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main_impl.h) to see how the C implementation operates.


## If you can't include `SDL3/SDL_main.h`

If your application is written in a language other than C/C++, and must manage the application's entry point directly, it is recommended that you call [`SDL_RunApp`](SDL_RunApp)() from your actual entry point, passing in a C-callable callback function that constitutes your application's "main function" as the third argument. `SDL_RunApp()` initializes platform-specific details before calling the callback and is the best way to ensure that your application will work on as many platforms as possible.

This example is written in C for clarity, but any language that can call into C, and provide C-callable function pointers, can work.

```c
// Include 'SDL3/SDL_main.h' without redefining the main function by defining SDL_MAIN_HANDLED.
#define SDL_MAIN_HANDLED
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

// Native non-standard main function
int main(int argc, char *argv[], char *envp[])
{
    // The first and second arguments, 'argc' and 'argv', can be
    // ignored if you don't care about command-line arguments.
    // The fourth argument, 'reserved', is currently unused and must be NULL!
    return SDL_RunApp(argc, argv, my_runapp_callback, NULL);
}

// Callback passed to SDL_RunApp
int SDLCALL my_runapp_callback(int argc, char *argv[])
{
    // Your app logic should live in scope of this function.
}
```

If you also want to use SDL's main callbacks system, the callback that you pass to `SDL_RunApp()` should in turn call [`SDL_EnterAppMainCallbacks`](SDL_EnterAppMainCallbacks)(), passing in your application's init, iterate, event and quit callbacks.

```c
#define SDL_MAIN_HANDLED
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

int main(int argc, char *argv[], char *envp[])
{
    return SDL_RunApp(argc, argv, my_runapp_callback, NULL);
}

int SDLCALL my_runapp_callback(int argc, char *argv[])
{
    // Forward the received 'argc' and 'argv'
    return SDL_EnterAppMainCallbacks(
        argc, argv,
        my_init_callback, my_iterate_callback, my_event_callback, my_quit_callback
    );
}

SDL_AppResult SDLCALL my_init_callback(void **appstate, int argc, char *argv[]) { /* ... */ }

SDL_AppResult SDLCALL my_iterate_callback(void *appstate) { /* ... */ }

SDL_AppResult SDLCALL my_event_callback(void *appstate, SDL_Event *event) { /* ... */ }

void SDLCALL my_quit_callback(void *appstate, SDL_AppResult result) { /* ... */ }
```

Any callback functions passed to `SDL_RunApp()`/`SDL_EnterAppMainCallbacks()` must be defined with a calling convention equivalent to `SDLCALL`.

If you don't let SDL redefine main, and you don't use `SDL_RunApp()`, SDL will not initialize any platform-specific details, and your app might not work correctly on certain platforms. In this case, you will need to perform all platform initialization yourself, and then inform SDL that the initialization work is done by calling `SDL_SetMainReady()` before initializing any SDL subsystems. While many platforms need only minor (or no) initialization through SDL_RunApp, this can be a complicated process on some targets, so it can be desirable for SDL to handle it for you.

Be aware that some platforms, for example Android, may have additional requirements beyond just calling `SDL_RunApp()`. When in doubt, the best advice is to carefully read and try to understand the parts of SDL's source code that deal with application entry points and replicate them to the best of your ability in the language of your choosing.

## SDL_RunApp blocks

Note that `my_runapp_callback`, in those examples, is intended to return when the application is terminating (in the same way that returning from main() would), and that SDL_RunApp() will return after that. Therefore, SDL_RunApp() blocks for the lifetime of the app.

If you have a platform that can't tolerate this at all, things can get tricky. You might need to provide an SDL_RunApp callback that uses an equivalent of longjmp() or throws an exception to return control to the caller once SDL has initialized (Emscripten does something like this, in fact), or avoid using SDL_RunApp at all and deal with platform quirks directly.

## Using SDL as an external module

There are times when SDL will be used from a scripting language module, either as a straightfoward binding, where the language can just call SDL APIs directly, or internally as part of some other module. Perhaps it's being used by a plugin to an otherwise-unrelated app. In both cases, SDL isn't even _loaded_ when the process starts, and is not expected to control app startup.

In these cases, SDL _will_ generally function normally. You should, after loading the library, call SDL_SetMainReady() from your process's main thread. Since SDL isn't handling startup, you don't need to manage command line arguments, etc. The esoteric platform-specific startup work that SDL provides will not be done, but the expectation is that the base app will be responsible for this; if you're running Python on a PlayStation 2, the Python interpreter should know enough about the PS2 to handle those things; failing that, you should consult [SDL's "main" code](https://github.com/libsdl-org/SDL/tree/main/src/main) for any surprises as you bootstrap on new targets.


