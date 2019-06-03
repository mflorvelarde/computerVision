#ifdef _MSC_VER
typedef __int64 int64_t;       /* Define it from MSVC's internal type */
#else
#include <stdint.h>            /* Use the C99 official header */
#endif

#include <math.h>

#include "coreslam.h"
#include "coreslam_internals.h"

#include <pmmintrin.h>
#include <xmmintrin.h>
#include <mmintrin.h>

/* This structure supports extracting two 32-bit integer coordinates from a 64-bit register */
typedef union 
{
    struct 
    { 
        int y; 
        int x; 
            
    } pos;

    __m64 mmx;

} cs_pos_mmx_t;


int 
distance_scan_to_map(
    map_t *  map,
    scan_t * scan,
    position_t position)
{    
    int npoints = 0; /* number of points where scan matches map */
    int64_t sum = 0; /* sum of map values at those points */
    
    /* Pre-compute sine and cosine of angle for rotation */
    double position_theta_radians = radians(position.theta_degrees);
    double costheta = cos(position_theta_radians) * map->scale_pixels_per_mm;
    double sintheta = sin(position_theta_radians) * map->scale_pixels_per_mm;
    
    /* Pre-compute pixel offset for translation */
    double pos_x_pix = position.x_mm * map->scale_pixels_per_mm;
    double pos_y_pix = position.y_mm * map->scale_pixels_per_mm;
    
    __m128 sincos128 = _mm_set_ps (costheta, -sintheta, sintheta, costheta);
    __m128 posxy128  = _mm_set_ps (pos_x_pix, pos_y_pix, pos_x_pix, pos_y_pix);

    int i = 0;
    for (i=0; i<scan->npoints; i++) 
    {        
        /* Consider only scan points representing obstacles */
        if (scan->value[i] == OBSTACLE)
        {
            /* Compute coordinate pair using SSE */
            __m128 xy128 = _mm_set_ps (scan->x_mm[i], scan->y_mm[i], scan->x_mm[i], scan->y_mm[i]);
            xy128 = _mm_mul_ps(sincos128, xy128);
            xy128 = _mm_hadd_ps(xy128, xy128);
            xy128 = _mm_add_ps(xy128, posxy128);
            cs_pos_mmx_t pos;
            pos.mmx = _mm_cvtps_pi32(xy128);

            /* Extract coordinates */
            int x = pos.pos.x;
            int y = pos.pos.y;

            /* Empty the multimedia state to avoid floating-point errors later */
            _mm_empty();
         
            /* Add point if in map bounds */
            if (x >= 0 && x < map->size_pixels && y >= 0 && y < map->size_pixels) 
            {
                sum += map->pixels[y * map->size_pixels + x];
                npoints++;
            } 
        }
    } 

    /* Return sum scaled by number of points, or -1 if none */
    return npoints ? (int)(sum * 1024 / npoints) : -1;  
}
