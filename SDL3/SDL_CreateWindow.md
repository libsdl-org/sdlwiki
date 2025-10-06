# SDL_CreateWindow

أنشئ نافذة بالأبعاد والعلامات المحددة.

## ملف الرأس

مُعرّف في [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## بناء الجملة

```c
SDL_Window * SDL_CreateWindow(const char *title, int w, int h, SDL_WindowFlags flags);
```

## معلمات الدالة

| | | |
| ---------------------------------- | --------- | ------------------------------------------------------------------- |
| const char * | **title** | عنوان النافذة، بترميز UTF-8. |
| int | **w** | عرض النافذة. |
| int | **h** | ارتفاع النافذة. |
| [SDL_WindowFlags](SDL_WindowFlags) | **flags** | 0، أو واحد أو أكثر من [SDL_WindowFlags](SDL_WindowFlags) معًا باستخدام OR. |

## قيمة الإرجاع

([SDL_Window](SDL_Window) *) تُرجع النافذة التي تم إنشاؤها أو قيمة NULL عند الفشل؛ استدعي [SDL_GetError](SDL_GetError)() لمزيد من المعلومات.

## ملاحظات

حجم النافذة هو طلب، وقد يختلف عن المتوقع بناءً على تخطيط سطح المكتب وسياسات إدارة النوافذ. يجب أن يكون تطبيقك جاهزًا للتعامل مع أي حجم نافذة.

يمكن استخدام `flags` كأيٍّ من القيم التالية معًا (أو):

- [`SDL_WINDOW_FULLSCREEN`](SDL_WINDOW_FULLSCREEN): نافذة بملء الشاشة بدقة سطح المكتب
- [`SDL_WINDOW_OPENGL`](SDL_WINDOW_OPENGL): نافذة قابلة للاستخدام مع سياق OpenGL
- [`SDL_WINDOW_HIDDEN`](SDL_WINDOW_HIDDEN): النافذة غير مرئية
- [`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS): لا توجد زخرفة للنافذة
- [`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE): يمكن تغيير حجم النافذة
- [`SDL_WINDOW_MINIMIZED`](SDL_WINDOW_MINIMIZED): النافذة مصغّرة
- [`SDL_WINDOW_MAXIMIZED`](SDL_WINDOW_MAXIMIZED): النافذة مُكبَّرة
- [`SDL_WINDOW_MOUSE_GRABBED`](SDL_WINDOW_MOUSE_GRABBED): النافذة
تلتقط تركيز الماوس
- [`SDL_WINDOW_INPUT_FOCUS`](SDL_WINDOW_INPUT_FOCUS): النافذة
تتمركز
- [`SDL_WINDOW_MOUSE_FOCUS`](SDL_WINDOW_MOUSE_FOCUS): النافذة
تتركز
- [`SDL_WINDOW_EXTERNAL`](SDL_WINDOW_EXTERNAL): النافذة لم تُنشأ بواسطة SDL
- [`SDL_WINDOW_MODAL`](SDL_WINDOW_MODAL): النافذة نافذة نموذجية
- [`SDL_WINDOW_HIGH_PIXEL_DENSITY`](SDL_WINDOW_HIGH_PIXEL_DENSITY): تستخدم النافذة مخزنًا احتياطيًا عالي الكثافة للبكسل إن أمكن.
- [`SDL_WINDOW_MOUSE_CAPTURE`](SDL_WINDOW_MOUSE_CAPTURE): تم التقاط حركة الماوس في النافذة (غير مرتبط بـ MOUSE_GRABBED)
- [`SDL_WINDOW_ALWAYS_ON_TOP`](SDL_WINDOW_ALWAYS_ON_TOP): يجب أن تكون النافذة دائمًا أعلى من النوافذ الأخرى.
- [`SDL_WINDOW_UTILITY`](SDL_WINDOW_UTILITY): يجب أن تُعامل النافذة كنافذة أداة، ولا تظهر في شريط المهام وقائمة النوافذ.
- [`SDL_WINDOW_TOOLTIP`](SDL_WINDOW_TOOLTIP): يجب أن تُعامل النافذة كنافذة تلميح، ولا يتم التركيز عليها باستخدام الماوس أو لوحة المفاتيح، وتتطلب نافذة رئيسية
- [`SDL_WINDOW_POPUP_MENU`](SDL_WINDOW_POPUP_MENU): يجب التعامل مع النافذة كقائمة منبثقة، وتتطلب نافذة رئيسية.
- [`SDL_WINDOW_KEYBOARD_GRABBED`](SDL_WINDOW_KEYBOARD_GRABBED): تم التقاط مدخلات لوحة المفاتيح في النافذة.
- [`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN): نافذة قابلة للاستخدام مع نسخة Vulkan.
- [`SDL_WINDOW_METAL`](SDL_WINDOW_METAL): نافذة قابلة للاستخدام مع نسخة Metal.
- [`SDL_WINDOW_TRANSPARENT`](SDL_WINDOW_TRANSPARENT): نافذة ذات مخزن مؤقت شفاف.
- [`SDL_WINDOW_NOT_FOCUSABLE`](SDL_WINDOW_NOT_FOCUSABLE): يجب أن تكون النافذة غير قابلة للتركيز

سيتم عرض [SDL_Window](SDL_Window) إذا لم يتم ضبط [SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN). إذا كانت مخفية عند الإنشاء، فيمكن استخدام [SDL_ShowWindow](SDL_ShowWindow)() لعرضها لاحقًا.

في نظام macOS من Apple، **يجب** ضبط الخاصية NSHighResolutionCapable Info.plist على YES، وإلا فلن تحصل على لوحة OpenGL عالية الدقة.

قد يختلف حجم بكسل النافذة عن حجم إحداثياتها إذا كانت النافذة على شاشة عالية الكثافة. استخدم الدالة [SDL_GetWindowSize](SDL_GetWindowSize)() للاستعلام عن حجم منطقة العميل بإحداثيات النافذة، و[SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)() أو [SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)() للاستعلام عن حجم العناصر القابلة للرسم بالبكسل. يُرجى ملاحظة أن حجم العناصر القابلة للرسم قد يتغير بعد إنشاء النافذة، ويجب الاستعلام عنه مرة أخرى في حال ظهور حدث [SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED)

إذا تم إنشاء النافذة باستخدام أيٍّ من علامتي [SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL) أو [SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN)، فسيتم استدعاء دالة LoadLibrary المقابلة ([SDL_GL_LoadLibrary](SDL_GL_LoadLibrary) أو [SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary))، وسيتم استدعاء دالة UnloadLibrary المقابلة بواسطة [SDL_DestroyWindow](SDL_DestroyWindow)().

إذا تم تحديد [SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN) ولم يكن هناك برنامج تشغيل Vulkan عامل، فسوف تفشل [SDL_CreateWindow](SDL_CreateWindow)()،