#include <iostream>
#include <fstream>
#include <string>
using namespace std;
struct Employee
{
    string name;
    string designation;
    int age;
};
void addEmployee()
 {
    Employee emp;
    cout << "Enter name: ";
    cin.ignore();
    getline(cin, emp.name);
    cout << "Enter designation: ";
    getline(cin, emp.designation);
    cout << "Enter age: ";
    cin >> emp.age;
    ofstream file("employees.txt", ios::app);
    file << emp.name << "," << emp.designation << "," << emp.age << endl;
    cout << "Employee added successfully." << endl;
    file.close();
}
void displayEmployees()
{
    ifstream file("employees.txt");
    string line;
    cout << "Employee Records:" << endl;
    cout << "-----------------" << endl;
    while (getline(file, line))
        {
        size_t pos = 0;
        string token;
        while ((pos = line.find(",")) != string::npos)
        {
            token = line.substr(0, pos);
            cout << token << "\t";
            line.erase(0, pos + 1);
        }
        cout << line << endl;
    }

    file.close();
}
int main()
{
    int choice;
    do
        {
        cout << "Employee Record Management" << endl;
        cout << "--------------------------" << endl;
        cout << "1. Add Employee" << endl;
        cout << "2. Display Employees" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch(choice)
        {
            case 1:
                addEmployee();
                break;
            case 2:
                displayEmployees();
                break;
            case 3:
                cout << "Exiting the program..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
        cout << endl;
    } while (choice != 3);
    return 0;
}
