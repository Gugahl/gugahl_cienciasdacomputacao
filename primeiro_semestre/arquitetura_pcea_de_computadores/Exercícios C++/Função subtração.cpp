#include <iostream>

int subtracao(int a, int b) {
    return a - b;
}

int main() {
    int num1, num2;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;

    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

      int resultado = subtracao(num1, num2);
      std::cout << "O resultado da subtração de " << num1 << " - " << num2 << " é: " << resultado << std::endl;

    return 0;
}