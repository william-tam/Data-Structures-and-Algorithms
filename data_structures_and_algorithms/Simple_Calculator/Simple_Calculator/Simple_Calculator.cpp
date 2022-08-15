// Simple_Calculator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdlib.h>
using namespace std; 

double calculate(double num1, double num2, char op) {
    // checks if the inputs from the user is viable. 
    if (op == '*') {
        printf("%f",num1 * num2);
    }
    else if (op == '/') {
        printf("%f",num1 / num2);
    }
    else if (op == '+') {
        printf("%f",num1 + num2);
    }
    else if (op == '-') {
        printf("%f",num1 - num2);
    } 
    else {
        printf("Invalid operator, please enter a correct operator.");
    }

}
int main()
{
    double sum1, sum2;
    char op; 

    printf("Enter a number: ");
    scanf("%lf", &sum1);
    printf("Enter a second number: ");
    scanf("%lf", &sum2);
    printf("Enter the operator: ");
    scanf("%c", &op);

    calculate(sum1, sum2, op);
    return 0; 
}

