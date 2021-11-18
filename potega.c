#include <stdio.h>
#include <math.h>

int main()
{
    int a,b;
    scanf("%d%d",&a,&b);

    // 1. Sposób
    printf("%d\n",(int)pow(a,b));

    // 2. Sposób
    int c=1;
    for(int i=0;i<b;i++){
        c*=a;
    }
    printf("%d\n",c);

    return 0;
}
