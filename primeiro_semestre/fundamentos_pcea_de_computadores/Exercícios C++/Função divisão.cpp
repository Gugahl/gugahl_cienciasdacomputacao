#include <iostream>

float divisao(float a, float b) {
    return a / b;
}

int main() {
    float num1, num2;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;

    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

      float resultado1 = divisao(num1, num2);

      float resultado2 = divisao(num2, num1);
  
      std::cout << "O resultado da divisão de " << num1 << " / " << num2 << " é: " << resultado1 << std::endl;

      std::cout << "O resultado da divisão de " << num2 << " / " << num1 << " é: " << resultado2 << std::endl;
  
    return 0;
}