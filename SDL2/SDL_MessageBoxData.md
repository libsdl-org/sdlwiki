###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_MessageBoxData

MessageBox structure containing title, text, window, etc.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxData
{
    Uint32 flags;                       /**< ::SDL_MessageBoxFlags */
    SDL_Window *window;                 /**< Parent window, can be NULL */
    const char *title;                  /**< UTF-8 title */
    const char *message;                /**< UTF-8 message text */

    int numbuttons;
    const SDL_MessageBoxButtonData *buttons;

    const SDL_MessageBoxColorScheme *colorScheme;   /**< ::SDL_MessageBoxColorScheme, can be NULL to use system settings */
} SDL_MessageBoxData;
```

## Data Fields

{|
| Uint32                               
| '''flags'''       
| an [[SDL_MessageBoxFlags]] 
|-
| SDL_Window*                          
| '''window'''      
| an parent window, can be NULL 
|-
| const char*                          
| '''title'''       
| an UTF-8 title 
|-
| const char*                          
| '''message'''     
| an UTF-8 message text 
|-
| int                                  
| '''numbuttons'''  
| the number of buttons 
|-
| const [[SDL_MessageBoxButtonData]]*  
| '''buttons'''     
| an array of [[SDL_MessageBoxButtonData]] with length of '''numbuttons''' 
|-
| const [[SDL_MessageBoxColorScheme]]* 
| '''colorScheme''' 
| an [[SDL_MessageBoxColorScheme]], can be NULL to use system settings 
|}

## Related Enumerations

:[[SDL_MessageBoxFlags]]

## Related Structures

:[[SDL_MessageBoxButtonData]]
:[[SDL_MessageBoxColorScheme]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryVideo](CategoryVideo), [CategoryDraft](CategoryDraft)


