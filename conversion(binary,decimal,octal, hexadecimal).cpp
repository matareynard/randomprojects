#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <string>
#include <bitset>

using namespace std;

// Function to convert binary string to double (supports large binary numbers and fractions)
double binaryToDouble(const string &binary) {
    size_t pos = binary.find('.');
    unsigned long long integerPart = 0;
    double fractionalPart = 0.0;

    if (pos != string::npos) {
        integerPart = bitset<64>(binary.substr(0, pos)).to_ullong();
    } else {
        integerPart = bitset<64>(binary).to_ullong();
    }

    if (pos != string::npos) {
        string fracPart = binary.substr(pos + 1);
        for (size_t i = 0; i < fracPart.length(); ++i) {
            if (fracPart[i] == '1') {
                fractionalPart += 1.0 / (1ULL << (i + 1));
            }
        }
    }

    return integerPart + fractionalPart;
}

// Function to convert octal string to double
double octalToDouble(const string &octal) {
    size_t pos = octal.find('.');
    unsigned int integerPart = 0;
    double fractionalPart = 0.0;

    if (pos != string::npos) {
        integerPart = stoi(octal.substr(0, pos), nullptr, 8);
    } else {
        integerPart = stoi(octal, nullptr, 8);
    }

    if (pos != string::npos) {
        string fracPart = octal.substr(pos + 1);
        for (size_t i = 0; i < fracPart.length(); ++i) {
            fractionalPart += (fracPart[i] - '0') / pow(8, i + 1);
        }
    }

    return integerPart + fractionalPart;
}

// Function to convert hexadecimal string to double
double hexToDouble(const string &hex) {
    size_t pos = hex.find('.');
    unsigned int integerPart = 0;
    double fractionalPart = 0.0;

    if (pos != string::npos) {
        integerPart = stoi(hex.substr(0, pos), nullptr, 16);
    } else {
        integerPart = stoi(hex, nullptr, 16);
    }

    if (pos != string::npos) {
        string fracPart = hex.substr(pos + 1);
        for (size_t i = 0; i < fracPart.length(); ++i) {
            if (isdigit(fracPart[i]))
                fractionalPart += (fracPart[i] - '0') / pow(16, i + 1);
            else
                fractionalPart += (toupper(fracPart[i]) - 'A' + 10) / pow(16, i + 1);
        }
    }

    return integerPart + fractionalPart;
}

// Function to convert fractional decimal to binary, octal, or hexadecimal with exact precision
string convertFractionalToBase(double fractionalPart, int base, int precision = 10) {
    string result = ".";
    int count = 0;

    while (fractionalPart > 0 && count < precision) {
        fractionalPart *= base;
        int integerPart = static_cast<int>(fractionalPart);
        if (integerPart < 10)
            result += to_string(integerPart);
        else
            result += static_cast<char>('A' + integerPart - 10); // for hex digits
        fractionalPart -= integerPart;
        count++;
    }

    // Pad with '0' to ensure precision if necessary
    while (count < precision) {
        result += '0';
        count++;
    }

    return result;
}

// Function to display the result in binary, octal, decimal, or hexadecimal
void displayInFormat(double num, int targetBase, int fractionalPrecision = 16) {  // Increase precision for binary fractional parts
    unsigned long long integerPart = static_cast<unsigned long long>(num);
    double fractionalPart = num - integerPart;

    if (targetBase == 2) {
        // Convert integer part to binary
        string intBinary = bitset<64>(integerPart).to_string();
        intBinary = intBinary.substr(intBinary.find('1'));

        // Display integer and fractional parts in binary
        cout << "Binary:      " << intBinary;
        if (fractionalPart > 0) {
            cout << convertFractionalToBase(fractionalPart, 2, fractionalPrecision);  // Increased precision for binary
        }
        cout << endl;
    } else if (targetBase == 10) {
        cout << "Decimal:     " << fixed << setprecision(16) << num << endl;
    } else if (targetBase == 8) {
        cout << "Octal:       " << oct << integerPart;
        if (fractionalPart > 0) {
            cout << convertFractionalToBase(fractionalPart, 8, fractionalPrecision);
        }
        cout << endl;
    } else if (targetBase == 16) {
        cout << "Hexadecimal: " << hex << uppercase << integerPart;
        if (fractionalPart > 0) {
            cout << convertFractionalToBase(fractionalPart, 16, fractionalPrecision);
        }
        cout << endl;
    }
}

// Function to get the input from the user and convert it to a double
double getNumberFromUser(int base) {
    string numStr;
    cout << "Enter the number in base " << base << ": ";
    cin >> numStr;

    if (base == 16)
        return hexToDouble(numStr);
    else if (base == 8)
        return octalToDouble(numStr);
    else if (base == 2)
        return binaryToDouble(numStr);
    else
        return stod(numStr);
}

void displayMenu() {
    cout << "\n========= Number System Converter =========\n";
    cout << "1. Enter a number in Binary\n";
    cout << "2. Enter a number in Decimal\n";
    cout << "3. Enter a number in Octal\n";
    cout << "4. Enter a number in Hexadecimal\n";
    cout << "5. Exit\n";
    cout << "===========================================\n";
}

int displayTargetMenu(int inputBase) {
    cout << "\nSelect the target format:\n";
    if (inputBase != 2) cout << "1. Binary\n";
    if (inputBase != 10) cout << "2. Decimal\n";
    if (inputBase != 8) cout << "3. Octal\n";
    if (inputBase != 16) cout << "4. Hexadecimal\n";
    cout << "===========================================\n";
    cout << "Select an option: ";

    int choice;
    cin >> choice;

    if (inputBase != 2 && choice == 1) return 2;
    if (inputBase != 10 && choice == 2) return 10;
    if (inputBase != 8 && choice == 3) return 8;
    if (inputBase != 16 && choice == 4) return 16;

    return -1;
}

int main() {
    int choice;
    double number = 0;

    while (true) {
        displayMenu();
        cout << "Select an option: ";
        cin >> choice;

        if (choice == 5) {
            cout << "Exiting...\n";
            break;
        }

        int inputBase = 0;
        switch (choice) {
            case 1: inputBase = 2; break;
            case 2: inputBase = 10; break;
            case 3: inputBase = 8; break;
            case 4: inputBase = 16; break;
            default:
                cout << "Invalid option. Please try again.\n";
                continue;
        }

        number = getNumberFromUser(inputBase);
        int targetBase = displayTargetMenu(inputBase);
        
        if (targetBase == -1) {
            cout << "Invalid target option. Please try again.\n";
            continue;
        }

        displayInFormat(number, targetBase);
    }

    return 0;
}
