/**
 * Demonstrates composition and encapsulation using Engine and Car classes.
 * @author Jeff Johnson
 * @version 1.0.0
 * @since Week 3 of CSC6301
 */
public class JohnsonJeffPA3 {
    /**
     * The main method demonstrates creating Engine and Car objects and invoking their behaviors.
     * @param args command-line arguments (not used)
     * @since Week 3 of CSC6301
     */
    public static void main(String[] args) {
        Engine electricEngine = new Engine("Electric", 200);
        Car tesla = new Car("Tesla", "Model 3", electricEngine);

        Engine gasolineEngine = new Engine("Gasoline", 150);
        Car honda = new Car("Honda", "Civic", gasolineEngine);

        tesla.drive();
        honda.drive();
    }
}

/**
 * Represents an engine with a type and horsepower.
 * Demonstrates encapsulation by keeping fields private and providing public getters.
 * @author Jeff Johnson
 * @version 1.0.0
 * @since Week 3 of CSC6301
 */
class Engine {
    private String type;
    private int horsepower;

    /**
     * Constructs an Engine with the specified type and horsepower.
     * @param type the type of engine (e.g., "Electric", "Gasoline")
     * @param horsepower the horsepower rating of the engine
     * @since Week 3 of CSC6301
     */
    public Engine(String type, int horsepower) {
        this.type = type;
        this.horsepower = horsepower;
    }

    /**
     * Starts the engine and prints a message to the console.
     * @since Week 3 of CSC6301
     */
    public void start() {
        System.out.println(type + " engine with " + horsepower + " HP started.");
    }

    /**
     * Gets the type of the engine.
     * @return the engine type
     * @since Week 3 of CSC6301
     */
    public String getType() {
        return type;
    }

    /**
     * Gets the horsepower of the engine.
     * @return the engine horsepower
     * @since Week 3 of CSC6301
     */
    public int getHorsepower() {
        return horsepower;
    }
}

/**
 * Represents a car with a make, model, and engine.
 * Demonstrates composition by including an Engine object.
 * @author Jeff Johnson
 * @version 1.0.0
 * @since Week 3 of CSC6301
 */
class Car {
    private String make;
    private String model;
    private Engine engine;

    /**
     * Constructs a Car with the specified make, model, and engine.
     * @param make the car manufacturer
     * @param model the car model
     * @param engine the engine object associated with the car
     * @since Week 3 of CSC6301
     */
    public Car(String make, String model, Engine engine) {
        this.make = make;
        this.model = model;
        this.engine = engine;
    }

    /**
     * Drives the car and starts its engine.
     * Prints a message to the console.
     * @since Week 3 of CSC6301
     */
    public void drive() {
        System.out.println("Driving the " + make + " " + model + ".");
        engine.start();
    }

    /**
     * Gets the make of the car.
     * @return the car make
     * @since Week 3 of CSC6301
     */
    public String getMake() {
        return make;
    }

    /**
     * Gets the model of the car.
     * @return the car model
     * @since Week 3 of CSC6301
     */
    public String getModel() {
        return model;
    }

    /**
     * Gets the engine of the car.
     * @return the Engine object
     * @since Week 3 of CSC6301
     */
    public Engine getEngine() {
        return engine;
    }
}

/**
 * 
 * Class Diagram
 *
 * +-------------------+      +-------------------+      +-------------------+
 * |      Engine       |      |       Car         |      |   JohnsonJeffPA3  |
 * +-------------------+      +-------------------+      +-------------------+
 * | - type: String    |<>----| - make: String    |      | + main(args:      |
 * | - horsepower: int |      | - model: String   |      |   String[]): void |
 * +-------------------+      | - engine: Engine  |      +-------------------+
 * | + Engine(...)     |      +-------------------+
 * | + start(): void   |      | + Car(...)        |
 * | + getType():      |      | + drive(): void   |
 * |   String          |      | + getMake():      |
 * | + getHorsepower():|      |   String          |
 * |   int             |      | + getModel():     |
 * +-------------------+      |   String          |
 *                            | + getEngine():    |
 *                            |   Engine          |
 *                            +-------------------+
 */

/**
 * Note: The JohnsonJeffPA3 class interacts with Car and Engine classes by creating instances of them.
 *
 * Encapsulation:
 *     The Engine and Car classes demonstrate good encapsulation by declaring their instance variables 
 *     (type, horsepower, make, model, engine) as private. 
 *     This restricts direct access from outside the class, 
 *     preventing external code from directly manipulating their internal state.
 *
 * Controlled Access:
 *     Public getter methods (getType(), getHorsepower(), getMake(), getModel(), getEngine()) are provided for
 *     controlled access to the internal data. This allows external code to retrieve information without directly modifying it.
 *
 * Behavioral Abstraction:
 *     The start() method in Engine and drive() method in Car encapsulate the internal 
 *     logic and operations related to starting an engine and driving a car, respectively. 
 *     Users of these classes interact with these methods without needing to know the implementation details.
 *
 * Modularity:
 *     Separation of Concerns:
 *         The code is well-modularized, with each class having a distinct responsibility:
 *         Engine: Manages engine-specific properties and behaviors.
 *         Car: Manages car-specific properties and behaviors, and delegates engine-related tasks to its Engine object.
 *         Main: Orchestrates the creation and interaction of Engine and Car objects.
 */