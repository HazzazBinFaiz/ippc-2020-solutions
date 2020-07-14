#include <stdio.h>
#include <math.h>

const double PI = atan(1.0)*4;

int main(){
    double f, s;
    s = sin((108*PI)/180) / sin((63*PI)/180);
    while(scanf("%lf",&f) != EOF){
        printf("%.10lf\n",s*f);
    }
    return 0;
}