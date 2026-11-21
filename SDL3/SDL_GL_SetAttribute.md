# SDL_GL_SetAttribute

Set an OpenGL window attribute before context creation.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GL_SetAttribute(SDL_GLAttr attr, int value);
```

## Function Parameters

|                          |           |                                                       |
| ------------------------ | --------- | ----------------------------------------------------- |
| [SDL_GLAttr](SDL_GLAttr) | **attr**  | an enum value specifying the OpenGL attribute to set. |
| int                      | **value** | the desired value for the attribute.                  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets the OpenGL attribute `attr` to `value`. The requested
attributes should be set before creating an OpenGL context. You should use
[SDL_GL_GetAttribute](SDL_GL_GetAttribute)() to check the values after
creating the OpenGL context, since the values obtained can differ from the
requested ones.

SDL's GL attributes are global state, and while you can use related
functions from any thread, you should only use them to prepare a single GL
context at a time.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
SDL_Window *window;
SDL_GLContext context;

SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

window = SDL_CreateWindow("OpenGL Window", 640, 480, SDL_WINDOW_OPENGL);
if (!window) {
    fprintf(stderr, "Couldn't create window: %s\n", SDL_GetError());
    return 1;
}

context = SDL_GL_CreateContext(window);
if (!context) {
    fprintf(stderr, "Couldn't create context: %s\n", SDL_GetError());
    return 1;
}

int r, g, b;
SDL_GL_GetAttribute(SDL_GL_RED_SIZE, &r);
SDL_GL_GetAttribute(SDL_GL_GREEN_SIZE, &g);
SDL_GL_GetAttribute(SDL_GL_BLUE_SIZE, &b);

printf("Red size: %d, Green size: %d, Blue size: %d\n", r, g, b);
```

## See Also

- [SDL_GL_CreateContext](SDL_GL_CreateContext)
- [SDL_GL_GetAttribute](SDL_GL_GetAttribute)
- [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

