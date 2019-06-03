#include "ziggurat.h"
#include "random.h"

#include <stdlib.h>
#include <string.h>

typedef struct random_t 
{
    float    fn[128];
    uint32_t kn[128];
    float    wn[128];  
    uint32_t seed;
        
} random_t;

size_t random_size(void)
{
    return sizeof(random_t);
}


void * random_new(int seed)
{
    random_t * r = (random_t *)malloc(sizeof(random_t));
    
    random_init(r, seed);
    
    return r;
    
}


void random_init(void * v, int seed)
{
    random_t * r = (random_t *)v;
    
    r->seed = seed;
        
    r4_nor_setup (r->kn, r->fn, r->wn );    
}


double random_normal(void * v, double mu, double sigma)
{
    random_t * r = (random_t *)v;
    
    return mu + sigma * r4_nor ( &r->seed, r->kn, r->fn, r->wn );
}

void random_free(void * v)
{
    free(v);
}

void * random_copy(void * v)
{
    random_t * r = (random_t *)malloc(sizeof(random_t));
    
    memcpy(r, v, sizeof(random_t));

    return r;    
}

