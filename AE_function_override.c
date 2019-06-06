const char *getObjectName (object *anObject) {
  static char * (*func)();

  if(!func)
    func = (char *(*)()) dlsym(RTLD_NEXT, "getObjectName");
  printf("Overridden!\n");     
  return(func(anObject));    // call original function
}