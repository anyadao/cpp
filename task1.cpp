// 1. �������� �������, ������� ����� ��������� �������� ���������� ����� (� � ��� ������� ��������).
#include <iostream>
using namespace std;

void BitOddEven(int number)
{
	int check;
	check = number & 1;
	if (check == 0)
	{
		cout << "\n���� ����� ������. " << endl;
	}
	if (check == 1)
	{
		cout << "���� ����� ��������. " << endl;
	}
}

void OrdOddEven(int number)
{
	if (number % 2 != 0)
	{
		cout << "\n���� ����� ��������. " << endl;
	}
	if (number % 2 == 0)
	{
		cout << "\n���� ����� ������. " << endl;
	}
}

void main()
{
	setlocale(LC_ALL, "Russian");
	int number, check;
	cout << "������� ����� ��� �������� ��� �� ��������: ";
	cin >> number;
	BitOddEven(number);
	OrdOddEven(number);
};