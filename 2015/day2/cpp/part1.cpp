#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int get_smallest_side(int x, int y, int z){
  int side_a = x * y;
  int side_b = x * z;
  int side_c = y * z;
  int result = side_a;
  if (side_b < result) {
    result = side_b;
  }
  if (side_c < result) {
    result = side_c;
  }
  return result;
}

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
  int total_area = 0;
  while (std::getline(file_in, current_line)) {
    int area;
    int smallest_side;
    if (current_line.size() > 0) {
      std::vector<int> sides = get_sides(current_line);
      area = (2 * sides[0] * sides[1]) + (2 * sides[1] * sides[2]) + (2 * sides[0] * sides[2]);
      smallest_side = get_smallest_side(sides[0], sides[1], sides[2]);
      total_area += area;
      total_area += smallest_side;
      printf("%s has area of %d and slack of %d total area of %d\n", current_line.c_str(), area, smallest_side, area + smallest_side);
    }
  }
  printf("The answer is: %d\n", total_area);
  return 0;
}
