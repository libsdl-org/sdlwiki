# SDL_SystemCursor

Cursor types for [SDL_CreateSystemCursor](SDL_CreateSystemCursor)().

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
typedef enum SDL_SystemCursor
{
    SDL_SYSTEM_CURSOR_DEFAULT,      /**< Default cursor. Usually an arrow. */
    SDL_SYSTEM_CURSOR_TEXT,         /**< Text selection. Usually an I-beam. */
    SDL_SYSTEM_CURSOR_WAIT,         /**< Wait. Usually an hourglass or watch or spinning ball. */
    SDL_SYSTEM_CURSOR_CROSSHAIR,    /**< Crosshair. */
    SDL_SYSTEM_CURSOR_PROGRESS,     /**< Program is busy but still interactive. Usually it's WAIT with an arrow. */
    SDL_SYSTEM_CURSOR_NWSE_RESIZE,  /**< Double arrow pointing northwest and southeast. */
    SDL_SYSTEM_CURSOR_NESW_RESIZE,  /**< Double arrow pointing northeast and southwest. */
    SDL_SYSTEM_CURSOR_EW_RESIZE,    /**< Double arrow pointing west and east. */
    SDL_SYSTEM_CURSOR_NS_RESIZE,    /**< Double arrow pointing north and south. */
    SDL_SYSTEM_CURSOR_MOVE,         /**< Four pointed arrow pointing north, south, east, and west. */
    SDL_SYSTEM_CURSOR_NOT_ALLOWED,  /**< Not permitted. Usually a slashed circle or crossbones. */
    SDL_SYSTEM_CURSOR_POINTER,      /**< Pointer that indicates a link. Usually a pointing hand. */
    SDL_SYSTEM_CURSOR_NW_RESIZE,    /**< Window resize top-left. This may be a single arrow or a double arrow like NWSE_RESIZE. */
    SDL_SYSTEM_CURSOR_N_RESIZE,     /**< Window resize top. May be NS_RESIZE. */
    SDL_SYSTEM_CURSOR_NE_RESIZE,    /**< Window resize top-right. May be NESW_RESIZE. */
    SDL_SYSTEM_CURSOR_E_RESIZE,     /**< Window resize right. May be EW_RESIZE. */
    SDL_SYSTEM_CURSOR_SE_RESIZE,    /**< Window resize bottom-right. May be NWSE_RESIZE. */
    SDL_SYSTEM_CURSOR_S_RESIZE,     /**< Window resize bottom. May be NS_RESIZE. */
    SDL_SYSTEM_CURSOR_SW_RESIZE,    /**< Window resize bottom-left. May be NESW_RESIZE. */
    SDL_SYSTEM_CURSOR_W_RESIZE,     /**< Window resize left. May be EW_RESIZE. */
    SDL_SYSTEM_CURSOR_CONTEXT_MENU, /**< A context menu is available for the object under the cursor. */
    SDL_SYSTEM_CURSOR_HELP,         /**< Help is available for the object under the cursor. */
    SDL_SYSTEM_CURSOR_CELL,         /**< A set of cells may be selected. */
    SDL_SYSTEM_CURSOR_VERTICAL_TEXT,/**< Text selection. May be TEXT */
    SDL_SYSTEM_CURSOR_ALIAS,        /**< A shortcut is to be created. */
    SDL_SYSTEM_CURSOR_COPY,         /**< Something is to be copied. */
    SDL_SYSTEM_CURSOR_NO_DROP,      /**< The dragged item cannot be dropped at this location. May be NOT_ALLOWED. */
    SDL_SYSTEM_CURSOR_GRAB,         /**< The object under the cursor can be grabbed */
    SDL_SYSTEM_CURSOR_GRABBING,     /**< An object is currently being grabbed. */
    SDL_SYSTEM_CURSOR_COL_RESIZE,   /**< Column resize. May be EW_RESIZE. */
    SDL_SYSTEM_CURSOR_ROW_RESIZE,   /**< Row resize. May be NS_RESIZE. */
    SDL_SYSTEM_CURSOR_ALL_SCROLL,   /**< Four pointed arrow pointing north, south, east, and west. */
    SDL_SYSTEM_CURSOR_ZOOM_IN,      /**< Zoom in. */
    SDL_SYSTEM_CURSOR_ZOOM_OUT,     /**< Zoom out. */
    SDL_SYSTEM_CURSOR_COUNT
} SDL_SystemCursor;
```

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryMouse](CategoryMouse)

