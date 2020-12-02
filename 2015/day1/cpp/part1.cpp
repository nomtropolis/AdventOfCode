#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream file_in;
  file_in.open("../input.txt", ios::in);
  char current_character;
  int floor = 0;
  while (!file_in.eof()) {
    file_in.get(current_character);
    // std::cout << typeid(current_character).name();
    if (current_character == '(') {
      floor ++;
    } else if (current_character == ')') {
      floor --;
    }
  }
  std::cout << "Floor: " << floor << std::endl;
  return 0;
}
