#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

std::vector<int> get_sides(string line) {
  std::replace(line.begin(), line.end(), 'x', ' '); // convert to whitespace separator for stringstream
  vector<int> sides;
  stringstream ss(line);
  int temp;
  while (ss >> temp) {
    sides.push_back(temp);
  }
  return sides;
}

int main() {
  ifstream file_in("../input.txt");
  std::vector<vector<int>> sides;
  string current_line;
  int total_ribbon = 0;
  while (std::getline(file_in, current_line)) {
    if (current_line.size() > 0) {
      std::vector<int> sides = get_sides(current_line);
      int bow = sides[0] * sides[1] * sides[2];

      std::sort(sides.begin(), sides.end());
      std::vector<int> two_sides = std::vector<int>(&sides[0], &sides[sides.size()-1]);

      int package_ribbon = (two_sides[0] + two_sides[1]) * 2;
      
      total_ribbon += bow;
      total_ribbon += package_ribbon;
    }
  }
  printf("The answer is: %d\n", total_ribbon);
  return 0;
}
