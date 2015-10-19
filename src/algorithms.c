//#include <stdio.h>

int n_squared(int iterations) {

    int result = 0;
    int i = 0;
    int j = 0;

    while(i < iterations) {
        j = 0;
        while(j < iterations) {
            result = result + i + j;
            j = j + 1;
        }
        i = i + 1;
    }
    return result;
}


int linear(int iterations) {

    int result = 0;
    int i = 0;

    while(i < iterations) {
        result = result + i;
        i = i + 1;
    }
    return result;
}


int log_n(int iterations) {

    int result = 0;
    int i = 0;

    while(i < iterations) {
        result = result + i;
        iterations = iterations / 2;
        i = i + 1;
    }
    return result;
}
