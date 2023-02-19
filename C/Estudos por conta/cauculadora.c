#include <stdio.h>
#include <math.h>

double cauculator(double a, char b, double c);

int main(void){
    double num1, num2;
    char op;

    printf("Primeiro numero: ");
    scanf("%lf", &num1);
    printf("Operador: ");
    scanf(" %c", &op);
    printf("Segundo numero: ");
    scanf("%lf", &num2);
    printf("%lf %c %lf = %lf", num1, op, num2, cauculator(num1, op, num2));

}

double cauculator(double a, char b, double c){
    double res;
    if (b == '+'){
        res = a + c;
    }
    else if (b == '-'){
        res = a - c;
    }
    else if (b == '/'){
        res = a / c;
    }
    else if (b == '*'){
        res = a * c;
    }
    return (int) (res);
}