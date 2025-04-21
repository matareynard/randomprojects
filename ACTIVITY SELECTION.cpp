#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to compare two activities based on their finish times
bool activityCompare(pair<int, int> a, pair<int, int> b) {
    return a.second < b.second; // Sort by finish time
}

// Prints a maximum set of activities that can be done by a single person, one at a time.
void printMaxActivities(vector<pair<int, int>>& activities) {
    // Sort activities by finish time
    sort(activities.begin(), activities.end(), activityCompare);

    cout << "\nThe result:  ";

    // The first activity always gets selected
    int lastSelectedIndex = 0; // index of last selected activity
    cout << lastSelectedIndex + 1 << " "; // output the activity number (1-based index)

    // Consider the rest of the activities
    for (size_t j = 1; j < activities.size(); j++) {
        // If this activity has a start time greater than or equal to the finish time of the last selected activity
        if (activities[j].first >= activities[lastSelectedIndex].second) {
            cout << j + 1 << " "; // output the activity number (1-based index)
            lastSelectedIndex = j; // Update the index of the last selected activity
        }
    }
    cout << endl;
}

// Driver code
int main() {
    int n;

    // Ask the user for the number of activities
    cout << "Enter the number of activities: ";
    cin >> n;

    // Check if the number of activities is valid
    if (n <= 0) {
        cout << "Please enter a valid number of activities." << endl;
        return 1;
    }

    vector<pair<int, int>> activities(n); // Vector to store pairs of start and finish times

    // Input start and finish times
    for (int i = 0; i < n; i++) {
        cout << "Start time and finish time for " << (i + 1) << ": ";
        cin >> activities[i].first >> activities[i].second;
    }

    // Call the function to print the maximum set of activities
    printMaxActivities(activities);

    return 0;
}