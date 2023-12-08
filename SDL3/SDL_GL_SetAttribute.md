###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_SetAttribute

Set an OpenGL window attribute before window creation.

## Syntax

```c
int SDL_GL_SetAttribute(SDL_GLattr attr, int value);

```

## Function Parameters

|               |                                                                               |
| ------------- | ----------------------------------------------------------------------------- |
| **attr**      | an [SDL_GLattr](SDL_GLattr.md) enum value specifying the OpenGL attribute to set |
| **value**     | the desired value for the attribute                                           |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function sets the OpenGL attribute `attr` to `value`. The requested
attributes should be set before creating an OpenGL window. You should use
[SDL_GL_GetAttribute](SDL_GL_GetAttribute.md)() to check the values after
creating the OpenGL context, since the values obtained can differ from the
requested ones.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_Window *window;
SDL_GLContext context;

SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 5);
SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16);
SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

window = SDL_CreateWindow("OpenGL Window", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_OPENGL);
if (!window) {
    fprintf(stderr, "Couldn't create window: %s\n", SDL_GetError());
    return;
}

context = SDL_GL_CreateContext(window);
if (!context) {
    fprintf(stderr, "Couldn't create context: %s\n", SDL_GetError());
    return;
}

int r, g, b;
SDL_GL_GetAttribute(SDL_GL_RED_SIZE, &r);
SDL_GL_GetAttribute(SDL_GL_GREEN_SIZE, &g);
SDL_GL_GetAttribute(SDL_GL_BLUE_SIZE, &b);

printf("Red size: %d, Green size: %d, Blue size: %d\n", r, g, b);
```

## Related Functions

* [SDL_GL_GetAttribute](SDL_GL_GetAttribute.md)
* [SDL_GL_ResetAttributes](SDL_GL_ResetAttributes.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
