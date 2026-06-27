# Python Concurrency Notes

---

# Concurrency

- One worker
- Many tasks
- Switch between tasks
- One task executes at a time

Example:

- One waiter serving many tables.

> Concurrency = Managing multiple tasks.

# Threading

- One process
- Multiple threads
- Shared memory
- Fast context switching
- Affected by GIL
- Good for I/O tasks

Examples:

- File downloads
- API requests
- Database calls

Problems:

- Race conditions
- Shared memory issues

Solutions:

- Lock
- RLock
- Semaphore

# Multiprocessing

- Multiple processes
- Multiple CPU cores
- Separate memory
- Bypasses GIL
- True parallelism
- CPU intensive tasks

Examples:

- Image processing
- AI training
- Video rendering
- Data analysis

# GIL (Global Interpreter Lock)

- Only one thread executes Python bytecode at a time.
- Exists in CPython.
- Protects shared memory.
- Prevents memory corruption.

Effects:

- Threads cannot achieve true parallelism.
- Multiprocessing bypasses GIL.

> GIL = One thread runs Python code at a time.
