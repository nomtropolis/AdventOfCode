#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream file_in;
  file_in.open("../input.txt", ios::in);
  char current_character;
  int floor = 0;
  int char_num = 0;
  while (!file_in.eof()) {
    char_num ++;
    file_in.get(current_character);
    if (current_character == '(') {
      floor ++;
    } else if (current_character == ')') {
      floor --;
    }
    if (floor < 0) {
      std::cout << "Entered basement at postiion: " << char_num << std::endl;
      return 0;
    }
  }
  
  return 0;
}
