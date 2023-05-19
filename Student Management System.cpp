#include <iostream>
#include <fstream>
#include <string>
using namespace std;
struct Student
{
    string name;
    int rollNumber;
    string course;
};
void addStudent()
{
    Student student;
    cout << "Enter name: ";
    cin.ignore();
    getline(cin, student.name);
    cout << "Enter roll number: ";
    cin >> student.rollNumber;
    cout << "Enter course: ";
    cin.ignore();
    getline(cin, student.course);
    ofstream file("students.txt", ios::app);
    file << student.name << "," << student.rollNumber << "," << student.course << endl;
    cout << "Student added successfully." << endl;
    file.close();
}
void displayStudents()
{
    ifstream file("students.txt");
    string line;
    cout << "Student Records:" << endl;
    cout << "----------------" << endl;
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
        cout << "Student Management System" << endl;
        cout << "-------------------------" << endl;
        cout << "1. Add Student" << endl;
        cout << "2. Display Students" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch(choice)
        {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
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
