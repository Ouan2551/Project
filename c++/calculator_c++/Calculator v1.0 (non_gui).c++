//this program can use only +,-,*,/,%,^2,root,
//simple step just get value, operator and output value
#include <bits/stdc++.h>
using namespace std;

string input_operator(void)
{
    string op = ""; cout << "operator : "; cin >> op; return op;
}

string check_operator(string op)
{
    string a[7] = {"+","-","*","/","%","^","root"}; int check = 0;
    for (int i = 0; i < 7; i++)
    {
        if (op != a[i])
        {
            check++;
        }
    }

    if (check == 7)
    {
        cout << "Please type correct operator" << endl;
        op = input_operator();
        op = check_operator(op);
    }
    return op;
}

//process
double plus_numbers(double n1, double n2)
{
    double result = n1 + n2;
    return result;
}
double subtract_numbers(double n1, double n2)
{
    double result = n1 - n2;
    return result;
}
double multiply_numbers(double n1, double n2)
{
    double result = n1 * n2;
    return result;
}
double divide_numbers(double n1, double n2)
{
    double result = n1 / n2;
    return result;
}
double modulus_numbers(double n1, double n2)
{
    double result = fmod(n1,n2);
    return result;
}
double power_numbers(double n1, double n2)
{
    double result = pow(n1, n2);
    return result;
}
double square_root_numbers(double n1, double n2)
{
    double result = pow(n1, 1/n2);
    return result;
}

int main ()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //user guide
    cout << "this program can only do this operator" << endl;
    cout << "this program can only support double datatype" << endl;
    cout << "all command => +   -   *   /   %   ^(power)   root(square_root)" << endl;
    cout << "in () is just description doesn't type this" << endl;
    cout << endl;
    cout << "If you want to power_number. number 2 is exponent" << endl;
    cout << "If you want to find square_root. number 2 is degree of the root" << endl;
    cout << endl;

    //get number
    double n1, n2, result; n1 = n2 = result = 0;
    cout << "number1 : "; cin >> n1; cout << "number2 : "; cin >> n2;
    
    //operator
    // string txt = ""; cin >> txt;
    string txt = input_operator();
    
    //checking correct input
    string op = check_operator(txt);


    //have idea use for loop to select and use operator
    if (op == "+")
    {
        result = plus_numbers(n1, n2);
    }
    if (op == "-")
    {
        result = subtract_numbers(n1, n2);
    }
    if (op == "*")
    {
        result = multiply_numbers(n1, n2);
    }
    if (op == "/")
    {
        result = divide_numbers(n1, n2);
    }
    if (op == "%")
    {
        result = modulus_numbers(n1, n2);
    }
    if (op == "^")
    {
        result = power_numbers(n1, n2);
    }
    if (op == "root")
    {
        result = square_root_numbers(n1, n2);
    }

    cout << fixed << setprecision(2) << "result : " << result;

    return 0;
}


//now stuck at problem operator divide and find square root.
//now upper problem can fix now and fix buy in process session i use double instead int
//and normal modulus (%) is not work in double use fmod for number with decimal like double it better

//sorry bad grammar bro.