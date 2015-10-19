#include <stdio.h>
#include "algorithms.h"

int main(int argc, char* argv[]) {

  int iterations = 100;
  int n2_result = 0;
  int n_result = 0;
  int log_result = 0;

  n2_result = n_squared(iterations);
  n_result = linear(iterations);
  log_result = log_n(iterations);

  printf("Results.\nn^2: %d\nn: %d\nlog n: %d\n", n2_result, n_result, log_result);

  return 0;
}
