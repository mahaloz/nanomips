# Learning NanoMIPS
This directory contains all the files and binaries used in reverse engineering
the 0CTF 2020 Quals challenge `babymips`.

## Background
While learning the skills to do this challenge I used the following reference
quite a lot: https://www.mips.com/products/architectures/nanomips/

## Running
Before anything, run the `setup.sh` script, which will require root access to
fix system libraries to have NanoMIPS. 

In this directory is the `babymips` program. To see the non-annotated assembly
simply run the `dissass_mips.sh` file, which should start a NanoMIPS version of
`objdump`. 

Running this binary is more tricky. To run the binary, first execute
`start_proc.sh`, which will start a `qemu` instance and run the binary waiting
for a `gdb` connection. Then run the `start_gdb.sh` script, and hit c. This will
allow the program to continue execution. Feel free to debug it :).

## Included Files
`babymips`: NanoMIPS program that was reverse engineered
`babymips.diss`: Manually annotated disassembly of babymips
`dissass_mips.sh`: Script to disassemble a babymips
`setup.sh`: Setup Script, which installs libraries
`solve.py`: MIPS translated to Python.
`start_gdb.sh`: Starts babymips in a gdb instance
`start_proc.sh`: Starts babymips, waits for gdb to connect
