#1 ) Include the docstrings documentation
from random import random


class Queue:
    """    
    This class implements a first in first out (FIFO) data structure using
    two lists: one for enqueuing elements and another for dequeuing elements.
    """
    
    def __init__(self):
        """
        Initialize an empty Queue with two internal lists.
        """
        self.a_in = []
        self.a_out = []
        
        
    def enqueue(self, d):
        """
        Add an element to the back of the queue.
        """
        self.a_in.append(d)
        
    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        
        Returns:
            The element at the front of the queue (the oldest element).
        """
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = [] 
        return self.a_out.pop(0)
    

#2  Convert from python to Java
def RSP():
    guess = ''
    while (True):
        guess = input("Enter (r)ock, (s)cissors, or (p)aper: ")
        if (guess not in ['r', 's', 'p']):
            print("Try again.")
        else:
            break
    rand = random()
    if rand < 1/3:
        comp = 'r'
    elif rand < 2/3:
        comp = 's'
    else:
        comp = 'p'
    
    if guess == comp:
        print("It's a tie!")
    elif (guess == 'r' and comp == 'p') or (guess == 'p' and comp == 's') or (guess == 's' and comp == 'r'):
        print("You lose! Computer chose", comp)
    else:
        print("You win! Computer chose", comp)

RSP()

# import java.util.Random;
# import java.util.Scanner;

# /**
#  * A Rock-Scissors-Paper game implementation.
#  * 
#  * This class provides an interactive game where a player competes against
#  * the computer in a single round of Rock-Scissors-Paper.
#  */
# public class RSP {
    
#     private static final String ROCK = "r";
#     private static final String SCISSORS = "s";
#     private static final String PAPER = "p";
    
#     /**
#      * Main method to run the Rock-Scissors-Paper game.
#      * 
#      * @param args command line arguments (not used)
#      */
#     public static void main(String[] args) {
#         playGame();
#     }
    
#     /**
#      * Executes a single round of Rock-Scissors-Paper.
#      * 
#      * The method prompts the user to enter their choice (rock, scissors, or paper),
#      * validates the input, generates a random choice for the computer, and determines
#      * the winner based on standard Rock-Scissors-Paper rules:
#      * - Rock beats Scissors
#      * - Scissors beats Paper
#      * - Paper beats Rock
#      * 
#      * The computer's choice is randomly generated with equal probability (1/3) for
#      * each option. The game result (win, lose, or tie) is displayed to the user
#      * along with the computer's choice.
#      */
#     public static void playGame() {
#         Scanner scanner = new Scanner(System.in);
#         String playerGuess = "";
        
#         // Input validation loop
#         while (true) {
#             System.out.print("Enter (r)ock, (s)cissors, or (p)aper: ");
#             playerGuess = scanner.nextLine().toLowerCase().trim();
            
#             if (!playerGuess.equals(ROCK) && !playerGuess.equals(SCISSORS) && !playerGuess.equals(PAPER)) {
#                 System.out.println("Try again.");
#             } else {
#                 break;
#             }
#         }
        
#         // Generate computer's choice
#         Random random = new Random();
#         double randomValue = random.nextDouble();
#         String computerChoice;
        
#         if (randomValue < 1.0 / 3.0) {
#             computerChoice = ROCK;
#         } else if (randomValue < 2.0 / 3.0) {
#             computerChoice = SCISSORS;
#         } else {
#             computerChoice = PAPER;
#         }
        
#         // Determine and display the result
#         if (playerGuess.equals(computerChoice)) {
#             System.out.println("It's a tie!");
#         } else if ((playerGuess.equals(ROCK) && computerChoice.equals(PAPER)) ||
#                    (playerGuess.equals(PAPER) && computerChoice.equals(SCISSORS)) ||
#                    (playerGuess.equals(SCISSORS) && computerChoice.equals(ROCK))) {
#             System.out.println("You lose! Computer chose " + computerChoice);
#         } else {
#             System.out.println("You win! Computer chose " + computerChoice);
#         }
        
#         scanner.close();
#     }
# }

#3) Class Diagram

public class Person {
    private String name;
    private int age;
    void display(){
        //methond body
    }

    public class Student extends Person {
        String major;
    }
    
    public class Instructor extends Person {
        String title;
    }
    
    public class Course {
        String name;
        int credits;
        Instructor teacher;
        Student roster[];
        void addStudent(Student name){
            //method body
        }
        void display(){
            //method body
        }
    }
    
    public class OnlineCourse extends Course {
        String meetingId;
        Person helper;
    }
}

# ┌─────────────────────────────┐
# │         Person              │
# ├─────────────────────────────┤
# │ - name: String              │
# │ - age: int                  │
# ├─────────────────────────────┤
# │ + display(): void           │
# └─────────────────────────────┘
#          △           △
#          │           │
#          │           │
#     ┌────┘           └────┐
#     │                     │
# ┌───────────────┐   ┌─────────────────┐
# │   Student     │   │   Instructor    │
# ├───────────────┤   ├─────────────────┤
# │ + major: String│   │ + title: String │
# └───────────────┘   └─────────────────┘
#                             │
#                             │
#                             │ teacher
#                             │ 1
#                     ┌───────▼──────────────┐
#                     │      Course          │
#                     ├──────────────────────┤
#                     │ + name: String       │
#                     │ + credits: int       │
#                     │ + teacher: Instructor│
#                     │ + roster: Student[]  │
#                     ├──────────────────────┤
#                     │ + addStudent(Student)│
#                     │ + display(): void    │
#                     └──────────────────────┘
#                             △
#                             │
#                             │
#                     ┌───────┴──────────────┐
#                     │   OnlineCourse       │
#                     ├──────────────────────┤
#                     │ + meetingId: String  │
#                     │ + helper: Person     │
#                     └──────────────────────┘

# 4) Java Collections

A Stack colletion is last in first out consider a stack of plates you would take from the top.
A Queue collection is first in first out consider a line of people to get into a concert, you take the first person in line.

#5) SDLC Software Development Life Cycle
The advantages of having the SDLC is that it provides a structured to the piece of software being put out. It will ensure that all necessary steps are followed 
and that the final product meets the requirements of the stakeholders. It will helps to identify potential issues early in the development process,
reducing the risk.

#6) Version Control



#7) Profiling

Face value just looking at the code the check function looks to be doing the most its O(n^2) because of the nested loops.
I can also tell its redoing work by counting the number of 0's and 1's in each column every time a new row is added.
Could potentially optimse this by keeping track of the counts of 0's and 1's in each column as rows are added instead of recounting every time.

from intertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)), n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if i in o:
                case.append(1)
            else:
                case.append(0)
        ans.append(tuple(case))
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans +=1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat(n):
    perm = permutations(n)
    ans = layer(0, [], perm, 0)
    return ans

import cProfile
cProfile.run('print("Balanced matrices of size 6:", balanced01mat(6))')


#)8 SDM
Waterfall is defined as a simple approach that is not flexible enough to projects needing adjustments as the project evolves.
Not Agile because it is considered the most flexible and is made for mistakes and errors in the early stages" and uses iterative/incremental approaches.
Not DevOps because it is a mix of both lean and agile so not this one.
So it has to be Lean which has a strategy of "don't do today what can be done tomorrow" which means its not flexible enough for changes during the project which is Waterfall.
