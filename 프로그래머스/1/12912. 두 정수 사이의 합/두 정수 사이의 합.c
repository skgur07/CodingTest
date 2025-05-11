#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    
    int tmp;
    if (b < a) {
        tmp = a;
        a = b;
        b = tmp;
    }
    
    long long answer = 0;
    for (int i = a; i <= b; i++){
        answer += i;   
    }
    
    return answer;
}