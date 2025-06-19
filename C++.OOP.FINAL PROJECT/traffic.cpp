#include <iostream>
#include <cstring> // for strcpy
using namespace std;

// Define the struct State
struct State {
    char color[10];
    int duration;
};

// Abstract class
class TrafficLightController {
protected:
    State* states;
    int stateCount;
    int currentIndex;

public:
    TrafficLightController() : states(NULL), stateCount(0), currentIndex(0) {}
    virtual ~TrafficLightController() {
        delete[] states;
    }

    virtual void cycle() = 0; // pure virtual
};

// BasicTrafficLight derived class
class BasicTrafficLight : public TrafficLightController {
public:
    BasicTrafficLight() {
        stateCount = 3;
        states = new State[stateCount];
        strcpy(states[0].color, "Green");
        states[0].duration = 60;
        strcpy(states[1].color, "Yellow");
        states[1].duration = 5;
        strcpy(states[2].color, "Red");
        states[2].duration = 55;
    }

    void cycle() {
        State* current = states + currentIndex; // pointer arithmetic
        cout << "[Basic] Light: " << current->color << " for " << current->duration << "s" << endl;
        currentIndex = (currentIndex + 1) % stateCount;
    }
};

// PedestrianTrafficLight derived class
class PedestrianTrafficLight : public TrafficLightController {
public:
    PedestrianTrafficLight() {
        stateCount = 2;
        states = new State[stateCount];
        strcpy(states[0].color, "Walk");
        states[0].duration = 30;
        strcpy(states[1].color, "Don't Walk");
        states[1].duration = 30;
    }

    void cycle() {
        State* current = states + currentIndex; // pointer arithmetic
        cout << "[Pedestrian] Light: " << current->color << " for " << current->duration << "s" << endl;
        currentIndex = (currentIndex + 1) % stateCount;
    }
};

// TrafficSystem to manage controllers
class TrafficSystem {
private:
    TrafficLightController** controllers;
    int controllerCount;

public:
    TrafficSystem() {
        controllers = NULL;
        controllerCount = 0;
    }

    ~TrafficSystem() {
        for (int i = 0; i < controllerCount; i++) {
            delete controllers[i];
        }
        delete[] controllers;
    }

    void addController(TrafficLightController* controller) {
        TrafficLightController** newControllers = new TrafficLightController*[controllerCount + 1];
        for (int i = 0; i < controllerCount; i++) {
            newControllers[i] = controllers[i];
        }
        newControllers[controllerCount] = controller;
        controllerCount++;

        delete[] controllers;
        controllers = newControllers;
    }

    void removeController(int index) {
        if (index < 0 || index >= controllerCount) return;

        delete controllers[index];

        TrafficLightController** newControllers = new TrafficLightController*[controllerCount - 1];
        for (int i = 0, j = 0; i < controllerCount; i++) {
            if (i != index) {
                newControllers[j++] = controllers[i];
            }
        }
        controllerCount--;

        delete[] controllers;
        controllers = newControllers;
    }

    void cycleAll() {
        for (int i = 0; i < controllerCount; i++) {
            controllers[i]->cycle(); // polymorphic dispatch
        }
    }

    int getControllerCount() {
        return controllerCount;
    }
};

// Main function to run the simulation
int main() {
    TrafficSystem system;

    system.addController(new BasicTrafficLight());
    system.addController(new PedestrianTrafficLight());

    for (int i = 0; i < 3; i++) {
        cout << "Cycle " << i + 1 << ":" << endl;
        system.cycleAll();
        cout << "-----------------------" << endl;
    }

    system.removeController(0);
    cout << "After removing controller 0:" << endl;
    system.cycleAll();

    return 0;
}

