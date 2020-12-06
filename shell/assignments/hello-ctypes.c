#include <stdio.h>
#include <time.h>

void say_hello(char* name) {
	printf("Hello %s!\n", name);
}

long factorial(long n) {
	if (n == 0)
		return 1;

	return (n * factorial(n - 1));
}

void what_time() {
	time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    char s[64];
    strftime(s, sizeof(s), "%c", tm);
    printf("%s\n", s);
}

