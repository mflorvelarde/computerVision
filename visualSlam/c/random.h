#include "stdlib.h"

#ifdef __cplusplus 
extern "C" {
#endif
    
/* Returns size of random-number generator in bytes */
size_t random_size(void);

/* Creates and initializes a new random-number generator */
void * random_new(int seed);

/* Initializes a random-number generator */
void random_init(void * r, int seed);

/* Make a copy of the specified random-number generator */
void * random_copy(void * r);

/* Deallocates memory for a random-number generator */
void random_free(void * v);

/* Returns a  standard normal variate with mean mu, variance sigma */
double random_normal(void * v, double mu, double sigma);

#ifdef __cplusplus 
}
#endif
