// 1. Написать функцию, которая будет проверять четность некоторого числа (с и без битовых операций).
#include <iostream>
using namespace std;

void BitOddEven(int number)
{
	int check;
	check = number & 1;
	if (check == 0)
	{
		cout << "\nВаше число четное. " << endl;
	}
	if (check == 1)
	{
		cout << "Ваше число нечетное. " << endl;
	}
}

void OrdOddEven(int number)
{
	if (number % 2 != 0)
	{
		cout << "\nВаше число нечетное. " << endl;
	}
	if (number % 2 == 0)
	{
		cout << "\nВаше число четное. " << endl;
	}
}

void main()
{
	setlocale(LC_ALL, "Russian");
	int number, check;
	cout << "Введите число для проверки его на четность: ";
	cin >> number;
	BitOddEven(number);
	OrdOddEven(number);
};