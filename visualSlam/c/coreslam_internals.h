#ifdef _MSC_VER
typedef __int64 int64_t;       /* Define it from MSVC's internal type */
#define _USE_MATH_DEFINES
#include <math.h>
#else
#include <stdint.h>            /* Use the C99 official header */
#endif


static const int NO_OBSTACLE            = 65500;
static const int OBSTACLE               = 0;

static double 
radians(double degrees)
{
    return degrees * M_PI / 180;
}
