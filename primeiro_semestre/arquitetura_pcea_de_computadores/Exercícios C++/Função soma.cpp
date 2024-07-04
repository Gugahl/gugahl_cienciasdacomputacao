#include <iostream>

int soma(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;

    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

    int resultado = soma(num1, num2);

    std::cout << "A soma de " << num1 << " e " << num2 << " é: " << resultado << std::endl;

    return 0;
}