#include <iostream>

int multiplicacao(int a, int b) {
    return a * b;
}

int main() {
    int num1, num2;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;

    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

      int resultado = multiplicacao(num1, num2);
  
      std::cout << "O resultado da multiplicação de " << num1 << " x " << num2 << " é: " << resultado << std::endl;

    return 0;
}