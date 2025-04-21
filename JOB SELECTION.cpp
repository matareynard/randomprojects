#include <algorithm>
#include <iostream>
using namespace std;

// A structure to represent a job
struct Job {
    char id;  // Job Id
    int dead; // Deadline of job
    int profit; // Profit if job is over before or on the deadline
};

// Comparator function for sorting jobs by profit in descending order
bool comparison(Job a, Job b) {
    return (a.profit > b.profit);
}

// Function to print job scheduling for maximum profit
void printJobScheduling(Job arr[], int n) {
    // Sort all jobs according to decreasing order of profit
    sort(arr, arr + n, comparison);

    int result[n];  // To store result (Sequence of jobs)
    bool slot[n];   // To keep track of free time slots
    int totalProfit = 0; // Variable to keep track of total profit

    // Initialize all slots to be free
    for (int i = 0; i < n; i++)
        slot[i] = false;

    // Iterate through all given jobs
    for (int i = 0; i < n; i++) {
        // Find a free slot for this job (Note that we start from the last possible slot)
        for (int j = min(n, arr[i].dead) - 1; j >= 0; j--) {
            // Free slot found
            if (slot[j] == false) {
                result[j] = i; // Add this job to result
                slot[j] = true; // Mark this slot as occupied
                totalProfit += arr[i].profit; // Add profit to total profit
                break;
            }
        }
    }

    // Print the result
    cout << "Following is the maximum profit sequence of jobs:\n";
    for (int i = 0; i < n; i++)
        if (slot[i])
            cout << arr[result[i]].id << " ";

    cout << "\nTotal profit: " << totalProfit << endl; // Print total profit
}

// Driver code
int main() {
    int n;

    // Ask the user for the number of jobs
    cout << "Enter the number of jobs: ";
    cin >> n;
    Job arr[n]; // Array to store jobs

    // Get job details from the user
    for (int i = 0; i < n; i++) {
        cout << "job number, deadline, profit" << i + 1 << ":\n";
        cin >> arr[i].id >> arr[i].dead >> arr[i].profit;
    }

    // Once all jobs are entered, calculate the maximum profit sequence
    printJobScheduling(arr, n);

    return 0;
}