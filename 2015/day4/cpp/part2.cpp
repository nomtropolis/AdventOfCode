#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <openssl/md5.h>

std::string PUZZLE_INPUT = "ckczppom";

std::string md5thing(std::string guess) {
  unsigned char digest[MD5_DIGEST_LENGTH];
  char digest_str[2*MD5_DIGEST_LENGTH];

  MD5((const unsigned char*)guess.c_str(), guess.length(), digest);

  std::stringstream md5string;
  md5string << std::hex << std::uppercase << std::setfill('0');
  for (const auto &byte: digest){
    md5string << std::setw(2) << (int)byte;
  }
  return md5string.str();
}

int main(int argc, char *argv[]) {
    int counter = 0;
    while(true) {
      counter++;
      std::string guess = PUZZLE_INPUT + std::to_string(counter);
      std::string md5_digest = md5thing(guess);
      if(counter % 100 == 0){
	std::cout << "On count: " << counter << " with guess: " << guess << " : " <<md5_digest << "\n";
      }
      if (md5_digest.rfind("000000", 0) == 0){
	std::cout << "The guess was: " << guess << "\n";
	std::cout << "The matching digest is: " << md5_digest << "\n";
	std::cout << "The matching digest c_str() is: " << md5_digest.c_str() << "\n";	
	std::cout << "The answer is: " << counter << "\n";
	break;
      }
    }
    return 0;
}
