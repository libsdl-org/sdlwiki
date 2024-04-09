# Building SDL3 for Android

## Draft

This page was roughly updated from the SDL2 version, but needs to be inspected
for details that are out of date, and a few SDL2isms need to be cleaned out
still, too. Read this page with some skepticism for now.


## Existing documentation

A lot of information can be found in [README/android](README/android).

This page is more walkthrough-oriented.


## Pre-requisites

* Install minimal Java environment. For instance, in Debian/Ubuntu:

```bash
sudo apt install openjdk-8-jdk ant android-sdk-platform-tools-common
```

* Install NDK (tested with [https://dl.google.com/android/repository/android-ndk-r10e-linux-x86_64.zip r10e])
* Install the latest SDK, run `tools/bin/sdkmanager` (or `tools/android` pre-2017) and install one API (>= 31)
* Configure your environment variables, e.g.:

```bash
PATH="/usr/src/android-ndk-rXXx:$PATH"                  # for 'ndk-build'
PATH="/usr/src/android-sdk-linux/tools:$PATH"           # for 'android'
PATH="/usr/src/android-sdk-linux/platform-tools:$PATH"  # for 'adb'
export ANDROID_HOME="/usr/src/android-sdk-linux"        # for gradle
export ANDROID_NDK_HOME="/usr/src/android-ndk-rXXx"     # for gradle
```

## Simple builds

### SDL wrapper for simple programs

* Compile a sample app (calls ndk-build): 

```bash
cd /usr/src/SDL3/build-scripts/
./androidbuild.sh org.libsdl.testgles ../test/testgles.c
```

* Follow the instructions to install on your device: 

```bash
cd /usr/src/SDL3/build/org.libsdl.testgles/
./gradlew installDebug
```bash

Notes:

* multiple targets armeabi-v7a/arm64-v8a/x86/x86_64 compilation
* application doesn't quit

#### Troubleshooting

* use OpenJDK 8: execute `sudo update-alternatives --config java` and select jdk-8 as default; or use `JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 ./gradlew`
* `javax/xml/bind/annotation/XmlSchema, Could not initialize class com.android.sdklib.repository.AndroidSdkHandler`: check the Android Gradle Plugin version in `/android-project/build.gradle`, e.g.
` classpath 'com.android.tools.build:gradle:3.1.0' `
* You can customize the Gradle version in `/android-project/gradle/wrapper/gradle-wrapper.properties`:
` distributionUrl=https\://services.gradle.org/distributions/gradle-4.9-all.zip `
* You can customize your SDK/NDK versions in `android-project/app/build.gradle`:

```c
android {
    buildToolsVersion "28.0.1"
    compileSdkVersion 28
```

* You can customize your targets depending on the NDK version:

```c
externalNativeBuild {
    ndkBuild {
        arguments "APP_PLATFORM=android-14"
        abiFilters 'armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'
```

* `ABIs [x86_64, arm64-v8a] are not supported for platform. Supported ABIs are [armeabi, armeabi-v7a, x86, mips]`: upgrade to NDK >= 10
* TODO: check how we can use the distro's gradle instead of executing stuff from the Internet - `apt install gradle libgradle-android-plugin-java`

### SDL wrapper + SDL_image NDK module

Let's modify `SDL3_image/showimage.c` to show a simple embedded image (e.g. XPM).

```c
#include <SDL3/SDL.h>
#include <SDL3/SDL_image.h>

/* XPM */
static char * icon_xpm[] = {
  "32 23 3 1",
  " 	c #FFFFFF",
  ".	c #000000",
  "+	c #FFFF00",
  "                                ",
  "            ........            ",
  "          ..++++++++..          ",
  "         .++++++++++++.         ",
  "        .++++++++++++++.        ",
  "       .++++++++++++++++.       ",
  "      .++++++++++++++++++.      ",
  "      .+++....++++....+++.      ",
  "     .++++.. .++++.. .++++.     ",
  "     .++++....++++....++++.     ",
  "     .++++++++++++++++++++.     ",
  "     .++++++++++++++++++++.     ",
  "     .+++++++++..+++++++++.     ",
  "     .+++++++++..+++++++++.     ",
  "     .++++++++++++++++++++.     ",
  "      .++++++++++++++++++.      ",
  "      .++...++++++++...++.      ",
  "       .++............++.       ",
  "        .++..........++.        ",
  "         .+++......+++.         ",
  "          ..++++++++..          ",
  "            ........            ",
  "                                "};

int main(int argc, char *argv[])
{
  SDL_Window *window;
  SDL_Renderer *renderer;
  SDL_Surface *surface;
  SDL_Texture *texture;
  int done;
  SDL_Event event;

  if (SDL_CreateWindowAndRenderer(0, 0, 0, &window, &renderer) < 0) {
    SDL_LogError(SDL_LOG_CATEGORY_APPLICATION,
        "SDL_CreateWindowAndRenderer() failed: %s", SDL_GetError());
    return(2);
  }

  surface = IMG_ReadXPMFromArray(icon_xpm);
  texture = SDL_CreateTextureFromSurface(renderer, surface);
  if (!texture) {
    SDL_LogError(SDL_LOG_CATEGORY_APPLICATION,
        "Couldn't load texture: %s", SDL_GetError());
    return(2);
  }
  SDL_SetWindowSize(window, 800, 480);

  done = 0;
  while (!done) {
    while (SDL_PollEvent(&event)) {
      if (event.type == SDL_EVENT_QUIT)
        done = 1;
    }
    SDL_RenderTexture(renderer, texture, NULL, NULL);
    SDL_RenderPresent(renderer);
    SDL_Delay(100);
  }
  SDL_DestroyTexture(texture);

  SDL_Quit();
  return(0);
}
```

Then let's make an Android app out of it. To compile: 

```bash
cd /usr/src/SDL3/build-scripts/
./androidbuild.sh org.libsdl.showimage /usr/src/SDL3_image/showimage.c
cd /usr/src/SDL3/build/org.libsdl.showimage/
ln -s /usr/src/SDL3_image jni/
ln -s /usr/src/SDL3_image/external/libwebp-0.3.0 jni/webp
sed -i -e 's/^LOCAL_SHARED_LIBRARIES.*/& SDL3_image/' jni/src/Android.mk
ndk-build -j$(nproc)
ant debug install
```

Notes:
* application doesn't restart properly


## Build an autotools-friendly environment

You use autotools in your project and can't be bothering understanding ndk-build's cryptic errors? This guide is for you!

Note: this environment can be used for CMake too.

### Compile a shared binaries bundle for SDL and SDL_*

* Get the latests SDL3_* releases:

(FIXME: this needs to be updated for SDL3.)

```bash
cd /usr/src/
wget https://libsdl.org/release/SDL2-2.0.5.tar.gz
wget https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.1.tar.gz
wget https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.1.tar.gz
wget https://www.libsdl.org/projects/SDL_net/release/SDL2_net-2.0.1.tar.gz
wget https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.14.tar.gz

tar xf SDL2-2.0.5.tar.gz
tar xf SDL2_image-2.0.1.tar.gz
tar xf SDL2_mixer-2.0.1.tar.gz
tar xf SDL2_net-2.0.1.tar.gz
tar xf SDL2_ttf-2.0.14.tar.gz

ln -s SDL2-2.0.5 SDL2
ln -s SDL2_image-2.0.1 SDL2_image
ln -s SDL2_mixer-2.0.1 SDL2_mixer
ln -s SDL2_net-2.0.1 SDL2_net
ln -s SDL2_ttf-2.0.14 SDL2_ttf
```

* Start with a minimal build:

```bash
cd /usr/src/SDL3/
#git checkout -- .  # remove traces of previous builds
cd build-scripts/
# edit androidbuild.sh and modify $ANDROID update project --target android-XX
./androidbuild.sh org.libsdl /dev/null
# doesn't matter if the actual build fails, it's just for setup
cd ../build/org.libsdl/
```

* Remove reference to our dummy file:

```bash
rm -rf jni/src/
```

* Reference SDL_image, SDL_mixer, SDL_ttf, and their dependencies, as NDK modules:

```bash
ln -s /usr/src/SDL3_image jni/
ln -s /usr/src/SDL3_image/external/libwebp-0.3.0 jni/webp
ln -s /usr/src/SDL3_mixer jni/
ln -s /usr/src/SDL3_mixer/external/libmikmod-3.1.12 jni/libmikmod
ln -s /usr/src/SDL3_mixer/external/smpeg2-2.0.0 jni/smpeg2
ln -s /usr/src/SDL3_net jni/
ln -s /usr/src/SDL3_ttf jni/
```

* Optionnaly edit `jni/Android.mk` to disable some formats, e.g.:

```make
SUPPORT_MP3_SMPEG := false
include $(call all-subdir-makefiles)
```

* Launch the build!

```bash
ndk-build -j$(nproc)
```

Note: no need to add `System.loadLibrary` calls in `SDLActivity.java`, your application will be linked to them and Android's ld-linux loads them automatically.


### Install SDL in a GCC toolchain

Now:

* Copy the NDK into a traditional GCC toolchain (leave android-14 as-is):

```bash
/usr/src/android-ndk-r8c/build/tools/make-standalone-toolchain.sh \
  --platform=android-14 --install-dir=/usr/src/ndk-standalone-14-arm --arch=arm
```

* Set your PATH (important, do it before any build):

```bash
NDK_STANDALONE=/usr/src/ndk-standalone-14-arm
PATH=$NDK_STANDALONE/bin:$PATH
```

* Install the SDL3 binaries in the toolchain:

```bash
cd /usr/src/SDL3/build/org.libsdl/
for i in libs/armeabi/*; do ln -nfs $(pwd)/$i $NDK_STANDALONE/sysroot/usr/lib/; done
mkdir $NDK_STANDALONE/sysroot/usr/include/SDL3/
cp jni/SDL/include/* $NDK_STANDALONE/sysroot/usr/include/SDL3/
cp jni/*/SDL*.h $NDK_STANDALONE/sysroot/usr/include/SDL3/
```

* Install `pkg-config` and install a host-triplet-prefixed symlink in the PATH (auto-detected by autoconf):

```bash
VERSION=0.9.12
cd /usr/src/
wget http://rabbit.dereferenced.org/~nenolod/distfiles/pkgconf-$VERSION.tar.gz
tar xf pkgconf-$VERSION.tar.gz
cd pkgconf-$VERSION/
mkdir native-android/ && cd native-android/
../configure --prefix=$NDK_STANDALONE/sysroot/usr
make -j$(nproc)
make install
ln -s ../sysroot/usr/bin/pkgconf $NDK_STANDALONE/bin/arm-linux-androideabi-pkg-config
mkdir $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/
```

* Install pkg-config `.pc` files for SDL:

```bash
cat <<'EOF' > $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/sdl2.pc
prefix=/usr/src/ndk-standalone-14-arm/sysroot/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: sdl2
Description: Simple DirectMedia Layer is a cross-platform multimedia library designed to provide low level access to audio, keyboard, mouse, joystick, 3D hardware via OpenGL, and 2D video framebuffer.
Version: 2.0.5
Requires:
Conflicts:
Libs: -lSDL3
Cflags: -I${includedir}/SDL3   -D_REENTRANT
EOF

cat <<'EOF' > $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/SDL3_image.pc
prefix=/usr/src/ndk-standalone-14-arm/sysroot/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: SDL3_image
Description: image loading library for Simple DirectMedia Layer
Version: 2.0.1
Requires: sdl2 >= 2.0.0
Libs: -L${libdir} -lSDL3_image
Cflags: -I${includedir}/SDL3
EOF

cat <<'EOF' > $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/SDL3_mixer.pc
prefix=/usr/src/ndk-standalone-14-arm/sysroot/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: SDL3_mixer
Description: mixer library for Simple DirectMedia Layer
Version: 2.0.1
Requires: sdl2 >= 2.0.0
Libs: -L${libdir} -lSDL3_mixer
Cflags: -I${includedir}/SDL3
EOF

cat <<'EOF' > $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/SDL3_net.pc
prefix=/usr/src/ndk-standalone-14-arm/sysroot/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: SDL3_net
Description: net library for Simple DirectMedia Layer
Version: 2.0.1
Requires: sdl2 >= 2.0.0
Libs: -L${libdir} -lSDL3_net
Cflags: -I${includedir}/SDL3
EOF

cat <<'EOF' > $NDK_STANDALONE/sysroot/usr/lib/pkgconfig/SDL3_ttf.pc
prefix=/usr/src/ndk-standalone-14-arm/sysroot/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: SDL3_ttf
Description: ttf library for Simple DirectMedia Layer with FreeType 2 support
Version: 2.0.14
Requires: sdl2 >= 2.0.0
Libs: -L${libdir} -lSDL3_ttf
Cflags: -I${includedir}/SDL3
EOF
```

### Building other dependencies

You can add any other libraries (e.g.: SDL2_gfx, freetype, gettext, gmp...) using commands like:

```bash
mkdir cross-android/ && cd cross-android/
../configure --host=arm-linux-androideabi --prefix=$NDK_STANDALONE/sysroot/usr \
  --with-some-option --enable-another-option \
  --disable-shared
make -j$(nproc)
make install
```

Static builds (`--disable-shared`) are recommended for simplicity (no additional `.so` to declare).

(FIXME: is there an SDL3_gfx?)

```bash
Example with SDL2_gfx:
VERSION=1.0.3
wget http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-$VERSION.tar.gz
tar xf SDL2_gfx-$VERSION.tar.gz
mv SDL2_gfx-$VERSION/ SDL2_gfx/
cd SDL2_gfx/
mkdir cross-android/ && cd cross-android/
../configure --host=arm-linux-androideabi --prefix=$NDK_STANDALONE/sysroot/usr \
  --disable-shared --disable-mmx
make -j$(nproc)
make install
```

You can compile YOUR application using this technique, with some more steps to tell Android how to run it using JNI.


### Build your autotools app

First, prepare an Android project:

* Copy and adapt the `/usr/src/SDL3/android-project` skeleton as explained in `README-android.md`. You can leave it as-is in a first step.
* Make links to the SDL binaries as well:

```bash
mkdir -p libs/armeabi/
for i in /usr/src/SDL3/build/org.libsdl/libs/armeabi/*; do ln -nfs $i libs/armeabi/; done
```

Make your project Android-aware:

* Add `/usr/src/SDL3/src/main/android/SDL_android_main.c` in your project (comment out the line referencing "SDL_internal.h"). Compile it as C (not C++).
* In your `configure.ac`, detect Android:

```c
AM_CONDITIONAL(ANDROID, test "$host" = "arm-unknown-linux-androideabi")
```

* In your `Makefile.am`, tell Automake you'll build executables as libraries, using something like:

```c
if ANDROID
<!--  Build .so JNI libs rather than executables -->
  AM_CFLAGS = -fPIC
  AM_LDFLAGS += -shared
  COMMON_OBJS += SDL_android_main.c
endif
```

* Cross-compile your project using the GCC toolchain environment we created:

```bash
PATH=$NDK_STANDALONE/bin:$PATH
mkdir cross-android/ && cd cross-android/
../configure --host=arm-linux-androideabi \
  --prefix=/android-aint-posix \
  --with-your-option --enable-your-other-option ...
make
```

* Do this again for any additional arch you want to support (TODO: see how to support `armeabi-v7a` and document what devices support it); something like:

```bash
mkdir cross-android-v7a/ && cd cross-android-v7a/
# .o: -march=armv5te -mtune=xscale -msoft-float -mthumb  =>  -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=softfp -mthumb
# .so: -march=armv7-a -Wl,--fix-cortex-a8
CFLAGS="-g -O2 -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=softfp -mthumb" LFDLAGS="-march=armv7-a -Wl,--fix-cortex-a8" \
  ../configure --host=arm-linux-androideabi \
  ...
```

Now you can install your pre-built binaries and build the Android project:

* Copy your program in `android-project/libs/armeabi/libmain.so`.
* Build your Android `.apk`:

```bash
android update project --name your_app --path . --target android-XX
ant debug
ant installd
```

* You can run the application remotely:

```bash
adb shell am start -a android.intenon.MAIN -n org.libsdl.app/org.libsdl.app.SDLActivity  # replace with your app package
```

* Your SDL3 Android app is running!

### Build your CMake app

(Work In Progress)

You can use our Android GCC toolchain using a simple toolchain file:

```cmake
# CMake toolchain file
SET(CMAKE_SYSTEM_NAME Linux)  # Tell CMake we're cross-compiling
include(CMakeForceCompiler)
# Prefix detection only works with compiler id "GNU"
CMAKE_FORCE_C_COMPILER(arm-linux-androideabi-gcc GNU)
SET(ANDROID TRUE)
```

You then call CMake like this:
```bash
PATH=$NDK_STANDALONE/bin:$PATH
cmake \
  -D CMAKE_TOOLCHAIN_FILE=../android_toolchain.cmake \
  ...
```

## Troubleshootings

If `ant installd` categorically refuses to install with `Failure [INSTALL_FAILED_INSUFFICIENT_STORAGE]`, even if you have free local storage, that may mean anything. Check logcat first:

```bash
adb logcat
```

If the error logs are not helpful (likely ;')) try locating all past traces of the application:

```bash
find / -name "org...."
```

and remove them all.

If the problem persists, you may try installing on the SD card:

```bash
adb install -s bin/app-debug.apk
```

-----

If you get in your logcat:

`SDL: Couldn't locate Java callbacks, check that they're named and typed correctly`

this probably means your `SDLActivity.java` is out-of-sync with your libSDL3.so.

