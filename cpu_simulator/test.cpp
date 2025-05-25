#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// ตัวอย่าง Instruction
enum InstructionType { LOAD, STORE, ADD, SUB, HALT };

// โครงสร้างคำสั่ง
struct Instruction {
    InstructionType type;
    int reg1, reg2, reg3;
    int address_or_value;
};