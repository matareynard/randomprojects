    #include <iostream>
    #include <vector>
    #include <unordered_map>
    #include <cmath>
    #include <conio.h>

    using namespace std;

    // Euclidean Algorithm to find GCD (with progress display)
    int euclideanAlgorithm(int a, int b) {
        cout << "Solving GCD for (" << a << ", " << b << "):" << endl;
        while (b != 0) {
            cout << a << " = " << (a / b) << " * " << b << " + " << (a % b) << endl;
            int temp = b;
            b = a % b;
            a = temp;
        }
        cout << "GCD is: " << a << endl;
        return a;
    }

    unordered_map<int, int> memo; // Memoization map

    int fibonacci(int n) {
        if (n <= 1) {
            cout << "Fib(" << n << ") = " << n << endl;
            return n;
        }

        // Check if result is already calculated
        if (memo.find(n) != memo.end()) {
            return memo[n];
        }

        // Calculate Fibonacci values
        int fib1 = fibonacci(n - 1);
        int fib2 = fibonacci(n - 2);

        // Display the step and result
        cout << "Fib(" << n << ") = Fib(" << n - 1 << ") + Fib(" << n - 2 << ") = " << fib1 << " + " << fib2 << " = " << (fib1 + fib2) << endl;

        // Store the result in memo map
        memo[n] = fib1 + fib2;
        return memo[n];
    }

    // Egyptian Fraction representation (with progress display)
    void egyptianFraction(int numerator, int denominator) {
        cout << "Solving Egyptian Fraction for " << numerator << "/" << denominator << ":" << endl;

        if (denominator == 0 || numerator == 0)
            return;

        if (denominator % numerator == 0) {
            cout << "1/" << denominator / numerator << endl;
            return;
        }

        if (numerator % denominator == 0) {
            cout << numerator / denominator << endl;
            return;
        }

        if (numerator > denominator) {
            cout << numerator / denominator << " + ";
            egyptianFraction(numerator % denominator, denominator);
            return;
        }

        int n = denominator / numerator + 1;
        cout << "1/" << n << " + ";
        egyptianFraction(numerator * n - denominator, denominator * n);
    }

    // Function to check if a number is prime
    bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

    // Function to generate prime numbers up to n
    vector<int> primeNumbersInRange(int start, int end) {
    vector<bool> sieve(end + 1, true);
    sieve[0] = sieve[1] = false;

    for (int i = 2; i * i <= end; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= end; j += i) {
                sieve[j] = false;
            }
        }
    }

    vector<int> primes;
    for (int i = max(2, start); i <= end; i++) {
        if (sieve[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

    // Function to find prime factors of a number
    vector<int> primeFactorization(int n) {
        vector<int> factors;
        for (int i = 2; i <= n; i++) {
            while (isPrime(i) && n % i == 0) {
                factors.push_back(i);
                n /= i;
            }
        }
        return factors;
    }

    // Function to calculate GCD (Greatest Common Divisor)
    int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    // Function to calculate LCM (Least Common Multiple)
    int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    // Addition in Modular Arithmetic
int modAddition(int a, int b, int mod) {
    int result = (a + b) % mod;
    cout << "(" << a << " + " << b << ") mod " << mod << " = " << (a + b) << " mod " << mod << " = " << result << " mod " << mod << endl;
    return result;
}

// Subtraction in Modular Arithmetic
int modSubtraction(int a, int b, int mod) {
    int result = (a - b) % mod;
    if (result < 0) result += mod;  // Ensure the result is non-negative
    cout << "(" << a << " - " << b << ") mod " << mod << " = " << (a - b) << " mod " << mod << " = " << result << " mod " << mod << endl;
    return result;
}

// Multiplication in Modular Arithmetic
int modMultiplication(int a, int b, int mod) {
    int result = (a * b) % mod;
    cout << "(" << a << " x " << b << ") mod " << mod << " = " << (a * b) << " mod " << mod << " = " << result << " mod " << mod << endl;
    return result;
}

// Exponentiation in Modular Arithmetic
int modExponentiation(int base, int exp, int mod) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result = (result * base) % mod;
    }
    cout << base << "^" << exp << " mod " << mod << " = " << result << " mod " << mod << endl;
    return result;
}

    // Function for Modular Arithmetic (a % b)
void modArithmeticMenu() {
    int choice, a, b, mod;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Exponentiation" << endl;
    cout << "5. Back to main menu" << endl;
    cout << "Choose an operation: ";
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "Enter two numbers and the modulus: ";
            cin >> a >> b >> mod;
            modAddition(a, b, mod);
            break;
        case 2:
            cout << "Enter two numbers and the modulus: ";
            cin >> a >> b >> mod;
            modSubtraction(a, b, mod);
            break;
        case 3:
            cout << "Enter two numbers and the modulus: ";
            cin >> a >> b >> mod;
            modMultiplication(a, b, mod);
            break;
        case 4:
            cout << "Enter base, exponent, and modulus: ";
            cin >> a >> b >> mod;
            modExponentiation(a, b, mod);
            break;
        case 5:
            system("CLS");  // Clear the screen and go back to the main menu
            return;
        default:
            cout << "Invalid option! Please choose again." << endl;
            break;
    }
    getch();  // Pause to view result
    system("CLS");
    modArithmeticMenu();  // Display the submenu again
}

    // Menu display
    void displayMenu() {
        cout << "==================== OPTIONS ====================" << endl;
        cout << "1. Euclidean Algorithm (GCD)" << endl;
        cout << "2. Fibonacci Sequence" << endl;
        cout << "3. Egyptian Fraction" << endl;
        cout << "4. Seize of Eratosthenes" << endl;
        cout << "5. Prime Factorization" << endl;
        cout << "6. GCD and LCM" << endl;
        cout << "7. Modular Arithmetic" << endl;
        cout << "8. Exit" << endl;
        cout << "Choose an option: ";
    }

    int main() {
        int choice;

        do {
            displayMenu();
            cin >> choice;

            switch (choice) {
                case 1: {
                    int a, b;
                    cout << "Enter two numbers: ";
                    cin >> a >> b;
                    euclideanAlgorithm(a, b);
                    getch();
                    system("CLS");
                    break;
                }
                case 2: {
                    int n;
                    cout << "Enter the position of Fibonacci number: ";
                    cin >> n;
                    cout << "Calculating Fibonacci sequence..." << endl;
                    int result = fibonacci(n);
                    cout << "Fibonacci number at position " << n << " is: " << result << endl;
                      getch();
                    system("CLS");
                    break;
                }
                case 3: {
                    int num, denom;
                    cout << "Enter numerator and denominator: ";
                    cin >> num >> denom;
                    cout << "Egyptian Fraction representation of " << num << "/" << denom << " is: ";
                    egyptianFraction(num, denom);
                      getch();
                    system("CLS");
                    cout << endl;
                    break;
                }
                case 4: {
                    int start, end;
                cout << "Enter the starting number of the range: ";
                cin >> start;
                cout << "Enter the ending number of the range: ";
                cin >> end;
                vector<int> primes = primeNumbersInRange(start, end);
                cout << "Prime numbers between " << start << " and " << end << ": ";
                for (int prime : primes) {
                    cout << prime << " ";
                }
                cout << endl;
                getch();
                system("CLS");
                break;
            }
                case 5: {
                    int n;
                    cout << "Enter a number to find its prime factors: ";
                    cin >> n;
                    vector<int> factors = primeFactorization(n);
                    cout << "Prime factors of " << n << ": ";
                    for (int factor : factors) {
                        cout << factor << " ";
                    }
                    cout << endl;
                      getch();
                    system("CLS");
                    break;
                }
                case 6: {
                    int a, b;
                    cout << "Enter two numbers to calculate GCD and LCM: ";
                    cin >> a >> b;
                    cout << "GCD of " << a << " and " << b << ": " << gcd(a, b) << endl;
                    cout << "LCM of " << a << " and " << b << ": " << lcm(a, b) << endl;
                      getch();
                    system("CLS");
                    break;
                }
                case 7: {
                modArithmeticMenu();
    getch();
    system("CLS");
    break;
}
                case 8:
                    cout << "Exiting the program. Goodbye!" << endl;
                    break;
                default:
                    cout << "Invalid option! Please choose again." << endl;
            }
        } while (choice != 8);

        return 0;
    }
