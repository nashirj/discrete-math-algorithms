cmake_minimum_required(VERSION 3.16)
project(sets C)

set(CMAKE_C_STANDARD 11)

find_package(PythonInterp 3.7 REQUIRED)
find_package(PythonLibs 3.7 REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})

add_library(sets ${PYTHON_LIBRARIES} csetsmodule.c)