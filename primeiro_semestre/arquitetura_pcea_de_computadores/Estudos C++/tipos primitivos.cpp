#include <iostream>

int main() {
  int myInt = -10; //números inteiros
  unsigned int myUint = 0; //números inteiros positivos
  
  float myFloat = 0.0f; //números decimais
  double myDouble = 0.0; //números decimais mais precisos
  
  bool myBool = true; //true or false
  myBool = false;
  
  char myChar = 'a'; //caracteres
  char myArray[11] = "0123456789"; //array de caracteres
  
  size_t mySizeT = 0; //tamanho de algo

  std::cout << myInt << "\n" << myUint << "\n" << myFloat << "\n" << myDouble << "\n" << myBool << "\n" << myChar << "\n" << myArray << "\n" << mySizeT << "\n";
  
  return 0;
}
