function pthread_hook() {
    //int pthread create(pthread t *newthread, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)
    var pthread_create_origin = Module.findExportByName("libc.so", "pthread_create");
    var pthread_create_replace = new NativeFunction(pthread_create_origin, "int", ["pointer", "pointer", "pointer", "pointer"]);
    Interceptor.replace(pthread_create_origin, new NativeCallback(function (ptr0, ptr1, ptr2, ptr3) {
        retval = pthread_create_replace(ptr0, ptr1, ptr2, ptr3);
        return retval;
    }, "int", ["pointer", "pointer", "pointer", "pointer"]));
}
