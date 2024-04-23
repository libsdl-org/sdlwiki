
# Firstly let's start by the compilation 

## cmake:

```

find_package(SDL3 QUIET)
if(NOT SDL3_FOUND)
        include(FetchContent)
        FetchContent_Declare(
                SDL
                GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
                GIT_TAG main
        #        GIT_SHALLOW TRUE
        #        GIT_PROGRESS TRUE
        )
        FetchContent_MakeAvailable(SDL)
endif()

[...]

target_link_libraries(${PROJECT_NAME} SDL3::SDL3)

```
The major things that change in a cmake is the linked library that change from "SDL2::SDL2" to "SDL3::SDL3"

# Now let's continue with your code

When compiling the error handling you can fall on some depreciation, the compilation will throw error like this:

Compilation/Sdl/Main.cpp:36:13: error: use of undeclared identifier 'SDL_FillRect_renamed_SDL_FillSurfaceRect'
            SDL_FillRect( screenSurface, NULL, SDL_MapRGB( screenSurface->format, 0xFF, 0xFF, 0xFF ) );

looking closer we can read 'SDL_FillRect_renamed_SDL_FillSurfaceRect' meaning that old name SDL_FillRect turns into SDL_FillSurfaceRect 

## Includes

- `#include <SDL2/SDL.h>` turns into <SDL3/SDL.h>

## Sources (let's give the basics change to run a default app)

- `SDL_Window *SDL_CreateWindow(const char *title, int x, int y, int w, int h, Uint32 flags)` turns into `SDL_Window *SDL_CreateWindow(const char *title, int w, int h, SDL_WindowFlags flags)`
- `int SDL_FillRect(SDL_Surface *dst, const SDL_Rect *rect, Uint32 color)` turns into `int SDL_FillSurfaceRect(SDL_Surface *dst, const SDL_Rect *rect, Uint32 color)`
- `SDL_EventType::SDL_QUIT` turns into SDL_EventType::SDL_EVENT_QUIT`

# Now let's open A window with SDL3

##Source code

CMakeList.txt
```
cmake_minimum_required(VERSION 3.24)
project(app)

set(CMAKE_CXX_STANDARD 17)

#set(SDL_VERSION "2.30.2")

find_package(SDL3 QUIET)
if(NOT SDL3_FOUND)
        include(FetchContent)
        FetchContent_Declare(
                SDL
                GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
                GIT_TAG main
        #        GIT_SHALLOW TRUE
        #        GIT_PROGRESS TRUE
        )
        FetchContent_MakeAvailable(SDL)
endif()

set(SOURCE_FILES Main.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} SDL3::SDL3)
#target_compile_options(${PROJECT_NAME} -Wall)
```

Main.cpp
```
//Using SDL and standard IO
#include <SDL3/SDL.h>
#include <stdio.h>

//Screen dimension constants
const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

int main( int argc, char* args[] )
{
    //The window we'll be rendering to
    SDL_Window* window = NULL;
    
    //The surface contained by the window
    SDL_Surface* screenSurface = NULL;

    //Initialize SDL
    if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
    {
        printf( "SDL could not initialize! SDL_Error: %s\n", SDL_GetError() );
    }
    else
    {
        //Create window
        window = SDL_CreateWindow( "SDL Tutorial", /*SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,*/ SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_MAXIMIZED);
        if( window == NULL )
        {
            printf( "Window could not be created! SDL_Error: %s\n", SDL_GetError() );
        }
         else
        {
            //Get window surface
            screenSurface = SDL_GetWindowSurface( window );

            //Fill the surface white
            SDL_FillSurfaceRect( screenSurface, NULL, SDL_MapRGB( screenSurface->format, 0xFF, 0xFF, 0xFF ) );
            
            //Update the surface
            SDL_UpdateWindowSurface( window );

            //Hack to get window to stay up
            SDL_Event e; 
            bool quit = false;
            while(quit == false){
                while( SDL_PollEvent( &e ) ){
                    if( e.type == SDL_EVENT_QUIT ) {
                        quit = true;
                    }
                }
            }
        }
    }
    //Destroy window
    SDL_DestroyWindow( window );

    //Quit SDL subsystems
    SDL_Quit();

    return 0;
}
```

## Compilation

- create a folder build/ in your project folder to keep your work clean
- move in (using`cd` for unix based)
- `cmake ..` (to call the cmake in the parent directory)
- `cmake --build .` (then build your application)
- `./app` (run your application)